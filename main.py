from flask import Flask,jsonify,request
from data import data
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route("/")
def index():
    response = jsonify({
        "data":data,
        "message":"success"
    }),200
    return(response)
@app.route("/planet")
def planet():
    name = request.args.get("name")
    planet_data = next(item for item in data if item['name']==name)
    return jsonify({
        "data":planet_data,
        "message" : "success"
    }),200

if __name__ == "__main__":
    app.run()