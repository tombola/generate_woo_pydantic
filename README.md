# WooCommerce to Pydantic Example

Example using
[datamodel-code-generator](https://github.com/koxudaxi/datamodel-code-generator)
to generate pydantic models from an [OpenAPI schema for WooCoomerce](https://github.com/gerbrand/WooCommerce-OpenAPI-Client/blob/main/src/main/resources/woocommerce-openapi-3.0.x.yml).

These can hopefully then be used when working with the [WooCommerce
API](https://woocommerce.github.io/woocommerce-rest-api-docs/) from python, in
order to validate the records returned within API responses.

Another key advantage of using the pydantic models is that autocomplete in your editor will
supply all the relevant properties for each record returned by an API response
and all the nested properties. This should make working with the responses **much** easier.

## Overview of repo files

- `generate_models.sh` command to run the code generator
- `generate_models.sh` python command to generate a dictionary mapping 'path' to
  pydantic model (for use in woocommerce_pydantic package)
- `models.py` the resulting pydantic models
- `pyproject.toml` / `uv.lock` environment and dependencies handled by [uv](https://docs.astral.sh/uv/)
- `response_models.py` the results from `generate_models.sh` python command
- `usage.py` A usage example validating orders returned from the WC API
- `woocommerce-openapi-3.0.x.yml` the OpenAPI schema ([source](https://github.com/gerbrand/WooCommerce-OpenAPI-Client/blob/main/src/main/resources/woocommerce-openapi-3.0.x.yml))
