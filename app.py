#!python3

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def root_page():
    name = ''
    if request.method=='POST' and 'username' in request.form:
        name = request.form.get('username')
    return render_template("index.html", name=name)


@app.route('/method',methods=['GET', 'POST']) 
def fun():
    if request.method == 'POST':
        return "You have used a POST request"
    else:
        return "I reckon you are probably using GET method"

 
app.run()