# Import the dependencies.
from flask import Flask, jsonify
import datetime as dt
import numpy as np 
import pandas as pd 
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Meas = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
#################################################
# Flask Routes
#################################################
@app.route("/")
def main():
    
    return """
    Welcome to my Hawaii Weather App! Please navigate to the correct page:<br>
    /api/v1.0/precipitation - See Query Results of the last 12 months of Precipitation Data<br>
    /api/v1.0/stations - See a list of the Weather Stations<br>
    /api/v1.0/tobs - Displays the dates and temperatures of the most active weather station<br>
    /api/v1.0/<start> Find the min temp, avg temp & temp temp for a specific start date<br>
    /api/v1.0/<start>/<end> Find the min temp, avg temp & temp temp for a specific start & enddate<br>
    """
if __name__ == '__main__':
    app.run()


@app.route("/api/v1.0/precipitation")
def precipitation(): 
    session = Session(engine)
    stations = session.query(Meas.prcp, Meas.date).all()
    session.close()

    output_prcp = []
    for record in stations:
        output_prcp.append(record[0])  
    return jsonify(output_prcp)

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    stations = session.query(Station.station).all()
    session.close()

    output_stations = []
    for record in stations:
        output_stations.append(record[0])  
    return jsonify(output_stations)

@app.route("/api/v1.0/tobs")
def tobs(): 
    session = Session(engine)
    tobs = session.query(Meas.station,  Meas.tobs, Meas.date).filter(Meas.station == 'USC00519281').all()
    session.close()

    output_tobs = []
    for record in tobs: 
        output_tobs.append(record[0])
    return jsonify(output_tobs)

@app.route("/api/v1.0/<start>")
def startdate():
    session = Session(engine)
    startdate = session.query(Meas.station, Meas.tobs, Meas.date).all()
    session.close()

    output_min = []
    for record in tobs.min(): 
        output_min.append(record[0])
    return jsonify(output_min)
    
    output_max = []
    for record in tobs.max(): 
        output_min.append(record[0])
    return jsonify(output_min)

    output_avg = []
    for record in tobs.avg():
        output_avg.append(record[0])
    return jsonify(output_avg)
