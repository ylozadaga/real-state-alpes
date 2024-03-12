import strawberry
from .schemes import *

@strawberry.type
class Query:
    companies: typing.List[Company] = strawberry.field(resolver=get_companies)
    company : Company = strawberry.field(resolver=get_company)