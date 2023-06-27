from flask import Flask
import os
import redis

REDISPORT=os.environ['REDISPORT']
REDISIP=os.environ['REDISIP']
REDISPWD=os.environ['REDISPWD']

r = redis.Redis(host=REDISIP,port=REDISPORT, password=REDISPWD)

app = Flask(__name__) #creating the Flask class object

@app.route('/',methods = ['GET']) #decorator drfines the   
def home():
    return ("<h2>hello, this is our first flask website</h2>")

@app.route('/redis-port',methods = ['GET'])
def port():
    PORT=os.environ['REDISPORT']
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
