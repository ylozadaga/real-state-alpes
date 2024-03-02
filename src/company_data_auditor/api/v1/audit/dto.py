from pydantic import BaseModel
from datetime import datetime

class AuditCompany(BaseModel):
    id: str
    registration_date: datetime
    renovation_date: datetime
    nit: str
    acronym: str
    status: str
    validity: str
    organization_type: str
    registration_category: str
