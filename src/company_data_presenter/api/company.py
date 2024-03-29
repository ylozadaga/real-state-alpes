import company_data_presenter.seedwork.presentation.api as api
import json

from flask import request, Response

from company_data_presenter.modules.company.application.services import CompanyService

from company_data_presenter.modules.company.application.mappers import MapperCompanyDTOJson
from company_data_presenter.modules.company.application.commands.create_company import CreateCompany
from company_data_presenter.modules.company.infrastructure.dispatchers import Dispatcher

from company_data_presenter.seedwork.domain.exceptions import DomainException


bp = api.create_blueprint('presenter', '/presenter')

dispatcher = Dispatcher()

@bp.route('/company/private', methods=('GET',))
@bp.route('/company/private/<id>', methods=('GET',))
def find_company(id=None):
    sr = CompanyService()
    map_company = MapperCompanyDTOJson()
    if id:
        return map_company.dto_to_outer(sr.find_company_by_id(id))
    else:
        return [map_company.dto_to_outer(company) for company in sr.find_all_companies()]
