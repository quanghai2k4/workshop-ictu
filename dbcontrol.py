import datetime
import os
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
connstr = os.environ.get("CONNSTR")
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
def insert_acc(username, password, role):
    account.insert_one({'username': username, 'password': password, 'role': role})

def insert_employee(_id, name, age, sex, address, phone, position, salary):
    employee.insert_one({'_id': _id, 'name': name, 'age': age, 'sex': sex, 'address': address, 'phone': phone, 'position': position, 'salary': salary})

def insert_product(_id, name, price, quantity):
    product.insert_one({'_id': _id, 'name': name, 'price': price, 'stock': quantity})

def insert_customer(_id, name, address, phone, email):
    customer.insert_one({'_id': _id, 'name': name, 'address': address, 'phone': phone, 'email': email})

def insert_order(_id, customer_id, products, total):
    order.insert_one({'_id': _id, 'customer_id': customer_id, 'product_id': [products], 'total': total})

def insert_service(_id, name, price):
    service.insert_one({'_id': _id, 'name': name, 'price': price})  
#---------------------------------------------
    
#---------------------------------------------
# update data to mongodb
def update_acc(username, password, role):
    account.update_one({'username': username}, {'$set': {'password': password, 'role': role}})

def update_employee(_id, name, age, sex, phone, address, position, salary):
    employee.update_one({'_id': _id}, {'$set': {'name': name, 'age': age, 'sex': sex, 'phone': phone, 'address': address, 'position': position, 'salary': salary}})

def update_product(_id, name, price, quantity):
    product.update_one({'_id': _id}, {'$set': {'name': name, 'price': price, 'stock': quantity}})

def update_customer(_id, name, address, phone, email):
    customer.update_one({'_id': _id}, {'$set': {'name': name, 'address': address, 'phone': phone, 'email': email}})

def update_order(_id, customer_id, orderdate, enddate, detail, total, status):
    order.update_one({'_id': _id}, {'$set': {'customer_id': customer_id, 'orderdate': orderdate, 'enddate': enddate, 'detail': detail, 'total': total, 'status': status, 'order date': datetime.datetime.now()}})

def update_service(_id, name, price):
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
# check account is exist or not
def check_acc(username, password):
    if account.find_one({'username': username,'password': password, 'role':1}):
        return True
    elif account.find_one({'username': username,'password': password,'role':0}):
        return True
    else:
        return False
#---------------------------------------------