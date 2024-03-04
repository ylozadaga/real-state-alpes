from company_data_auditor.seedwork.aplicacion.queries import Query, QueryHandler, ResultadoQuery
import uuid

class ObtenerCompany(Query):
    listing_id: uuid.UUID

class ObtenerCompanyHandler(QueryHandler):

    def handle() -> ResultadoQuery:
        ...