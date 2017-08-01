"""Cloud Foundry test"""
from flask import Flask
import os

app = Flask(__name__)

port = int(os.getenv("PORT"))

@app.route('/')
def hello_world():
    samplefile = open("samplefile.txt","w")
    return 'Hello World! I am running on port '+ str(port) + "\n"

@app.route('/dir1')
def getCurrentDir1():
    while(1):
        pass
    return os.getcwd()
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
    while(1):
        pass
