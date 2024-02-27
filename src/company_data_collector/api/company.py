import src.company_data_collector.seedwork.presentation.api as api
import json
from src.company_data_collector.modules.company.application.services import CompanyService
from src.company_data_collector.modules.company.application.dto import CompanyDTO
from src.company_data_collector.seedwork.domain.exceptions import DomainException

from flask import redirect, render_template, request, session, url_for
from flask import Response
from src.company_data_collector.modules.company.application.mappers import MapperCompanyDTOJson
from src.company_data_collector.modules.company.application.commands.collect_company_data import CollectCompanyData
from src.company_data_collector.modules.company.application.queries.get_company import GetCompany
from src.company_data_collector.seedwork.application.commands import execute_command
from src.company_data_collector.seedwork.application.queries import execute_query

bp = api.create_blueprint('company', '/companies')


@bp.route('/commands/', methods=('POST',))
def create_company():
    try:
        company_dict = request.json

        mapped_company = MapperCompanyDTOJson()
        company_dto = mapped_company.externo_a_dto(company_dict)

        comando = CreateCompany(company_dto.fecha_creacion, company_dto.fecha_actualizacion, company_dto.id,
                               company_dto.itinerarios)

        execute_command(comando)

        return Response('{}', status=202, mimetype='application/json')
    except DomainException as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
