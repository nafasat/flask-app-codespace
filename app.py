from flask import Flask
import os

app = Flask(__name__) #creating the Flask class object
@app.route('/',methods = ['GET']) #decorator drfines the   

def home():
    return "hello, this is our first flask website"; 

@app.route('/port',methods = ['GET'])
def port():
    PORT=os.environ['PORT']
    return PORT


if __name__ =='__main__':  
    app.run(host='0.0.0.0', port=5000, debug = True)
