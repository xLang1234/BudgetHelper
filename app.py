from flask import Flask, request, redirect, session, url_for, render_template, jsonify
import requests
import json
import random
import pymongo

app = Flask(__name__)
app.config['DEBUG'] = True

myclient = pymongo.MongoClient(
    "mongodb+srv://ly:lylylyly@cluster0-kyqnj.mongodb.net/test?retryWrites=true&w=majority")

mydb = myclient["budgetplanner"]
budgetTable = mydb["budgetTable"]


@app.route("/", methods=["GET"])
@app.route("/index", methods=["GET"])
def default():
    return render_template("index.html")

@app.route("/planner", methods=["GET"])
def planner_route():
    return render_template("planner.html")

@app.route("/api/data")
def allData():
    data = budgetTable.find({}, {"_id": 0})
    return jsonify(list(data))

@app.route("/api/insertdata")
def insertData():
    data = request.args.get('data')
    data['user_id'] = 1
    query = {'user_id': 1 }
    result = budgetTable.replace_one(query, data, True)
    return result

if __name__ == '__main__':
    app.run()
    # app.run(host='0.0.0.0')
