# string = "DCCC-MEZ F/W Ver 0.689g\n\r"
 
# #emp_str = ""
# #for m in new_string:
#    # if m.isdigit():
#    #     emp_str = emp_str + m
# #print("Find numbers from string:",(emp_str)) 
# import re
# #s = "Sound Level: -11.7 db or 15.2 or 8 db"
# result = re.findall(r"[-+]?\d*\.\d+|\d+", string)
# #res = list(map(float, result))
# #a=str(res)
# print(' '.join(map(str, result)))

# from flask import Flask, jsonify
# app = Flask(__name__)

# data = [{"DCR": "50"}]

# @app.route('/4950/dcr', methods=['GET'])
# def get():
#     return jsonify({'4950': data})

# @app.route('/4950/dcr/<int:put_data>', methods=['PUT'])
# def put(put_data):
#     data[0]['DCR'] = str(put_data)
#     return jsonify({'4950': data})

# if __name__ == "__main__":
#     app.run(debug=True)

# import requests
# import json
# url = 'http://127.0.0.1:5000/4950/dcr/10'
# payload = {'some': 'data'}

# Create your header as required
# headers = {"content-type": "application/json", "Authorization": "<auth-key>" }

# r = requests.put(url, data=json.dumps(payload), headers=headers)

# from flask import Flask, jsonify, request

# app = Flask(__name__)

# data = [{"id": 1, "name": "John", "age": 30},
#         {"id": 2, "name": "Jane", "age": 25}]

# @app.route('/users', methods=['GET'])
# def get_users():
#     return jsonify({'users': data})

# @app.route('/users/<int:user_id>', methods=['PUT'])
# def update_user(user_id):
#     user = next((user for user in data if user["id"] == user_id), None)
#     if user:
#         user.update(request.json)
#         return jsonify({'user': user})
#     else:
#         return jsonify({'message': 'User not found'})

# if __name__ == "__main__":
#     app.run(debug=True)


import time
import re
import serial
from time import sleep
ser = serial.Serial("/dev/ttyACM0", 9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=1)       
ser.write(str.encode('VERSION\r\n'))
received_data = ser.read()              #read serial port
sleep(0.03)
data_left = ser.inWaiting()             #check for remaining byte
received_data += ser.read(data_left)
print (received_data)                   #print received data
# result = re.findall(r"[-+]?\d*\.\d+|\d+[g]$", received_data.decode("utf-8"))
# print(' '.join(map(str, result)))
sl_data = slice(17,25)
result = received_data[sl_data]
a = result.strip() 
print(a)
