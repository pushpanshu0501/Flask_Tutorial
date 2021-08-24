#!python3

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def root_page():
    return render_template("index.html")


@app.route('/method',methods=['GET', 'POST']) 
def fun():
    if request.method == 'POST':
        return "You have used a POST request"
    else:
        return "I reckon you are probably using GET method"

 
app.run()