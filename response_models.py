"""
Defines Pydantic response models for various WooCommerce API endpoints.

Attributes:
    response_models (dict): A dictionary mapping API endpoints to their
    corresponding response models.

"""
import models
from pydantic import BaseModel


class ShopCouponList(BaseModel):
    __root__: list[models.ShopCoupon]


class CustomerDownloadList(BaseModel):
    __root__: list[models.CustomerDownload]


class CustomerList(BaseModel):
    __root__: list[models.Customer]


class OrderNoteList(BaseModel):
    __root__: list[models.OrderNote]


class ShopOrderRefundList(BaseModel):
    __root__: list[models.ShopOrderRefund]


class ShopOrderList(BaseModel):
    __root__: list[models.ShopOrder]


class ProductAttributeTermList(BaseModel):
    __root__: list[models.ProductAttributeTerm]


class ProductAttributeList(BaseModel):
    __root__: list[models.ProductAttribute]


class ProductCatList(BaseModel):
    __root__: list[models.ProductCat]


class ProductReviewList(BaseModel):
    __root__: list[models.ProductReview]


class ProductShippingClassList(BaseModel):
    __root__: list[models.ProductShippingClass]


class ProductTagList(BaseModel):
    __root__: list[models.ProductTag]


class ProductList(BaseModel):
    __root__: list[models.Product]


class ProductVariationList(BaseModel):
    __root__: list[models.ProductVariation]


class SalesReportList(BaseModel):
    __root__: list[models.SalesReport]


class TopSellersReportList(BaseModel):
    __root__: list[models.TopSellersReport]


class ReportOrderTotalList(BaseModel):
    __root__: list[models.ReportOrderTotal]


class ReportProductTotalList(BaseModel):
    __root__: list[models.ReportProductTotal]


class ReportCustomerTotalList(BaseModel):
    __root__: list[models.ReportCustomerTotal]


class ReportCouponTotalList(BaseModel):
    __root__: list[models.ReportCouponTotal]


class ReportReviewTotalList(BaseModel):
    __root__: list[models.ReportReviewTotal]


class ReportList(BaseModel):
    __root__: list[models.Report]


class ShippingZoneList(BaseModel):
    __root__: list[models.ShippingZone]


class ShippingZoneLocationList(BaseModel):
    __root__: list[models.ShippingZoneLocation]


class ShippingZoneMethodList(BaseModel):
    __root__: list[models.ShippingZoneMethod]


class TaxClassList(BaseModel):
    __root__: list[models.TaxClass]


class TaxList(BaseModel):
    __root__: list[models.Tax]


class WebhookList(BaseModel):
    __root__: list[models.Webhook]


class SystemStatusToolList(BaseModel):
    __root__: list[models.SystemStatusTool]


class ShippingMethodList(BaseModel):
    __root__: list[models.ShippingMethod]


class PaymentGatewayList(BaseModel):
    __root__: list[models.PaymentGateway]


class DataContinentsList(BaseModel):
    __root__: list[models.DataContinents]


class DataCountriesList(BaseModel):
    __root__: list[models.DataCountries]


class DataCurrenciesList(BaseModel):
    __root__: list[models.DataCurrencies]


response_models = {'get': {
    '/coupons': ShopCouponList,
    '/coupons/{id}': models.ShopCoupon,
    '/customers/{customer_id}/downloads': CustomerDownloadList,
    '/customers': CustomerList,
    '/customers/{id}': models.Customer,
    '/orders/{order_id}/notes': OrderNoteList,
    '/orders/{order_id}/notes/{id}': models.OrderNote,
    '/orders/{order_id}/refunds': ShopOrderRefundList,
    '/orders/{order_id}/refunds/{id}': models.ShopOrderRefund,
    '/orders': ShopOrderList,
    '/orders/{id}': models.ShopOrder,
    '/products/attributes/{attribute_id}/terms': ProductAttributeTermList,
    '/products/attributes/{attribute_id}/terms/{id}': models.ProductAttributeTerm,
    '/products/attributes': ProductAttributeList,
    '/products/attributes/{id}': models.ProductAttribute,
    '/products/categories': ProductCatList,
    '/products/categories/{id}': models.ProductCat,
    '/products/reviews': ProductReviewList,
    '/products/reviews/{id}': models.ProductReview,
    '/products/shipping_classes': ProductShippingClassList,
    '/products/shipping_classes/{id}': models.ProductShippingClass,
    '/products/tags': ProductTagList,
    '/products/tags/{id}': models.ProductTag,
    '/products': ProductList,
    '/products/{id}': models.Product,
    '/products/{product_id}/variations': ProductVariationList,
    '/products/{product_id}/variations/{id}': models.ProductVariation,
    '/reports/sales': SalesReportList,
    '/reports/top_sellers': TopSellersReportList,
    '/reports/orders/totals': ReportOrderTotalList,
    '/reports/products/totals': ReportProductTotalList,
    '/reports/customers/totals': ReportCustomerTotalList,
    '/reports/coupons/totals': ReportCouponTotalList,
    '/reports/reviews/totals': ReportReviewTotalList,
    '/reports': ReportList,
    '/shipping/zones': ShippingZoneList,
    '/shipping/zones/{id}': models.ShippingZone,
    '/shipping/zones/{id}/locations': ShippingZoneLocationList,
    '/shipping/zones/{zone_id}/methods': ShippingZoneMethodList,
    '/shipping/zones/{zone_id}/methods/{instance_id}': models.ShippingZoneMethod,
    '/taxes/classes': TaxClassList,
    '/taxes/classes/{slug}': models.TaxClass,
    '/taxes': TaxList,
    '/taxes/{id}': models.Tax,
    '/webhooks': WebhookList,
    '/webhooks/{id}': models.Webhook,
    '/system_status': models.SystemStatus,
    '/system_status/tools': SystemStatusToolList,
    '/system_status/tools/{id}': models.SystemStatusTool,
    '/shipping_methods': ShippingMethodList,
    '/shipping_methods/{id}': models.ShippingMethod,
    '/payment_gateways': PaymentGatewayList,
    '/payment_gateways/{id}': models.PaymentGateway,
    '/data': models.DataIndex,
    '/data/continents': DataContinentsList,
    '/data/continents/{location}': models.DataContinents,
    '/data/countries': DataCountriesList,
    '/data/countries/{location}': models.DataCountries,
    '/data/currencies': DataCurrenciesList,
    '/data/currencies/current': models.DataCurrencies,
    '/data/currencies/{currency}': models.DataCurrencies,
}}
