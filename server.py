import flask
from flask import Flask, request, redirect, jsonify, Response, render_template
from flask_cors import CORS
from blockchain import Blockchain

app = Flask(__name__)
CORS(app)
medical_ledger = Blockchain()

@app.route("/")
def index():
    with open("index.html") as f:
        return f.read()

@app.route("/append")
def append():
    medical_ledger.append_block(request.args["search_key"], request.args["data"])
    return medical_ledger.__str__()

@app.route("/retrieve", methods=["GET", "OPTIONS"])
def retrieve():
    search_key = request.args["search_key"]
    
    res = medical_ledger.search(search_key)

    if res != None:
        return {"uid": res}
    else:
        return {"uid": "ERROR: 404"}

if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug = False, threaded = False)
