from flask import Flask, request, redirect, jsonify, Response
from blockchain import Blockchain

app = Flask("app")
medical_ledger = Blockchain()

@app.route("/")
def index():
    return "Flask Blockchain Application"

@app.route("/append")
def append():
    if len(request.args) != 1:
        return "FALSE"

    medical_ledger.append_block(request.args["data"])
    return "TRUE"

if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug = False, threaded = False)
