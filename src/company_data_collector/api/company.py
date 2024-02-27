import src.company_data_collector.seedwork.presentation.api as api
import json
from src.company_data_collector.modules.company.application.services import CompanyService
from src.company_data_collector.modules.company.application.dto import CompanyDTO
from src.company_data_collector.seedwork.domain.exceptions import DomainException

from flask import redirect, render_template, request, session, url_for
from flask import Response
from src.company_data_collector.modules.company.application.mappers import MapperCompanyDTOJson
from src.company_data_collector.modules.company.application.commands.create_company import CreateCompany
from src.company_data_collector.seedwork.application.commands import execute_command

bp = api.create_blueprint('company', '/companies')


@bp.route('/commands/', methods=('POST',))
def create_company():
    try:
        company_dict = request.json

        mapped_company = MapperCompanyDTOJson()
        company_dto = mapped_company.outer_to_dto(company_dict)

        comando = CreateCompany(company_dto.creation_date, company_dto.update_date, company_dto.id)

        execute_command(comando)

        return Response('{}', status=202, mimetype='application/json')
    except DomainException as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
