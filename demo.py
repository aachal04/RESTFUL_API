from flask import Flask,jsonify
app = Flask(__name__)
data = [{"DCR":"50"}]
@app.route('/4950/dcr', methods = ['GET'])
def get():
    return jsonify({'4950':data})
@app.route('/4950/dcr/<int:put_data>', methods=['PUT'])
def put(put_data):
    # data [put_data]['DCR'] = "25"
    # return jsonify({'4950':data[put_data]})
    data[0]['DCR'] = str(put_data)
    return jsonify({'4950': data})
if __name__ == "__main__":
    app.run(debug=True)
