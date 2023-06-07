from flask import Flask,jsonify,request

app = Flask(__name__)
capital_city = [{"Nepal": "Kathmandu", "Italy": "Rome", "England": "London"}]
@app.route('/')
def index():
    return "Hello World"
@app.route('/capital_city', methods = ['GET'])
def get():
    return jsonify({'City':capital_city})

# @app.route('/capital_city', methods=['POST'])
# def post():
#     landmark = {"Nepal":"Monkey Temple","Italy":"Coloseum","England":"Buckingham Palace"}
#     capital_city.append(landmark)
#     return jsonify({'landmark':landmark})

@app.route('/capital_city/<int:city>',methods=['PUT'])
def put(city):
    capital_city[city]['Nepal'] = "XYZ"
    return jsonify({'City':capital_city[city]})  

@app.route('/4950/data', methods=['POST'])
def post():
    new_data = {'DCR': request.json['DCR']}
    capital_city.append(new_data) 

@app.route('/capital_city/<int:city>',methods=['DELETE'])
def remove(city):
    capital_city.remove(capital_city[city])
    return jsonify({'result':True})

if __name__ == "__main__":
    app.run(debug=True)
