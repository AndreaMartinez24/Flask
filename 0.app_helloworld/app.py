"""
Ejercicio 1: Crea una aplicación web básica con Flask que,
al ser ejecutada, inica un servidor local en el puerto 5000.
cuando visita la ruta principal (http://localhost:500/),
el servidor responderá con un mensaje HTML que dice "Hello, World Flask".
"""
#Se importa el módulo Flask desde el paquete flask
from flask import Flask

#Crea un ainstancia de la clase Flask.
#El argumento __name__ le dice a flask, que utilice el nombre del archivo actual main.py
app = Flask(__name__)

#Este es un decorador que define una ruta
#corresponde a la página principal del app
@app.route('/')

#Cuando alguien visite app(por ejemplo, http://localhost:5000/),
#la funcion hello() será ejecutada
def hello():
    return "<h1> Hello, World Flask !</h1>"

#Solo se ejecute si el archivo es ejecutado directamente
#arranca la aplicación Flask en modo de depuración (debug=true)
if __name__ == "__main__":
    app.run(debug=True, port=5000)