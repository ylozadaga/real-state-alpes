from pydispatch import dispatcher

from .handlers import HandlerCompanyDomain
from ..domain.events import CompanyCreated

dispatcher.connect(HandlerCompanyDomain.handle_company_created,
                   signal=CompanyCreated.__name__)
