from flask import Flask
from flask import render_template
from flask import request
import os
import time
import MySQLdb
from random import randrange

app = Flask(__name__)

@app.route('/')
def index ():

	return render_template('form_p.html')

@app.route('/form_p', methods = ['GET'])
def action_form (frecuencia= None):
	frecuencia = int(request.args["frecuencia"])
	print frecuencia
	conn = MySQLdb.connect(
		host="localhost", port=3306, user="leandro",
		passwd="1234", db="datos"
	)
	cursor = conn.cursor()
	while 1:
		temp= randrange(30)
		humedad= randrange(100)
		presion= 1000 + (randrange(20))
		viento= randrange(200)
		select= ("INSERT INTO `datos`(`Id`, `temperatura`, `humedad`, `presion`, `viento`) VALUES (NULL,%s,%s,%s,%s)")
		data= (temp,humedad,presion,viento)
		cursor.execute (select,data)
		conn.commit()
		time.sleep(frecuencia)
		pass
	conn.close()

	return render_template('response2.html', frec= frecuencia)

if __name__ == "__main__":
    # Define HOST y PUERTO para accerder
    app.run(host='localhost', port=2000)



