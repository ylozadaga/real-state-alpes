from ....seedwork.domain.exceptions import FactoryException


class FactoryTypeNotImplementedException(FactoryException):
    def __init__(self, message='There is no implementation for the given repository type.'):
        self.__message = message

    def __str__(self):
        return str(self.__message)
