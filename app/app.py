import json
import figuras_random
import dibuja
from flask import Flask, json, render_template, Response

app = Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
def home():
    return render_template('index.html')

@app.route('/figuras', methods=('GET', 'POST'))
def fig():
    datos={
        "figuras": [
            {
                "nombre": "cuadrado",
                "lados": 4
            },
            {
                "nombre": "triangulo",
                "lados": 3
            },
            {
                "nombre": "circulo",
                "lados": 0
            }
        ]
    }
    datos['figuras'].append({
        "nombre": "pentagono",
        "lados": 5
    })
    return json.dumps(datos)
    
@app.route('/figuras_random', methods=('GET', 'POST'))
def fr():
    return figuras_random.figuras_random()

@app.route('/dibuja', methods=('GET', 'POST'))
def db():
    r = Response(response=dibuja.dibuja(), status=200, mimetype="image/png")
    r.headers["Content-Type"] = "image/png"
    return r

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
