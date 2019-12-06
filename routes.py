
from flask import Flask



# @app.route('/')
def index():
    return render_template('index.html')

#route for reservation\

@app.route("/reservation/add")
def add_reservation():
    pass

@app.route("/reservation/<id>")
def get_reservation(id):
    pass

@app.route("/reservation/update/<id>", methods=["GET", "POST"])
def update_reservation(id):
    pass

@app.route("/reservation/delete/<id>")
def delete_reservation(id):
    pass

#route for seatingTables
@app.route("/seating_tables/add")
def add_reservation():
    pass

@app.route("/seating_tables/<id>")
def get_reservation(id):
    pass

@app.route("/seating_tables/update/<id>", methods=["GET", "POST"])
def update_reservation(id):
    pass

@app.route("/seating_tables/delete/<id>")
def delete_reservation(id):
    pass


#route for customer 
@app.route("/customer/add")
def add_reservation():
    pass

@app.route("/customer/update/<id>", methods=["GET", "POST"])
def update_reservation(id):
    pass

@app.route("/customer/delete/<id>")
def delete_reservation(id):
    pass

#route for Restaurant
@app.route("/restaurant/add")
def add_reservation():
    pass

@app.route("/restaurant/update/<id>", methods=["GET", "POST"])
def update_reservation(id):
    pass

@app.route("/restaurant/delete/<id>")
def delete_reservation(id):
    pass


#route for SeatingReservations
@app.route("/Seating_reservations/add")
def add_reservation():
    pass

@app.route("/Seating_reservations/delete/<id>")
def delete_reservation(id):
    pass


