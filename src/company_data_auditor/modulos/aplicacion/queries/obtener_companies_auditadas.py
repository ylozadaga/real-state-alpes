from company_data_auditor.seedwork.aplicacion.queries import Query, QueryHandler, ResultadoQuery
import uuid

class ObtenerCompaniesAuditadas(Query):
    status: str

class ObtenerCompaniesAuditadasHandler(QueryHandler):

    def handle() -> ResultadoQuery:
        ...