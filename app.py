import datetime as dt
import numpy as np
import pandas as pd
# Import SQLAlchemy to access SQLite database
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
# Flask Dependency
from flask import Flask, jsonify
# Set up the database
# create_engine() function allows us to access and query our SQLite database file
engine = create_engine("sqlite:///hawaii.sqlite")
# Reflect the database into classes
Base = automap_base()
Base.prepare(engine, reflect=True)
# Create a variable for each of the classes so that we can reference them later
Measurement = Base.classes.measurement
Station = Base.classes.station
# Create session link from Python to our database
session = Session(engine)
app = Flask(__name__)
# Welcome Route
@app.route("/")
# For this we'll create a function, and our return statement will have f-strings as a reference to all of the other routes. 
# This will ensure our investors know where to go to view the results of our data.
# add the precipitation, stations, tobs, and temp routes that we'll need
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

# Precipitation route
@app.route("/api/v1.0/precipitation")
# calculates the date one year ago from the most recent date in the database
# query to get the date and precipitation for the previous year
# Jsonify() is a function that converts the dictionary to a JSON file.
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)

# Stations route
@app.route("/api/v1.0/stations")
#We want to start by unraveling our results into a one-dimensional array. 
# To do this, we want to use the function np.ravel(), with results as our parameter.
# Next, we will convert our unraveled results into a list. 
# To convert the results to a list, we will need to use the list function, which is list(), 
# and then convert that array into a list. Then we'll jsonify the list and return it as JSON
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

# Monthly Temp Route
@app.route("/api/v1.0/tobs")
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

# Statistics route
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)] # creates list called sel

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)