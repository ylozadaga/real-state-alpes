from strawberry.fastapi import GraphQLRouter
from .queries import Query
from .mutations import Mutation

import strawberry


schema = strawberry.Schema(query=Query, mutation=Mutation)
router = GraphQLRouter(schema)