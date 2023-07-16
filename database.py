from pymongo import mongo_client
import certifi

MONGO_URI = 'localhost'
ca = certifi.where()

def dbConnection():
    try:
        client = mongo_client(MONGO_URI, tlsCAFile=ca)
        db = client["ecommerce"]
    except ConnectionError:
        print('ERROR DE CONEXION CON LA BASE DE DATOS')
    return db