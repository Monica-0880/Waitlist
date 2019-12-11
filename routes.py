from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, login_required, logout_user
from Waitlist.models import Restaurant, Customer, Reservation, Seating_table
from Waitlist import app
from Waitlist.forms import LoginForm
from Waitlist import db
from Waitlist.forms import RegistrationForm


@app.route('/')

@app.route('/index')
@login_required
def index():
    allSeatingTables = Seating_table.query.filter(Customer.restaurant_id == current_user.id).all()
    allCustomers = Customer.query.filter(Customer.restaurant_id == current_user.id).all()
    allReservations = Reservation.query.filter(Reservation.restaurant_id == current_user.id).all()
    return render_template('index.html', customers = allCustomers, reservations = allReservations, seatingTables = allSeatingTables)


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
    restaurant  = Restaurant.query.get(current_user.id)
    status = "pending"

    reservation= Reservation(dateAndTime,status,restaurant,customer)
    db.session.add(reservation)
    db.session.commit()
    return redirect("/index")

@app.route("/reservation/<id>", methods=["GET"])
@login_required
def get_reservation(id):
    thisReservation = Reservation.query.get(id)
    return render_template("reservation/reservation_view.html", reservation = thisReservation)


@app.route("/reservation/update/<id>", methods=["GET", "POST"])
@login_required
def update_reservation(id):
    
    thisReservationAllCustomers = Customer.query.filter(Customer.restaurant_id == current_user.id).all()
    thisReservation = Reservation.query.get(id)
    return render_template("reservation/reservation_update.html", reservation = thisReservation, customers = thisReservationAllCustomers)
    
    # customer = Customer.query.get(int(request.form["customer"]))
    # numberOfseats = request.form["numOfPeople"]
    # newdateAndTime = request.form.get["dateime"]
    # olddateAndTime = Reservation.query.filter_by(id=id)

    # dateAndTime.update({olddateAndTime.reservation_time: newdateAndTime})

    # olddateAndTime.reservation_time = newdateAndTime
    # db.session.commit()
    # return redirect('/index')

@app.route("/reservation/delete/<id>", methods=["POST"])
@login_required
def delete_reservation(id):
    thisReservation = Reservation.query.get(id)
    db.session.delete(thisReservation)
    db.session.commit()
    return redirect('/')

#route for seatingTables
@app.route("/seating_tables/add", methods=['POST'])
def add_seating_tables():
    table_number = request.form["tablenum"]
    table_seats = request.form["seatsnum"]
    restaurant  = Restaurant.query.get(current_user.id)

    seating = Seating_table(table_number,table_seats,restaurant)
    db.session.add(seating)
    db.session.commit()
    return redirect("/index")

@app.route("/seating_tables/<id>")
def get_seating_tables(id):
    allSeatingTable = Seating_table.query.get(id)
    return render_template('/seating_table/seatingtables_view.html', seatingtable = allSeatingTable)


@app.route("/seating_tables/update/<id>", methods=["GET", "POST"])
def update_seating_tables(id):
    pass

@app.route("/seating_tables/delete/<id>")
def delete_seating_tables(id):
    thisSeatingTable = Seating_table.query.get(id)
    db.session.delete(thisSeatingTable)
    db.session.commit()
    return redirect('/')


#route for customer 
@app.route("/customer/add", methods=["POST"])
@login_required
def add_customer():
    customer_name = request.form["custName"]
    customer_phone = int(request.form["custTel"])
    customer_email = request.form["custEmail"]
    restaurant  = Restaurant.query.get(current_user.id)

    customer = Customer(customer_name,customer_phone,customer_email,restaurant)
    db.session.add(customer)
    db.session.commit()
    return redirect("/index")

@app.route("/customer/update/<id>", methods=["GET", "POST"])
def update_customer(id):
    thisCustomer = Customer.query.get(id)

    if request.method == "GET":
        return render_template('customer/customer_edit.html', customer = thisCustomer)
        # {{ url_for('update_customer', id=reservation.customer_id )}}
    
    if request.method == "POST":
        name = request.form.get("custName")
        phone_number = request.form.get("custTel")
        email = request.form.get("custEmail")

        if name != "":
            thisCustomer.name = name
        if phone_number != "":
            thisCustomer.phone_number = phone_number
        if email != "":
            thisCustomer.email = email

        db.session.commit()
        return redirect("/index")
    



@app.route("/customer/delete/<id>")
def delete_customer(id):
    thisCustomer = Customer.query.get(id)
    db.session.delete(thisCustomer)
    db.session.commit()
    return redirect('/')

#route for Restaurant
# @app.route("/restaurant/add", methods=["POST"])
# def add_restaurant():
#     pass

# @app.route("/restaurant/update/<id>", methods=["GET", "POST"])
# def update_restaurant(id):
#     pass

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


