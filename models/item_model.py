import sqlite3
from db import db


class ItemModel(db.Model):

    __tablename__ = 'items'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision =2))

    store_id = db.Column(db.Integer,db.ForeignKey('stores.id'))
    store = db.relationship("StoreModel")

    def __init__(self,name,price,store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name':self.name,'price':self.price}

    @classmethod
    def find_item_by_name(cls,name):
        return cls.query.filter_by(name = name).first() # SELECT * FROM items WHERE name = name LIMIT 1
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query = "SELECT * FROM items WHERE name = ?"
        # result = cursor.execute(query, (name,))
        # row = result.fetchone()
        #
        # if row:
        #     # return {'item': {'name': row[0], 'price': row[1]}}, 200
        #     return cls(*row)# return cls(row[0],row[1])

    # insert method changes into save_to_db
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query = "INSERT INTO items VALUES(?,?)"
        # cursor.execute(query, (self.name, self.price))
        #
        # connection.commit()
        # connection.close()

    # No need of update method as save_to_db is doing both insert and update is
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # query = "UPDATE items SET price = ? WHERE name= ?"
        #
        # cursor.execute(query, (self.name, self.price))
        # connection.commit()
        # connection.close()

        # '''Another way of updating item'''
        # global items
        # items = list(filter(lambda x:x['name']!=name,items))
        # data = request.get_json()
        # item = {
        #         "name" : name,
        #         "price" : data['price']
        #     }
        # items.append(item)
        # return {'item' : item},200