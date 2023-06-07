import time
import re
import serial
import requests 
import flask
from time import sleep
from flask import Flask,jsonify, request

app = Flask(__name__)

get_data = [{"version":""}]
@app.route('/4950/version', methods = ['GET'])
def get():
    ser = serial.Serial("/dev/ttyACM0", 9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=1)    
    a = 'VERSION\r\n'   
    ser.write(str.encode(a))
    received_data = ser.read()              #read serial port
    sleep(0.03)
    data_left = ser.inWaiting()             #check for remaining byte
    received_data += ser.read(data_left)
    print (received_data)                   #print received data
    result = re.findall(r"[-+]?\d*\.\d+|\d+", received_data.decode("utf-8"))
    print(' '.join(map(str, result)))
    # sl_data = slice(17,25)
    # result = received_data[sl_data]
    # res = result.strip() 
    # print(res)

    
    # data [put_data]['DCR'] = "25"
    # return jsonify({'4950':data[put_data]})
    get_data[0]['version'] = str(res)
    return jsonify({'4950':get_data})

data = [{"DCR":"50"}]
@app.route('/4950/dcr/<string:put_data>', methods=['PUT'])
def put(put_data):
    ser = serial.Serial("/dev/ttyACM0", 9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=1)    
    a = 'R'+ str(put_data)+'\r\n'   
    ser.write(str.encode(a))
    received_data = ser.read()              #read serial port
    sleep(0.03)
    data_left = ser.inWaiting()             #check for remaining byte
    received_data += ser.read(data_left)
    print (received_data)                   #print received data
    result = re.findall(r"[-+]?\d*\.\d+|\d+", received_data.decode("utf-8"))
    print(' '.join(map(str, result)))
    # data [put_data]['DCR'] = "25"
    # return jsonify({'4950':data[put_data]})
    data[0]['DCR'] = result
    return jsonify({'4950': data})

@app.route('/4950/data', methods=['POST'])
def post():
    new_data = {'DCR': request.json['DCR']}
    data.append(new_data)



if __name__ == "__main__":
    app.run(debug=True)