# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 22:24:32 2021

@author: Shabista
"""



import flask
from flask import Response,request
from flask_cors import CORS
from flask_api import status



app = flask.Flask(__name__)

CORS(app)



@app.route('/login', methods=['POST'])
def login():
    print(request.json)
    user = request.json['Username']
    pwd = request.json['password']
    resp=logins(user,pwd)
    if resp:
        msg = 'Logged in successfully !'
        return Response (response=msg, status=status.HTTP_200_OK)
    else:
         msg="Invalid Username and Password"
         return Response (response=msg, status=status.HTTP_400_BAD_REQUEST)
    


app.run()
