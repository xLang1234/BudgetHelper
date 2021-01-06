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
spending = mydb["spending"]


@app.route("/", methods=["GET"])
@app.route("/index", methods=["GET"])
def default():
    return render_template("index.html")

@app.route("/planner", methods=["GET"])
def planner_route():
    return render_template("planner.html")

@app.route("/faq", methods=["GET"])
def faq_route():
    return render_template("faq.html")

@app.route("/api/data")
def allData():
    data = budgetTable.find({}, {"_id": 0})
    return jsonify(list(data))

@app.route("/api/insertdata")
def insertData():
    query = {'user_id': request.args.get('user_id'), 'name' : request.args.get('name') }
    update = {
        'user_id' : request.args.get('user_id'),
        'name' : request.args.get('name'),
        'amount' : request.args.get('amount'),
    }
    result = budgetTable.replace_one(query, update, True)
    return str(result.acknowledged)

@app.route("/api/insertspending")
def insertSpendingData():
    query = {'user_id': request.args.get('user_id'), 'name' : request.args.get('name') }
    update = {
        'user_id' : request.args.get('user_id'),
        'name' : request.args.get('name'),
        'amount' : request.args.get('amount')
    }
    result = budgetTable.insert_one(query, update)
    return str(result.acknowledged)

if __name__ == '__main__':
    app.run()
    # app.run(host='0.0.0.0')
