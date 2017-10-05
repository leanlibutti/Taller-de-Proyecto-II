from flask import Flask
from flask import render_template
from flask import request
import os
import time

app = Flask(__name__)

@app.route('/')
def index ():
	return render_template('form.html')

@app.route('/form', methods = ['GET'])
def action_form (frecuencia= None):

	frecuencia = int(request.args["frecuencia"])
	
	return render_template('response.html',frec= frecuencia)

if __name__ == "__main__":
    # Define HOST y PUERTO para accerder
    app.run(host='localhost', port=4000)