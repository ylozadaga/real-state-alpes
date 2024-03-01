from src.company_data_presenter.seedwork.domain.exceptions import FactoryException


class ObjectTypeNotExistInDomainCompanyException(FactoryException):
    def __init__(self, message='there is no factory for given type in domain company'):
        self.__message = message

    def __str__(self):
        return str(self.__message)
