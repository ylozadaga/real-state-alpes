import src.company_data_presenter.seedwork.presentation.api as api
import json

from flask import request, Response

from src.company_data_presenter.modules.company.application.services import CompanyService

from src.company_data_presenter.modules.company.application.mappers import MapperCompanyDTOJson
from src.company_data_presenter.modules.company.application.commands.create_company import CreateCompany
from src.company_data_presenter.modules.company.infrastructure.dispatchers import Dispatcher

from src.company_data_presenter.seedwork.domain.exceptions import DomainException


bp = api.create_blueprint('company', '/company')

dispatcher = Dispatcher()


@bp.route('/company/private/<id>', methods=('GET',))
def find_company(id):
        sr = CompanyService()

    return sr.find_company_by_id(id)


@bp.route('/company/private', methods=('GET',))
def find_all_companies():
    sr = CompanyService()

    return sr.find_all_companies()

