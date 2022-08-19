from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import json

app = Flask(__name__)


@app.route('/')
def index():
    car_list = fetch_car_list()
    return render_template('list_cars.html', car_list=car_list)


@app.route('/new', methods=['GET', 'POST'])
def add_new_product():
    if request.method == 'GET':
        return render_template('new_data.html')
    else:
        cars = fetch_car_list()
        car_make = request.form['make']
        car_model = request.form['model']
        car_year = request.form['year']
        car_color = request.form['color']
        car_mileage = request.form['mileage']
        car_price = request.form['price']
        car_id = cars[len(cars) - 1]['id'] + 1
        new_car = get_new_car(car_id, car_make, car_model, car_year,
                              car_color, car_mileage, car_price)
        cars.append(new_car)

        write_csv(cars)

        return redirect(url_for('index'))


@app.route('/cars/<id>', methods=['GET', 'PUT', 'POST'])
def edit_car(id):
    cars = fetch_car_list()

    for car in cars:
        if car['id'] == int(id):
            selected_car = car
            break

    if request.method == 'GET':
        return render_template('edit_data.html', car=selected_car)
    else:
        data = {
            'id': car['id'],
            'make': request.form['make'],
            'model': request.form['model'],
            'year': request.form['year'],
            'color': request.form['color'],
            'mileage': request.form['mileage'],
            'price': request.form['price'],
        }
        update_cars(cars, data)
        write_csv(cars)
        return redirect(url_for('index'))


@app.route('/cars/<id>/delete', methods=['POST'])
def delete(id):
    print(f'id is {id}')
    delete_car(id)
    return redirect(url_for('index'))


def fetch_car_list():
    car_list = pd.read_csv('cars.csv')
    return car_list.to_dict('records')


def get_new_car(car_id, car_make, car_model, car_year, car_color, car_mileage, car_price):
    return {
        'id': car_id,
        'make': car_make,
        'model': car_model,
        'year': car_year,
        'color': car_color,
        'mileage': car_mileage,
        'price': car_price
    }


def update_cars(cars, new_car):
    for index in range(len(cars)):
        if new_car['id'] == cars[index]['id']:
            cars[index] = new_car
            break


def delete_car(id):
    cars = fetch_car_list()
    new_car_list = [car for car in cars if not (car['id'] == int(id))]
    write_csv(new_car_list)


def write_csv(cars):
    df = pd.DataFrame(cars).set_index('id')
    df.to_csv('cars.csv')


if __name__ == '__main__':
    app.run(debug=True)
