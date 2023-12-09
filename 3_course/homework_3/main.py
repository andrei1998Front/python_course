import json
from datetime import datetime

from flask import Flask, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Unicode, Column, Integer, Date
from sqlalchemy.orm.exc import UnmappedInstanceError
from utils import get_data_from_json, convert_to_list

app = Flask(__name__)

app.config.from_pyfile('./config.py')
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    first_name = Column(Unicode)
    last_name = Column(Unicode)
    age = Column(Integer)
    email = Column(Unicode())
    role = Column(Unicode)
    phone = Column(Unicode)

    def as_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "email": self.email,
            "role": self.role,
            "phone": self.phone
        }


class Order(db.Model):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True)
    name = Column(Unicode)
    start_date = Column(Date)
    end_date = Column(Date)
    address = Column(Unicode)
    price = Column(Integer)
    customer_id = Column(Integer, db.ForeignKey('user.id'))
    executor_id = Column(Integer, db.ForeignKey('user.id'))

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "start_date": self.start_date.strftime("%d.%m.%Y"),
            "end_date": self.end_date.strftime("%d.%m.%Y"),
            "address": self.address,
            "price": self.price,
            "customer_id": self.customer_id,
            "executor_id": self.executor_id
        }


class Offer(db.Model):
    __tablename__ = 'offer'

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, db.ForeignKey('order.id'))
    executor_id = Column(Integer, db.ForeignKey('user.id'))

    def as_dict(self):
        return {
            "id": self.id,
            "order_id": self.order_id,
            "executor_id": self.executor_id,
        }


with app.app_context():
    db.drop_all()
    db.create_all()

    data_dict = get_data_from_json(app.config.get('JSON_PATH'))

    for user in data_dict['users']:
        db.session.add(
            User(
                first_name=user['first_name'],
                last_name=user['last_name'],
                age=user['age'],
                email=user['email'],
                role=user['role'],
                phone=user['phone']
            )
        )

    for order in data_dict['orders']:
        db.session.add(
            Order(
                name=order['name'],
                start_date=order['start_date'],
                end_date=order['end_date'],
                address=order['address'],
                price=order['price'],
                customer_id=order['customer_id'],
                executor_id=order['executor_id']
            )
        )

    for offer in data_dict['offers']:
        db.session.add(
            Offer(
                order_id=offer['order_id'],
                executor_id=offer['executor_id']
            )
        )

    db.session.commit()


@app.route('/users', methods=["GET", "POST"])
def users_page():
    if request.method == 'GET':
        users = convert_to_list(User.query.all())

        return json.dumps(users, ensure_ascii=False, sort_keys=True, indent=4)
    elif request.method == 'POST':
        users_data = json.loads(request.data)

        nested = db.session.begin_nested()
        try:
            db.session.add(User(
                    first_name=users_data['first_name'],
                    last_name=users_data['last_name'],
                    age=users_data['age'],
                    email=users_data['email'],
                    role=users_data['role'],
                    phone=users_data['phone']
                )
            )
        except KeyError as e:
            nested.rollback()
            return 'Ошибка ключа!'

        db.session.commit()

        return redirect('/users')


@app.route('/users/<int:user_id>', methods=["GET", "PUT", "DELETE"])
def user_by_id_page(user_id: int):
    query = User.query.get(user_id)

    if request.method == "GET":
        return json.dumps(query.as_dict(), ensure_ascii=False, sort_keys=True, indent=4)
    elif request.method == "PUT":
        users_data = json.loads(request.data)

        nested = db.session.begin_nested()
        try:
            query.first_name = users_data['first_name']
            query.last_name = users_data['last_name']
            query.age = users_data['age']
            query.email = users_data['email']
            query.role = users_data['role']
            query.phone = users_data['phone']

            db.session.add(query)
        except KeyError as e:
            nested.rollback()
            return 'Ошибка ключа!'

        db.session.commit()

        return redirect('/users')
    elif request.method == 'DELETE':
        nested = db.session.begin_nested()

        try:
            db.session.delete(query)
        except UnmappedInstanceError as e:
            return "Не существует такого пользователя!"

        db.session.commit()
        return redirect('/users')


