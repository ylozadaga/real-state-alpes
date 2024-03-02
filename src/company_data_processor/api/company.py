import company_data_processor.seedwork.presentation.api as api
import json

from flask import request, Response

from company_data_processor.modules.company.application.services import CompanyService

from company_data_processor.modules.company.application.mappers import MapperCompanyDTOJson
from company_data_processor.modules.company.application.commands.create_company import CreateCompany
from company_data_processor.modules.company.infrastructure.dispatchers import Dispatcher

from company_data_processor.seedwork.domain.exceptions import DomainException

bp = api.create_blueprint('company', '/company')

dispatcher = Dispatcher()


@bp.route('/async/commands', methods=('POST',))
def create_company():
    try:
        company_dict = request.json
        company_mapper = MapperCompanyDTOJson()
        company_dto = company_mapper.outer_to_dto(company_dict)
        command = CreateCompany(company_dto)
        dispatcher.publish_command(command, "commands-company")
        return Response('{}', status=202, mimetype='application/json')
    except DomainException as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')


@bp.route('/company/private/<id>', methods=('GET',))
def find_company(id):
    sr = CompanyService()

    return sr.find_company_by_id(id)


@bp.route('/company/private', methods=('GET',))
def find_all_companies():
    sr = CompanyService()

    return sr.find_all_companies()
