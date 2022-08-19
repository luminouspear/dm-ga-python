from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/products')
def get_products():
    product_list = fetch_product_list()
    return render_template('products.html', products=product_list)


@app.route('/products/new', methods=['GET', 'POST'])
def add_new_product():
    if request.method == 'GET':
        return render_template('new-product.html')
    else:
        products = pd.read_csv('products.csv')
        product_list = products.to_dict('records')
        product_name = request.form['name']
        product_description = request.form['description']
        product_price = request.form['price']
        product_id = product_list[len(product_list) - 1]['id'] + 1
        new_product = {
            'id': product_id,
            'name': product_name,
            'description': product_description,
            'price': product_price,
        }
        product_list.append(new_product)
        df = pd.DataFrame(product_list).set_index('id')

        df.to_csv('products.csv')

        return redirect(url_for('get_products'))

# route to edit each product


@app.route('/products/<id>/delete')
def delete_product(id):
    delete_product(request.form('delete'))
    return redirect(url_for('get_products'))


@app.route('/products/<id>', methods=['GET', 'PUT', 'POST'])
def edit_product(id):
    product_list = fetch_product_list()

    # create a new template to update the product
    # load the "add new page" with the data from the object
    # allow editing from that page to save here

    for product in product_list:
        if product['id'] == int(id):
            selected_product = product
            break

    # if this is a GET request, show the form with the data

    if request.method == 'GET':
        return render_template('edit-product.html', product=selected_product)
    else:

        data = {

            'id': product['id'],
            'name': request.form['name'],
            'description': request.form['description'],
            'price': request.form['price']
        }
        update_product(product_list, data)
        df = pd.DataFrame(product_list).set_index('id')
        df.to_csv('products.csv')
        return redirect(url_for('get_products'))


def fetch_product_list():
    products = pd.read_csv('products.csv')
    return products.to_dict('records')


def update_product(product_list, new_product):
    for idx in range(len(product_list)):
        if new_product['id'] == product_list[idx]['id']:
            product_list[idx] = new_product
            break


def delete_product(id):
    product_list = fetch_product_list()

    new_list = [product for product in product_list if not (
        product['id'] == int(id))]
    df - pd.DataFrame(new_list).set_index('id')
    df.to_csv('products.csv')

# create a route called /hello
# returns "hey there"


@app.route('/hello')
def hello():
    return 'hey there'

# implement a route that returns the classmate that matches an id
# create a list of disctionaries, with each name having an id


@app.route('/classmates/<id>')
def get_classmates_by_id(id):
    names = [
        {"id": 1, "name": "Dan"},
        {"id": 2, "name": "Pavel"},
        {"id": 3, "name": "Son"},
        {"id": 4, "name": "Ella"},
        {"id": 5, "name": "Priscilla"},
        {"id": 6, "name": "Sanjeev"}
    ]
    name = names[id]
    print(name)
    return {"response_code": 200, "data": f'{name}'}


# create a route called classmates
# that returns a list of your classmates
@app.route('/classmates')
def get_classmates():
    classmates = ['Dan', 'Pavel', 'Son', 'Ella', 'Priscilla', 'Sanjeev']

    return {"response_code": 200, "data": f'{classmates}'}


if __name__ == '__main__':
    app.run(debug=True)
