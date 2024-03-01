from src.company_data_presenter.seedwork.domain.rules import BusinessRule


class IsValidDataFormat(BusinessRule):

    def __init__(self, message='invalid data format'):
        super().__init__(message)

    def is_valid(self) -> bool:
        return True
