from flask import Flask
from flask import render_template
from flask import request
import os
import time
import MySQLdb
import simplejson

app = Flask(__name__)

@app.route('/')
def index ():

	return render_template('form.html')

@app.route('/form_c', methods = ['GET'])
def action_form (frecuencia= None):
	x=0
	frecuencia = int(request.args["frecuencia"])
	print frecuencia
	conn = MySQLdb.connect(
		host="localhost", port=3306, user="leandro",
		passwd="1234", db="datos"	
		    )
	cursor = conn.cursor()
	select= "SELECT temperatura FROM datos;"
	cursor.execute(select)
	registro_temp= cursor.fetchall()
	select= "SELECT presion FROM datos;"
	cursor.execute(select)
	registro_presion= cursor.fetchall()
	select= "SELECT humedad FROM datos;"
	cursor.execute(select)
	registro_humedad= cursor.fetchall()
	select= "SELECT viento FROM datos;"
	cursor.execute(select)
	registro_viento= cursor.fetchall()
	cursor.close()
	conn.close()
	return render_template('response.html', frec= frecuencia ,r_temp=simplejson.dumps(registro_temp), r_humedad= simplejson.dumps(registro_humedad), r_presion=simplejson.dumps(registro_presion), r_viento=simplejson.dumps(registro_viento))

if __name__ == "__main__":
    # Define HOST y PUERTO para accerder
    app.run(host='localhost', port=4000)