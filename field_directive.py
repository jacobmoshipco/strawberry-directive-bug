

from fastapi import FastAPI
import strawberry
from strawberry.schema_directive import Location
from strawberry.fastapi import GraphQLRouter

@strawberry.schema_directive(locations=[Location.FIELD_DEFINITION])
class TestDirective: pass

@strawberry.type
class Query:
    @strawberry.field(directives=[TestDirective()])
    def test() -> str:
        return "Test"

schema = strawberry.Schema(Query, schema_directives=[TestDirective])

router = GraphQLRouter(schema, prefix='/graphql', graphql_ide="apollo-sandbox")
app = FastAPI()
app.include_router(router)

