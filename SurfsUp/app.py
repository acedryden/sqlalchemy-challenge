# Import the dependencies.
from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
#app = Flask(__name__)


# reflect an existing database into a new model

# reflect the tables


# Save references to each table


# Create our session (link) from Python to the DB


#################################################
# Flask Setup
#################################################




#################################################
# Flask Routes
#################################################
#@app.route("/")
#start the home page, list all the available routes  

#@app.route("/api/v1.0/precipitation")
#Convert the query results from the prec. analysis (last 12 months of data) to a dict using date as the key and prcp as the value
#return the JSON representation of your dict 

#@app.route("/api/v1.0/stations")
#Return a JSON list of the stations from the dataset

#@app.route("/api/v1.0/tobs")
#query the dates and temp of the most-active station for the previous year
#return a json list of temperature observations
#@app.route("/api/v1.0/<start>")
#return a JSON list of the min temp, avg temp and max temp for a sepecific start or start-end range. 
#for a specified start, calculate tmin, tavg & tmax for all the dates greater than or equal to the start date. 
#for a specified start and end date, calculate tmin, tavg and tmax for the dates from the start date to the end date, inclusive
#@app.route("/api/v1.0/<start>/<end>")