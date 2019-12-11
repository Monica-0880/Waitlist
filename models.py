from Waitlist import db
from flask_login import UserMixin
from Waitlist import login
from datetime import datetime

@login.user_loader
def load_user(id):
    return Restaurant.query.get(int(id))

# Restaurant model
class Restaurant(UserMixin, db.Model):
    id = db.Column( db.Integer, primary_key=True )
    company_name = db.Column( db.String(120))
    username = db.Column( db.String(120))
    password = db.Column( db.String(120))
    customers = db.relationship( 'Customer', backref= 'restaurant')
    seating_tables = db.relationship( 'Seating_table', backref= 'restaurant')
    reservations = db.relationship( 'Reservation', backref= 'restaurant')

    def __init__(self, company_name, username, password):
        self.company_name = company_name
        self.username = username
        self.password = password

# Customer model
class Customer(db.Model):
    id = db.Column( db.Integer, primary_key=True )
    name = db.Column( db.String(120))
    email = db.Column( db.String(120))
    phone_number = db.Column( db.Integer)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))
    reservations = db.relationship( 'Reservation', backref= 'customer')


    def __init__(self, name, email, phone_number,restaurant):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.restaurant = restaurant

        

# Reservation model
class Reservation(db.Model):
    id = db.Column( db.Integer, primary_key=True )
    reservation_time = db.Column( db.String(120))
    status = db.Column( db.String(120))
    number_people = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))
    seating_reservations = db.relationship( 'Seating_reservation', backref= 'reservation')


    def __init__(self, reservation_time, status, restaurant, customer, number_people):
        self.reservation_time = reservation_time
        self.status = status
        self.number_people
        self.restaurant = restaurant
        self.customer = customer
        


# Seating table model   
class Seating_table(db.Model):
    id = db.Column( db.Integer, primary_key=True )
    table_number = db.Column( db.Integer)
    seats = db.Column( db.Integer)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))
    seating_reservations = db.relationship( 'Seating_reservation', backref= 'seating_table')


    def __init__(self, table_number, seats, restaurant):
        self.table_number = table_number
        self.seats = seats
        self.restaurant = restaurant


# Seating reservation 
class Seating_reservation(db.Model):
    id = db.Column( db.Integer, primary_key=True )
    reservation_id = db.Column(db.Integer, db.ForeignKey('reservation.id'))
    seating_table_id = db.Column(db.Integer, db.ForeignKey('seating_table.id'))

    def __init__(self,reservation, seating_table):
        self.reservation = reservation
        self.seating_table = seating_table