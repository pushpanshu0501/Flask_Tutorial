#!python3

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'This is my first app! Heheh!'


@app.route('/method',methods=['GET', 'POST']) 
def fun():
    if request.method == 'POST':
        return "You have used a POST request"
    else:
        return "I reckon you are probably using GET method"

 
app.run()