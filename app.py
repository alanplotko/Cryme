# Flask
from flask import Flask, render_template, request, redirect, url_for, session, abort, make_response

# MongoDB and Sessions
from flask.ext.session import Session
from pymongo import MongoClient

# Miscellaneous
import os, logging, json

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__)

# MongoDB Setup
client = MongoClient(os.getenv('MONGOHQ_URL'))
db = client.core

# MongoDB Session Setup
SESSION_TYPE = "mongodb"
SESSION_MONGODB = client
SESSION_MONGODB_DB = "bc15"
SESSION_MONGODB_COLLECT = "sessions"
app.secret_key = '\xdcU\x8a\xaa\xc9\x1f\xbaVz\xbe\x06\xf9\xb9\xc5`~`\xee\xde\x92\x1b\xb4t\x80'

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

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)