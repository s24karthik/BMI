

# API TO CALCULATE BMI WITH WEIGHT IN KG & HEIGHT IN METERS

from flask import Flask, jsonify, request

app=Flask(__name__)

@app.route('/')
def hello():
	return "WELCOME TO BMI CALCULATION"


# POST METHOD	
@app.route("/", methods=['POST'])
def post():
	data = request.get_json()
	weight = data["weight"]
	height = data["height"]
	result = float(weight/(height*height))
	return jsonify("BMI IS:",result)
	
if __name__ == "__main__":
	app.run(port=5000,debug=True)	
