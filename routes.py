from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, login_required, logout_user
from Waitlist.models import Restaurant, Customer, Reservation
from Waitlist import app
from Waitlist.forms import LoginForm
from Waitlist import db
from Waitlist.forms import RegistrationForm


@app.route('/')

@app.route('/index')
@login_required
def index():
    allCustomers = Customer.query.all()
    allReservations = Reservation.query.all()
    return render_template('index.html', customers = allCustomers, reservations = allReservations)


# LOGIN
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        restaurant_username = Restaurant.query.filter_by(username=form.username.data).first()
        restaurant_password = Restaurant.query.filter_by(password=form.password.data).first()
        if restaurant_username is None or not restaurant_password:
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(restaurant_username, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('restaurant/resturant_login.html', title='Sign In', form=form)
    if form.validate_on_submit():
        restaurant = Restaurant.query.filter_by(username=form.username.data).first()
        if restaurant is None or not restaurant.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)

#  LOGOUT
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


# REGISTRATION  
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        restaurant = Restaurant(username=form.username.data, company_name=form.company_name.data, password=form.password.data)
        db.session.add(restaurant)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('restaurant/resturant_register.html', title='Register', form=form)

#route for reservation

@app.route("/reservation/add", methods=["POST"])
def add_reservation():
    customer = Customer.query.get(int(request.form["customer"]))
    numberOfseats = request.form["numOfPeople"]
    dateAndTime = request.form["dateTime"]
    restaurant  = Restaurant.query.get(1)
    status = "pending"

    reservation= Reservation(dateAndTime,status,restaurant,customer)
    db.session.add(reservation)
    db.session.commit()
    return redirect("/")

@app.route("/reservation/<id>", methods=["GET"])
@login_required
def get_reservation(id):
    # customer = Reservation.query.get(int(Reservation.id))
    reservation = Reservation.query.filter_by(id=id).first_or_404
    return render_template("reservation/reservation_view.html", reservation=reservation)


@app.route("/reservation/update/<id>", methods=["GET", "POST"])
def update_reservation(id):
    reservation = Reservation.query.filter_by(id=id).first_or_404
    return render_template("reservation/reservation_view.html", reservation=reservation)

@app.route("/reservation/delete/<id>")
def delete_reservation(id):
    pass

#route for seatingTables
@app.route("/seating_tables/add")
def add_seating_tables():
    pass

@app.route("/seating_tables/<id>")
def get_seating_tables(id):
    pass

@app.route("/seating_tables/update/<id>", methods=["GET", "POST"])
def update_seating_tables(id):
    pass

@app.route("/seating_tables/delete/<id>")
def delete_seating_tables(id):
    pass


#route for customer 
@app.route("/customer/add")
def add_customer():
    pass

@app.route("/customer/update/<id>", methods=["GET", "POST"])
def update_customer(id):
    pass

@app.route("/customer/delete/<id>")
def delete_customer(id):
    pass

#route for Restaurant
@app.route("/restaurant/add", methods=["POST"])
def add_restaurant():
    pass

@app.route("/restaurant/update/<id>", methods=["GET", "POST"])
def update_restaurant(id):
    pass

@app.route("/restaurant/delete/<id>")
def delete_restaurant(id):
    pass


#route for SeatingReservations
@app.route("/Seating_reservations/add")
def add_Seating_reservations():
    pass

@app.route("/Seating_reservations/delete/<id>")
def delete_Seating_reservations(id):
    pass


