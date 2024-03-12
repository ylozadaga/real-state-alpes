import typing
import strawberry
import uuid
import requests
import os

from datetime import datetime

RS_ALPES_HOST = os.getenv("RS_ALPES_ADDRESS", default="localhost")
DATE_FORMAT = "%Y-%m-%dT%H:%M:%SZ"


def get_company(root, id) -> typing.List["Company"]:
    companies_json = requests.get(f"http://{RS_ALPES_HOST}:5000/presenter/companies/private/" + id).json()  # TODO VERIFICAR URI
    return Company(
                id = company.get('id'),
                nit = company.get('nit', ''),
                status = company.get('status', ''),
                organization_type = company.get('organization_type', ''),
                registration_category = company.get('registration_category', ''),
                registration_date = datetime.strptime(company.get('registration_date', DATE_FORMAT))
            ) 

def get_companies(root) -> Company:
    companies_json = requests.get(f"http://{RS_ALPES_HOST}:5000/presenter/companies/private").json()  # TODO VERIFICAR URI
    companies = []

    for company in companies_json:
        companies.append(
            Company(
                id = company.get('id'),
                nit = company.get('nit', ''),
                status = company.get('status', ''),
                organization_type = company.get('organization_type', ''),
                registration_category = company.get('registration_category', ''),
                registration_date = datetime.strptime(company.get('registration_date', DATE_FORMAT))
            )
        )
    return companies

@strawberry.type
class Company:
    id: str
    nit: str
    status: str
    organization_type: str
    registration_category: str
    registration_date: datetime


@strawberry.type
class CompanyResponse:
    status: int
    message: str