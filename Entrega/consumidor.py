from flask import Flask
from flask import render_template
from flask import request
import os
import time
import MySQLdb
import simplejson

app = Flask(__name__)

contador=1
indice=0
m_temp = range(10)
m_humedad = range(10)
m_presion = range(10)
m_viento= range(10)

@app.route('/')
def index ():
	return render_template('form_c.html')

@app.route('/form_c', methods = ['GET'])
def action_form (frecuencia= None):
	conn = MySQLdb.connect(
	host="localhost", port=3306, user="leandro",
	passwd="1234", db="datos"	
	    )
	cursor = conn.cursor()
	frecuencia = int(request.args["frecuencia"])
	
	global contador
	global indice 

	select= "SELECT temperatura, id FROM datos ORDER BY id DESC;"
	cursor.execute(select)
	registro_temp= cursor.fetchone()
	print registro_temp
	select= "SELECT presion, id FROM datos ORDER BY id DESC;"
	cursor.execute(select)
	registro_presion= cursor.fetchone()
	select= "SELECT humedad, id FROM datos ORDER BY id DESC;"
	cursor.execute(select)
	registro_humedad= cursor.fetchone()
	select= "SELECT viento, id FROM datos ORDER BY id DESC;"
	cursor.execute(select)
	registro_viento= cursor.fetchone()

	global m_temp
	global m_humedad
	global m_viento
	global m_presion

	m_temp[indice]= registro_temp[0]
	m_viento[indice]= registro_viento[0]
	m_humedad[indice]= registro_humedad[0]
	m_presion[indice]= registro_presion[0]

	prom_temp= promedio(m_temp, contador)
	prom_viento= promedio(m_viento, contador)
	prom_humedad= promedio(m_humedad, contador)
	prom_presion= promedio(m_presion, contador)

	contador=contador + 1
	indice = (indice + 1) % 10



	cursor.close()
	conn.close()

	return render_template('response.html',cont=contador , frec= frecuencia ,temp=simplejson.dumps(registro_temp[0]), humedad= simplejson.dumps(registro_humedad[0]), presion=simplejson.dumps(registro_presion[0]), viento=simplejson.dumps(registro_viento[0]), prom_presion=simplejson.dumps(prom_presion), prom_humedad=simplejson.dumps(prom_humedad), prom_viento=simplejson.dumps(prom_viento), prom_temp=simplejson.dumps(prom_temp))


def promedio(v,x): 
	i=0
	prom=0
	if (x > 10):
		for i in v:
			prom= prom + i
		prom= prom / 10
	else:
		for i in range(x):
			prom= prom + int(v[i])
		prom= prom / x
	return prom	

if __name__ == "__main__":
    # Define HOST y PUERTO para accerder
    app.run(host='localhost', port=4000)