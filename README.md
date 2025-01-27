Example using
[datamodel-code-generator](https://github.com/koxudaxi/datamodel-code-generator)
to generate pydantic models from an [OpenAPI schema for WooCoomerce](https://github.com/gerbrand/WooCommerce-OpenAPI-Client/blob/main/src/main/resources/woocommerce-openapi-3.0.x.yml).

These can hopefully then be used when working with the [WooCommerce
API](https://woocommerce.github.io/woocommerce-rest-api-docs/) from python, in
order to validate the records returned within API responses.

- `generate.sh` command to run the code generator
- `models.py` the resulting pydantic models
- `pyproject.toml` / `uv.lock` environment and dependencies handled by [uv](https://docs.astral.sh/uv/)
- `woocommerce-openapi-3.0.x.yml` the OpenAPI schema ([source](https://github.com/gerbrand/WooCommerce-OpenAPI-Client/blob/main/src/main/resources/woocommerce-openapi-3.0.x.yml))