from datetime import datetime
import os
from unittest import result
import pyarrow
import pandas
import pymongoarrow as pma
from pymongoarrow.api import Schema
from pymongoarrow.monkey import patch_all
from pymongo import MongoClient
from dotenv import find_dotenv, load_dotenv

# Load environment variables
load_dotenv(find_dotenv())

# Patch all methods
patch_all()

# Connect to MongoDB
connstr = os.environ.get("ATLAS_URI")
client = MongoClient(connstr)
wood = client.wood
# Create collections
account = wood.account
employee = wood.employees
product = wood.products
customer = wood.customers
order = wood.orders
service = wood.services

#---------------------------------------------
#---------------------------------------------
# load data from mongodb
def load_acc():
    df = account.find_pandas_all({})
    return df

def load_employee():
    df = employee.find_pandas_all({})
    return df

def load_product():
    df = product.find_pandas_all({})
    return df

def load_customer():
    df = customer.find_pandas_all({})
    return df

def load_order():
    df = order.find_pandas_all({})
    return df

def load_service():
    df = service.find_pandas_all({})
    return df
#---------------------------------------------

#---------------------------------------------
# insert data to mongodb
def insert_acc(_id, username, password, role):
    account.insert_one({'_id': _id, 'username': username, 'password': password, 'role': role})

def insert_employee(_id, name, birthday, sex, address, phone, position, salary):
    birthday = datetime.combine(birthday, datetime.min.time())
    employee.insert_one({'_id': _id, 'name': name, 'birthday': birthday, 'sex': sex, 'address': address, 'phone number': phone, 'position': position, 'salary': salary, 'start date': datetime.now()})

def insert_product(_id, name, price, quantity):
    price = float(price)
    product.insert_one({'_id': _id, 'name': name, 'price': price, 'quantity': quantity})

def insert_customer(_id, name, address, phone, email):
    customer.insert_one({'_id': _id, 'name': name, 'address': address, 'phone number': phone, 'email': email})

def insert_order(_id, address, total, products, customer_id):
    order.insert_one({'_id': _id, 'address': address, 'order date': datetime.now(), 'total': total, 'detail': products, 'customer_id': customer_id, 'status': 'Pending'})

def insert_service(_id, name, price):
    price = float(price)
    service.insert_one({'_id': _id, 'name': name, 'price': price})  
#---------------------------------------------
    
#---------------------------------------------
# update data to mongodb
def update_acc(username, password, role):
    account.update_one({'username': username}, {'$set': {'password': password, 'role': role}})

def update_employee(_id, name, birthday, sex, phone, address, position, salary):
    birthday = datetime.strptime(birthday, "%Y-%m-%d").date()
    birthday = datetime.combine(birthday, datetime.min.time())
    employee.update_one({'_id': _id}, {'$set': {'name': name, 'birthday': birthday, 'sex': sex, 'phone': phone, 'address': address, 'position': position, 'salary': salary}})

def update_product(_id, name, price, quantity):
    product.update_one({'_id': _id}, {'$set': {'name': name, 'price': price, 'stock': quantity}})

def update_customer(_id, name, address, phone, email):
    customer.update_one({'_id': _id}, {'$set': {'name': name, 'address': address, 'phone': phone, 'email': email}})

def update_order(_id, customer_id, orderdate, enddate, detail, total, status):
    order.update_one({'_id': _id}, {'$set': {'customer_id': customer_id, 'orderdate': orderdate, 'enddate': enddate, 'detail': detail, 'total': total, 'status': status, 'order date': datetime.now()}})

def update_service(_id, name, price):
    price = float(price)
    service.update_one({'_id': _id}, {'$set': {'name': name, 'price': price}})
    
#---------------------------------------------
# delete data from mongodb
def delete_acc(_id):
    account.delete_one({'_id': _id})

def delete_employee(_id):
    employee.delete_one({'_id': _id})

def delete_product(_id):
    product.delete_one({'_id': _id})

def delete_customer(_id):
    customer.delete_one({'_id': _id})

def delete_order(_id):
    order.delete_one({'_id': _id})

def delete_service(_id):
    service.delete_one({'_id': _id})
#---------------------------------------------

#---------------------------------------------
# Functions of chart

#get total revenue
def total_revenue():
    total = 0
    for i in order.find():
        total += i['total']
    return total

# get total number of products
def total_products():
    total = 0
    for i in product.find():
        total += i['quantity']
    return total

# get total of customers
def total_customers():
    total = 0
    for i in customer.find():
        total += 1
    return total

# get length of detail in order
def total_detail():
    total = 0
    for i in order.find():
        total += len(i['detail'])
    return total
#---------------------------------------------

#---------------------------------------------
# get price of product
def get_price_product(name):
    result = product.find_one({'name': name})
    if result is not None:
        return result['price']
    else:
        return 0
    

#---------------------------------------------

#---------------------------------------------
# check account is exist or not
def check_acc(username, password):
    try:
        result = account.find_one({'$and': [{'username': username}, {'password': password}]})
        if result is not None:
            return result['role']  # Return the role
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
#---------------------------------------------