

from fastapi import FastAPI
import strawberry
from strawberry.fastapi import GraphQLRouter

@strawberry.input(one_of=True)
class TestInput:
    a: str | None = strawberry.UNSET
    b: str | None = strawberry.UNSET

@strawberry.type
class Query:
    @strawberry.field
    def test(x: TestInput) -> str:
        return "Test"

schema = strawberry.Schema(Query)

router = GraphQLRouter(schema, prefix='/graphql', graphql_ide="apollo-sandbox")
app = FastAPI()
app.include_router(router)

