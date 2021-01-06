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
    query = {'user_id': request.args.get('user_id') }
    data = budgetTable.find(query, {"_id": 0})
    return jsonify(list(data))

@app.route("/api/spendingdata")
def allSpendingData():
    query = {'user_id': request.args.get('user_id') }
    data = spending.find(query, {"_id": 0})
    return jsonify(list(data))

@app.route("/api/formatteddata")
def allFormattedData():
    query = {'user_id': request.args.get('user_id') }
    budget = budgetTable.find(query, {"_id": 0})
    spendingData = spending.find(query, {"_id": 0})
    spendingResult = {}
    budgetResult = []
    leftResult = {}
    for c in budget:
        spendingResult[c.get('name')] = 0
        leftResult[c.get('name')] = float(c.get('amount'))
        budgetResult.append(c)
    for b in spendingData:
        if(spendingResult.get(b.get('name')) == None):
            spendingResult[b.get('name')] = 0
        spendingResult[b.get('name')] += float(b.get('amount'))
    
    for c in spendingResult:
        leftResult[c] -= spendingResult[c]
    result = {
        'budget' : budgetResult,
        'spending' : spendingResult,
        'left': leftResult
    }


    print(result)
    return jsonify(result)

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
    # query = {'user_id': request.args.get('user_id'), 'name' : request.args.get('name') }
    update = {
        'user_id' : request.args.get('user_id'),
        'name' : request.args.get('name'),
        'amount' : request.args.get('amount')
    }
    result = spending.insert_one(update)
    return str(result.acknowledged)

if __name__ == '__main__':
    app.run()
    # app.run(host='0.0.0.0')
