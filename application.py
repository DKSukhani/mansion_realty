import os

from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("mansionreality").sheet1

app = Flask(__name__)


# engine = create_engine(
#     "postgresql://dipesh:dipesh123@db1:543/flights")
# xyz = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def landing_page():
    return render_template("landing_page.html")

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/form_result", methods=["POST", "GET"])
def form_result():
    if request.method == "POST":
        fname = request.form.get("firstname")
        lname = request.form.get("lastname")
        insertRow = [fname, lname]
        sheet.append_row(insertRow)

    data = sheet.get_all_records()  # Get a list of all records
    return render_template("form_result.html", data=data)    


# @app.route("/book", methods=["POST"])
# def book():
#     """Book a flight."""

#     # Get form information.
#     name = request.form.get("name")
#     try:
#         flight_id = int(request.form.get("flight_id"))
#     except ValueError:
#         return render_template("error.html", message="Invalid flight number.")

#     # Make sure flight exists.
#     if xyz.execute("SELECT * FROM flights WHERE id = :id", {"id": flight_id}).rowcount == 0:
#         return render_template("error.html", message="No such flight with that id.")
#     xyz.execute("INSERT INTO passengers (name, flight_id) VALUES (:name, :flight_id)",
#             {"name": name, "flight_id": flight_id})
#     xyz.commit()
#     return render_template("success.html")

# @app.route("/flights")
# def flights():
#     """Lists all flights."""
#     flights = xyz.execute("SELECT * FROM flights").fetchall()
#     return render_template("flights.html", flights=flights)

# @app.route("/flights/<int:flight_id>")
# def flight(flight_id):
#     """Lists details about a single flight."""

#     # Make sure flight exists.
#     flight = xyz.execute("SELECT * FROM flights WHERE id = :id", {"id": flight_id}).fetchone()
#     if flight is None:
#         return render_template("error.html", message="No such flight.")

#     # Get all passengers.
#     passengers = xyz.execute("SELECT name FROM passengers WHERE flight_id = :flight_id",
#                             {"flight_id": flight_id}).fetchall()
#     return render_template("flight.html", flight=flight, passengers=passengers)



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port, debug=True)



