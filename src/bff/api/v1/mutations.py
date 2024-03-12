import strawberry
import typing

from strawberry.types import Info
from bff import utils
from bff.dispatchers import Dispatcher

from .schemes import *

@strawberry.type
class Mutation:
    @strawberry.mutation #TODO DEFINIR AGREGAR EL ID DE CORRELACION
    async def create_company(self, correlation_id: str, nit:str, status:str,  organization_type:str, registration_category:str,info:Info) -> CompanyResponse:
        print(f"Nit compania: {nit}, ID Correlación: {correlation_id}")
        payload = dict(
            correlation_id = correlation_id,
            nit = nit,
            status = status,
            organization_type = organization_type,
            registration_category = registration_category,
            registration_date = utils.time_millis()
        )
        command = dict(
            id = str(uuid.uuid4()),
            time=utils.time_millis(),
            specversion = "v1",
            type = "CompanyCommand",
            ingestion=utils.time_millis(),
            datacontenttype="AVRO",
            service_name = "BFF",
            data = payload
        )
        dispatcher = Dispatcher()
        info.context["background_tasks"].add_task(dispatcher.publish_message, command, "command-create-company",  "public/default/command-create-company")

        return CompanyResponse(message="Processing message", status= 203)

    @strawberry.mutation #TODO DEFINIR AGREGAR EL ID DE CORRELACION
    async def update_company(self, correlation_id: str, nit:str, status:str,  organization_type:str, registration_category:str,info:Info) -> CompanyResponse:
        print(f"Nit compania: {nit}, ID Correlación: {correlation_id}")
        payload = dict(
            correlation_id = correlation_id,
            nit = nit,
            status = status,
            organization_type = organization_type,
            registration_category = registration_category,
            registration_date = utils.time_millis()
        )
        command = dict(
            id = str(uuid.uuid4()),
            time=utils.time_millis(),
            specversion = "v1",
            type = "CompanyCommand",
            ingestion=utils.time_millis(),
            datacontenttype="AVRO",
            service_name = "BFF",
            data = payload
        )
        dispatcher = Dispatcher()
        info.context["background_tasks"].add_task(dispatcher.publish_message, command, "command-update-company",  "public/default/command-update-company")

        return CompanyResponse(message="Processing message", status= 203)

