from company_data_auditor.seedwork.aplicacion.queries import Query, QueryHandler, ResultadoQuery
import uuid

class ObtenerUsuariosDesactivados(Query):
    status: str

class ObtenerUsuariosDesactivadosHandler(QueryHandler):

    def handle() -> ResultadoQuery:
        ...