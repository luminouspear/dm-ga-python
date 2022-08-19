# crud application for products in a store

# What are we storing about products?
# name
# description
# id
# price
# id,name,description,price


# create a product



# read product data


# update a product


# delete a product

import pandas as pd
from flask import Flask, render_template
import json

app = Flask(__name__)

#route to display all products
@app.route('/products')
def get_products(): #list all of the products
    #read my products file
    product_list = pd.read_csv('products.csv')
    product_dict = product_list.to_dict('records')
  
    # parsed_data = json.loads(product_list.to_json())
    # return parsed_data
    return render_template('products.html', products=product_dict)

#[{id:, name, description, price}, {id:, name, description, price}]
@app.route('/productlist')
def get_productlist(): 
    product_list = pd.read_csv('products.csv')
    output_list = []
    # for item in product_list:
    #     output_list.append({})

    product_dict = product_list.to_dict('records')

    # with open("products.csv", "r") as file:
    #     print(file.readlines())
    #     print(file.to_dict())

    return product_dict


#to start the server

if __name__ == '__main__':
    app.run()

# return 