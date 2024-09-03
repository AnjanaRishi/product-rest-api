from flask import Flask,jsonify,request
import json
import os
from routes import register_routes

app=Flask(__name__)

register_routes(app)

if __name__ == '__main__':
    port=int(os.environ.get('PORT',5005))
    app.run(debug=False,host='0.0.0.0',port=port) 


