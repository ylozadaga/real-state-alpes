from company_data_auditor.seedwork.aplicacion.queries import Query, QueryHandler, ResultadoQuery
import uuid

class ObtenerTodasCompanies(Query):
    ...

class ObtenerTodasCompaniesHandler(QueryHandler):

    def handle() -> ResultadoQuery:
        ...