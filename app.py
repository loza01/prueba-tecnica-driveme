from flask import Flask, request, jsonify
import requests
import pymysql
from datetime import datetime
from flask_cors import CORS
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

app = Flask(__name__)
CORS(app)


# Función para conectarse a la base de datos
def connect_db():
	#Conectate a la DB!
	return


@app.route('/guardar-clima', methods=['POST'])
def guardar_clima():
	# Obtener lat y lon de los datos enviados en la petición
	lat = request.form.get('lat')
	lon = request.form.get('lon')
	fecha = datetime.now().strftime('%Y-%m-%d')  # Fecha actual para el ejemplo
	# Realizar la petición a la API de clima
	api_key = config['default']['api-key']
	url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric&lang=es"
	
	#Realizamos petición, guardamos datos, y devolvemos json







	return jsonify({"success": True, "message": "Datos del clima guardados correctamente.", "fecha": fecha, "temperatura" : 0, "humedad" : 0, "viento" : 0, "descripcion" : 0, "url" : url})

if __name__ == '__main__':
	app.run(debug=True)
