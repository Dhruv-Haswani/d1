import faker as fk
from faker import Faker
import numpy as np
import pandas as pd
import random

fake = Faker()

categories = {
    "Furniture": ["Office chair", "Study Table", "Sofa", "Bookshelf", "Bed"],
    "Office supplies": ["Pen", "Notebook", "Stapler", "File folder", "Calculator"],
    "Electronics": ["Laptop", "Keyboard", "Mouse", "Headphones", "Monitor"],
    "Grocery": ["Rice bag", "Cooking oil", "Sugar", "Wheat", "Biscuits"]
}

regions = ["North", "South", "East", "West"]
payment_modes = ["Cash", "CC", "UPI", "NB"]
del_status = ["Delivered", "Pending", "Returned", "Cancelled"]
customer_segments = ["Consumer", "Corporate", "Home office"]

records = []

for i in range(1000):
    order_id = f"ord{1000 + i}"
    order_date = fake.date_between(start_date='-1y', end_date='today')
    ship_date = order_date + pd.Timedelta(days=random.randint(1, 7))

    customer_name = fake.name()
    customer_id = f"Cust{random.randint(100, 999)}"
    customer_segment = random.choice(customer_segments)

    category = random.choice(list(categories.keys()))
    prod_name = random.choice(categories[category])
    prod_id = f"prod{random.randint(1000, 9999)}"

    region = random.choice(regions)
    state = fake.state()
    city = fake.city()

    quantity = random.randint(1, 10)
    unit_price = random.randint(100, 5000)
    discount = random.choice([0, 5, 10, 15, 20])

    sales_amount = quantity * unit_price * (1 - discount / 100)
    cp = sales_amount * random.uniform(0.6, 0.9)
    profit = sales_amount - cp

    stock_left = random.randint(0, 50)
    supplier_name = fake.company()
    supplier_email = fake.company_email()
    payment_mode = random.choice(payment_modes)
    delivery = random.choice(del_status)

    if stock_left < 10:
        auto_reorder = "Yes"
        reorder_quantity = random.randint(20, 50)
    else:
        auto_reorder = "No"
        reorder_quantity = 0

    # append inside loop  👇
    records.append({
        "Order id": order_id,
        "order date": order_date,
        "ship date": ship_date,
        "customer id": customer_id,
        "customer segment": customer_segment,
        "product id": prod_id,
        "product name": prod_name,
        "category": category,
        "region": region,
        "state": state,
        "City": city,
        "Quantity": quantity,
        "Unit price": unit_price,
        "discount(%)": discount,
        "Sales amount": round(sales_amount, 2),
        "cost price": round(cp, 2),
        "profit": round(profit, 2),
        "Payment Mode": payment_mode,
        "Delivery status": delivery,
        "Supplier name": supplier_name,
        "Supplier email": supplier_email,
        "stock left": stock_left,
        "Auto reorder": auto_reorder,
        "reorder quantity": reorder_quantity
    })

df = pd.DataFrame(records)

try:
    df.to_csv("Superstore Management System.csv", index=False)
    print("Dataset generated successfully and saved as 'Superstore Management System.csv'")
except PermissionError:
    print("Please close the file 'Superstore Management System.csv' if open in Excel")
