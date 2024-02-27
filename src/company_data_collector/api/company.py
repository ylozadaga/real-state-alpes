import src.company_data_collector.seedwork.presentation.api as api
import json

from flask import request, Response

from src.company_data_collector.modules.company.application.mappers import MapperCompanyDTOJson
from src.company_data_collector.modules.company.application.commands.create_company import CreateCompany
from src.company_data_collector.modules.company.infrastructure.dispatchers import Dispatcher

from src.company_data_collector.seedwork.domain.exceptions import DomainException


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
