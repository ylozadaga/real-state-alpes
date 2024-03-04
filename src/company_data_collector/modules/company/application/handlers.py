from ....seedwork.application.handlers import Handler
from ..infrastructure.dispatchers import Dispatcher


class HandlerCompanyDomain(Handler):

    @staticmethod
    def handle_company_created(event):
        dispatcher = Dispatcher()
        dispatcher.publish_event(event, 'events-company')
