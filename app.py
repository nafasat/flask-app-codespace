from flask import Flask
import os
import redis

r = redis.Redis(host='34.131.18.147',port=6379, password='HdfcBank123')

app = Flask(__name__) #creating the Flask class object
@app.route('/',methods = ['GET']) #decorator drfines the   

def home():
    return "hello, this is our first flask website"; 

@app.route('/port',methods = ['GET'])
def port():
    PORT=os.environ['PORT']
    return PORT

@app.get('/home/<menu>')
def single_converter(menu):
    return "You tried accessing 'single_converter' \
    endpoint with value of 'menu' as " + str(menu)

@app.get('/redis/set/<key>/<val>')
def multiple_converter(key,val):
    r.set(key, val)
    return "Key "+str(key)+" with its value "+str(val)+" is set"

@app.get('/redis/get/<key>')
def single_converte(key):
    value = r.get(key).decode("utf-8")
    return "Value of key "+str(key)+" is "+str(value)

if __name__ =='__main__':  
    app.run(host='0.0.0.0', port=5000, debug = True)
