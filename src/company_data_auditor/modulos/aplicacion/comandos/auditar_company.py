from company_data_auditor.seedwork.aplicacion.comandos import Comando, ComandoHandler
from company_data_auditor.seedwork.aplicacion.comandos import ejecutar_commando as comando
from company_data_auditor.modulos.dominio.entidades import Company
#from company_data_auditor.modulos.dominio.objetos_valor import Fechas 
from dataclasses import dataclass
import datetime

@dataclass
class ComandoAuditarCompany(Comando):
    id: str
    registration_date: datetime
    renovation_date: datetime
    nit: str
    acronym: str
    status: str
    validity: str
    organization_type: str
    registration_category: str

class AuditarCompanyHandler(ComandoHandler):

    def a_entidad(self, comando: ComandoAuditarCompany) -> Company:
        params = dict(
            id = comando.id, 
            registration_date = comando.registration_date, 
            renovation_date = comando.renovation_date, 
            nit = comando.nit,
            acronym = comando.acronym, 
            status = comando.status, 
            validity = comando.validity, 
            organization_type = comando.organization_type, 
            registration_category = comando.registration_category, 
            audit_date = datetime.datetime.now()
        )

        company = Company(**params)
        return company
        

    def handle(self, comando: ComandoAuditarCompany):
        company = self.a_entidad(comando)
        
        
@comando.register(ComandoAuditarCompany)
def ejecutar_comando_auditar_company(comando: ComandoAuditarCompany):
    handler = AuditarCompanyHandler()
    handler.handle(comando)
