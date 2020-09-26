from flask import Flask, render_template, request, redirect, url_for
import os
import json

app = Flask(__name__)
database = {}
with open('customers.json') as fp:
        database = json.load(fp)

@app.route('/')
def home():
    return render_template('home.template.html')  
#special function from flask

@app.route('/customers')
def show_customers():
    return render_template('customers.template.html', all_customers=database)  
#special function from flask


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),    #host
            port=int(os.environ.get('PORT')),    
            debug=True)
