# Flask
from flask import Flask, render_template, request, redirect, url_for, session, abort, make_response

# MongoDB and Sessions
from flask.ext.session import Session
from pymongo import MongoClient

#ML Libs
import numpy as np
from sklearn.svm import LinearSVC
from sklearn.externals import joblib

# Miscellaneous
import os, logging, json

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__)

# MongoDB Setup
client = MongoClient(os.getenv('MONGOHQ_URL'))
db = client.bc15

# MongoDB Session Setup
SESSION_TYPE = "mongodb"
SESSION_MONGODB = client
SESSION_MONGODB_DB = "bc15"
SESSION_MONGODB_COLLECT = "sessions"
app.secret_key = '\xcbC\xb0\x0b\xe6\xe7\xc2\xd3u\xbf\xff\x9b\xfb\xb8\xb1\xb9^Y\xdbQ\xba\x7f\xabl'

app.config.from_object(__name__)
Session(app)

@app.before_first_request
def setup_logging():
	if not app.debug:
		# In production mode, add log handler to sys.stderr.
		app.logger.addHandler(logging.StreamHandler())
		app.logger.setLevel(logging.INFO)

@app.route('/')
def index():
	return render_template('index.html', template_folder=tmpl_dir)

@app.route('/dashboard')
def dashboard():
	return render_template('dashboard.html', template_folder=tmpl_dir)

@app.route('/predict', methods=["POST"])
def predict():
    svm = get_predictor()
    if svm != None:
        svm.predict(np.array([[request.form["time"], request.form["lat"], request.form["lon"]]]))
    return render_template('index.html', template_folder=tmpl_dir)

@app.errorhandler(401)
def unauthorized(error):
    return render_template('error.html', template_folder=tmpl_dir, error=401, error_msg="Unauthorized", 
		return_home="You must be logged in to access this page!"	
	)

@app.errorhandler(500)
def internal_server(e):
	return render_template('error.html', template_folder=tmpl_dir, error=500, error_msg="Internal Server Error", 
		return_home="Something went wrong! Let us know if it happens again!"	
	)

@app.errorhandler(404)
def page_not_found(e):
	return render_template('error.html', template_folder=tmpl_dir, error=404, error_msg="Page Not Found",
		return_home="We can't find what you're looking for."
	)

def get_predictor():
    try:
        svm = joblib.load("data/svm.pkl")
    except:
        crime_data = np.loadtxt(open("data/crimeData.csv", "rb"), delimiter=",", skiprows=1)
        crime_target = np.loadtxt(open("data/crimeLabels.csv", "rb"), delimiter=",", dtype=str)
        svm = LinearSVC().fit(crime_data, crime_target)
        joblib.dump(svm, "data/svm.pkl")
    finally:
        return svm

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)
