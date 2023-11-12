from flask import Flask, request, redirect, jsonify, Response

app = Flask("app")

@app.route("/")
def index():
    return "Flask Blockchain Application"

if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug = False, threaded = False)
