import os
import get_users
from flask import Flask, render_template, request, redirect
import pymongo
from pymongo import MongoClient

MONGO_URL = os.environ.get('MONGOHQ_URL')
client = MongoClient(MONGO_URL)

# Initialize the database
db = client.app56172051
iwh_collection = db.iwh_users
maga_collection = db.maga_users

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
	users = maga_collection.find()
	return render_template('index.html', users=users)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)