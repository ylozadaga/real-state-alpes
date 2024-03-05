from abc import ABC, abstractmethod
from enum import Enum

from ..domain.entities import RootAggregation
from pydispatch import dispatcher

import pickle


class Lock(Enum):
    OPTIMISTIC = 1
    PESSIMISTIC = 2


class Batch:
    def __init__(self, operation, lock: Lock, *args, **kwargs):
        self.operation = operation
        self.args = args
        self.lock = lock
        self.kwargs = kwargs


class WorkUnit(ABC):

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.rollback()

    def _get_events(self, batches=None):
        batches = self.batches if batches is None else batches
        for batch in batches:
            for arg in batch.args:
                if isinstance(arg, RootAggregation):
                    return arg.events
        return list()

    @abstractmethod
    def _clear_batches(self):
        raise NotImplementedError

    @abstractmethod
    def batches(self) -> list[Batch]:
        raise NotImplementedError

    @abstractmethod
    def save_points(self) -> list:
        raise NotImplementedError

    def commit(self):
        self._publish_events_post_commit()
        self._clear_batches()

    @abstractmethod
    def rollback(self, savepoint=None):
        self._clear_batches()

    @abstractmethod
    def savepoint(self):
        raise NotImplementedError

    def register_batch(self, operation, *args, lock=Lock.PESSIMISTIC, **kwargs):
        batch = Batch(operation, lock, *args, **kwargs)
        self.batches.append(batch)
        self._publish_domain_events(batch)

    def _publish_domain_events(self, batch):
        for event in self._get_events(batches=[batch]):
            dispatcher.send(signal=f'{type(event).__name__}Domain', event=event)

    def _publish_events_post_commit(self):
        for event in self._get_events():
            dispatcher.send(signal=f'{type(event).__name__}Integration', event=event)


def is_flask():
    try:
        from flask import session
        return True
    except Exception:
        return False


def register_work_unit(serialized_obj):
    from company_data_collector.config.uow import WorkUnitSQLAlchemy
    from flask import session

    session['uow'] = serialized_obj


def flask_uow():
    from flask import session
    from company_data_collector.config.uow import WorkUnitSQLAlchemy
    if session.get('uow'):
        return session['uow']
    else:
        uow_serialized = pickle.dumps(WorkUnitSQLAlchemy())
        register_work_unit(uow_serialized)
        return uow_serialized


def work_unit() -> WorkUnit:
    if is_flask():
        return pickle.loads(flask_uow())
    else:
        raise Exception('There is no Work Unit')


def save_work_unit(uow: WorkUnit):
    if is_flask():
        register_work_unit(pickle.dumps(uow))
    else:
        raise Exception('There is no Work Unit')


class UnitWorkPort:

    @staticmethod
    def commit():
        uow = work_unit()
        uow.commit()
        save_work_unit(uow)

    @staticmethod
    def rollback(savepoint=None):
        uow = work_unit()
        uow.rollback(savepoint=savepoint)
        save_work_unit(uow)

    @staticmethod
    def savepoint():
        uow = work_unit()
        uow.savepoint()
        save_work_unit(uow)

    @staticmethod
    def get_save_points():
        uow = work_unit()
        return uow.save_points()

    @staticmethod
    def register_batch(operation, *args, lock=Lock.PESSIMISTIC, **kwargs):
        uow = work_unit()
        uow.register_batch(operation, *args, lock=lock, **kwargs)
        save_work_unit(uow)
