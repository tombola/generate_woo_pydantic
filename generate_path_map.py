import yaml
from rich import print
from pydantic import BaseModel
from typing import List
import textwrap


with open('woocommerce-openapi-3.0.x.yml', 'r') as file:
    data = yaml.safe_load(file)

def get_model_from_ref(ref:str):
    ref_name = ref.split('/')[-1]
    components = ref_name.split('_')
    camel_case_name = ''.join(x.title() for x in components)
    return camel_case_name

def list_model_definition(list_model_name:str, model_name:str):
    return textwrap.dedent(f"""
            class {list_model_name}(BaseModel):
                __root__: list[models.{model_name}]

            """)

response_models = {}
path_response_models = {"get": {}}

for path, verbs in data['paths'].items():

    print(f"[cyan bold]{path}[/cyan bold]")
    for verb, details in verbs.items():
        print(f"  [red]{verb}[/red]")

        # TODO: handle other http verbs
        if verb != 'get':
            continue

        schema:dict = {}
        try:
            schema = details['responses']['200']['content']['application/json']['schema']
        except KeyError:
            continue

        if "type" in schema:
            if schema['type'] == 'array':
                model_name = get_model_from_ref(schema['items']['$ref'])
                list_model_name = model_name + 'List'
                response_models[list_model_name] = list_model_definition(
                    list_model_name,
                    model_name,
                )
                path_response_models['get'][path] = list_model_name
                print(f"    list[{model_name}]")
            elif schema['type'] == '$ref':
                model_name = get_model_from_ref(schema['$ref'])
                path_response_models['get'][path] = f"models.{model_name}"
                print(f"    {model_name}")
        elif "$ref" in schema:
            model_name = get_model_from_ref(schema['$ref'])
            path_response_models['get'][path] = f"models.{model_name}"
            print(f"    {model_name}")


with open('response_models.py', 'w') as f:

    f.write(textwrap.dedent(f"""\
            \"\"\"
            Defines Pydantic response models for various WooCommerce API endpoints.

            Attributes:
                response_models (dict): A dictionary mapping API endpoints to their
                corresponding response models.

            \"\"\"

            """))
    f.write("import models\n")
    f.write("from pydantic import BaseModel\n\n")


    for model_name, model_code in response_models.items():
        f.write(model_code)

    f.write("\nresponse_models = {'get': {\n")
    for path, model_name in path_response_models["get"].items():
        f.write(f"    '{path}': {model_name},\n")
    f.write("}}\n")
