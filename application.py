from flask import Flask, jsonify

import csv



Presidents = []
with open("presidents.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        Presidents.append(row)
     #   print(Presidents)


app = Flask(__name__)

# the function is filtering presidents based on the name selected
# inputs: a list of dictionarie and str
# outputs: dictionary

@app.route("/information/<lastname>")
def hello_world(lastname):
    for President in Presidents:
        if President["lastname"]== lastname:
            return jsonify(President)
    return "not found", 404

@app.route("/presido/<number>")
def presidents_zam(number):
    for row in Presidents:
        if row["number"] == number:
            return jsonify(row)
    return "not found", 404