@app.route('/orders', methods=["GET", "POST"])
def orders_page():
    if request.method == 'GET':
        orders = convert_to_list(Order.query.all())

        return json.dumps(orders, ensure_ascii=False, sort_keys=True, indent=4)

    elif request.method == 'POST':
        order_data = json.loads(request.data)

        nested = db.session.begin_nested()
        try:
            db.session.add(Order(
                    name=order_data['name'],
                    start_date=datetime.strptime(order_data['start_date'], "%m/%d/%Y").date(),
                    end_date=datetime.strptime(order_data['end_date'], "%m/%d/%Y").date(),
                    address=order_data['address'],
                    price=order_data['price'],
                    customer_id=order_data['customer_id'],
                    executor_id=order_data['executor_id']
                )
            )
        except KeyError as e:
            nested.rollback()
            return 'Ошибка ключа!'

        db.session.commit()

        return redirect('/orders')


@app.route('/orders/<int:order_id>', methods=["GET", "PUT", "DELETE"])
def order_by_id_page(order_id):
    query = Order.query.get(order_id)

    if request.method == "GET":
        return json.dumps(query.as_dict(), ensure_ascii=False, sort_keys=True, indent=4)
    elif request.method == "PUT":
        order_data = json.loads(request.data)

        nested = db.session.begin_nested()

        try:
            query.name = order_data['name']
            query.start_date = datetime.strptime(order_data['start_date'], "%m/%d/%Y").date()
            query.end_date = datetime.strptime(order_data['end_date'], "%m/%d/%Y").date()
            query.address = order_data['address']
            query.price = order_data['price']
            query.customer_id = order_data['customer_id']
            query.executor_id = order_data['executor_id']

            db.session.add(query)
        except KeyError as e:
            nested.rollback()
            return 'Ошибка ключа!'

        db.session.commit()

        return redirect('/orders')
    elif request.method == 'DELETE':
        nested = db.session.begin_nested()

        try:
            db.session.delete(query)
        except UnmappedInstanceError as e:
            return "Не существует такого пользователя!"

        db.session.commit()
        return redirect('/orders')


@app.route('/offers', methods=['GET', 'POST'])
def offers_page():
    if request.method == 'GET':
        offers = convert_to_list(Offer.query.all())

        return json.dumps(offers, ensure_ascii=False, sort_keys=True, indent=4)

    elif request.method == 'POST':
        offers_data = json.loads(request.data)

        nested = db.session.begin_nested()
        try:
            db.session.add(Offer(
                    order_id=offers_data['order_id'],
                    executor_id=offers_data['executor_id']
                )
            )
        except KeyError as e:
            nested.rollback()
            return 'Ошибка ключа!'

        db.session.commit()

        return redirect('/offers')


@app.route('/offers/<int:offer_id>', methods=['GET', 'PUT', 'DELETE'])
def offer_by_id_page(offer_id):
    query = Offer.query.get(offer_id)

    if request.method == "GET":
        return json.dumps(query.as_dict(), ensure_ascii=False, sort_keys=True, indent=4)
    elif request.method == "PUT":
        offer_data = json.loads(request.data)

        nested = db.session.begin_nested()

        try:
            query.order_id = offer_data['order_id']
            query.executor_id = offer_data['executor_id']

            db.session.add(query)
        except KeyError as e:
            nested.rollback()
            return 'Ошибка ключа!'

        db.session.commit()

        return redirect('/offers')
    elif request.method == 'DELETE':
        nested = db.session.begin_nested()

        try:
            db.session.delete(query)
        except UnmappedInstanceError as e:
            return "Не существует такого пользователя!"

        db.session.commit()
        return redirect('/offers')


if __name__ == "__main__":
    app.run(debug=True)
