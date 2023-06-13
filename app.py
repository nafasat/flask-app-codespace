from flask import Flask
import os
import redis

try:
    r = redis.Redis(host='34.131.18.147',port=6379, password='HdfcBank123')
except:
    errors.append("Unable to get URL. Please make sure it's valid and try again.")
    return {"error": errors}

app = Flask(__name__) #creating the Flask class object
@app.route('/',methods = ['GET']) #decorator drfines the   

def home():
    return "hello, this is our first flask website"; 

@app.route('/port',methods = ['GET'])
def port():
    PORT=os.environ['PORT']
    return PORT

@app.route('/redis/set/<key>/<value>',methods = ['GET'])
def set():
    r.set('foo', 'bar')
    return "Value set"

@app.route('/redis/get/<key>',methods = ['GET'])
def get():
    value = r.get('foo')
    return value

if __name__ =='__main__':  
    app.run(host='0.0.0.0', port=5000, debug = True)
