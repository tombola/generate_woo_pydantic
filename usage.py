import os
from datetime import datetime
import models
import json
import models
from woocommerce import API

def get_first_day_of_month():
    now = datetime.now()
    first_day_of_month = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    return first_day_of_month.isoformat()

def get_this_months_orders():
    wcapi = API(
        url=os.environ.get('WC_URL'),
        consumer_key=os.environ.get('WC_KEY'),
        consumer_secret=os.environ.get('WC_SECRET'),
        version="wc/v3",
        # For local testing only
        # verify_ssl=False,
    )
    response = wcapi.get("orders", params={"after": get_first_day_of_month()})
    return response.json()

# orders_data = get_this_months_orders()

# Or load the JSON data from the file
with open('./responses/orders.json') as f:
    orders_data = json.load(f)

# Parse JSON data into list of ShopOrder objects
orders = []
for order in orders_data:
    # Assigned to a variable to view in debugger
    shop_order = models.ShopOrder(**order)
    orders.append(shop_order)

for order in orders:
    print(order)
