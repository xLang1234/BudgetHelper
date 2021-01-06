from flask import Flask, request, redirect, session, url_for, render_template, jsonify
import requests
import json
import random

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=["GET"])
@app.route("/index", methods=["GET"])
def default():
    return render_template("index.html")

@app.route("/planner", methods=["GET"])
def default():
    return render_template("planner.html")

if __name__ == '__main__':
    app.run()
    # app.run(host='0.0.0.0')
