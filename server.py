from flask import Flask, request, redirect, jsonify, Response
from blockchain import Blockchain

app = Flask("app")
medical_ledger = Blockchain()

@app.route("/")
def index():
    return "Flask Blockchain Application"

@app.route("/append")
def append():
    medical_ledger.append_block(request.args["search_key"], request.args["data"])
    return medical_ledger.__str__()

@app.route("/retrieve")
def retrieve():
    search_key = request.args["search_key"]
    
    res = medical_ledger.search(search_key)

    if res != None:
        return flask.Response(res, status = 200)
    else:
        return flask.Response("ERROR: search key not found!!!", status = 400)

if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug = False, threaded = False)
