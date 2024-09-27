
import traceback
from typing import Callable
from strawberry.cli.utils import load_schema
from strawberry.printer import print_schema

DIRECTIVE_NAMES_QUERY = 'query { __schema { directives { name } } }'

def test_field_directive_schema_export():
    schema_symbol = load_schema("field_directive:schema", ".")
    output = print_schema(schema_symbol)
    assert "testDirective" in output

def test_one_of_schema_export():
    schema_symbol = load_schema("one_of_directive:schema", ".")
    output = print_schema(schema_symbol)
    assert "oneOf" in output

def test_field_directive_introspection():
    from field_directive import schema
    result = schema.execute_sync(DIRECTIVE_NAMES_QUERY)
    directives = { directive['name'] for directive in result.data['__schema']['directives'] }
    assert "testDirective" in directives

def test_one_of_introspection():
    from one_of_directive import schema
    result = schema.execute_sync(DIRECTIVE_NAMES_QUERY)
    directives = { directive['name'] for directive in result.data['__schema']['directives'] }
    assert "oneOf" in directives


def run_test(test: Callable):
    print("\n" + test.__name__.replace('_', ' ') + ": ", end="")
    try:
        test()
        print("PASS")
    except:
        print("FAIL")
        traceback.print_exc()

def run_tests():
    run_test(test_field_directive_schema_export)
    run_test(test_one_of_schema_export)
    run_test(test_field_directive_introspection)
    run_test(test_one_of_introspection)

if __name__ == '__main__':
    run_tests()
