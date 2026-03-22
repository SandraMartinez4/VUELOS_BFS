from flask import Flask, render_template, request
from bfs_vuelos import buscar_ruta

app = Flask(__name__)

conexiones = {
    'Jiloyork': {'Celaya', 'CDMX', 'Queretaro'},
    'Sonora': {'Zacatecas', 'Sinaloa'},
    'Guanajuato': {'Aguascalientes'},
    'Oaxaca': {'Queretaro'},
    'Sinaloa': {'Celaya', 'Sonora', 'Jiloyork'},
    'Celaya': {'Jiloyork', 'Sinaloa'},
    'Zacatecas': {'Sonora', 'Monterrey', 'Queretaro'},
    'Monterrey': {'Zacatecas', 'Sinaloa'},
    'Tamaulipas': {'Queretaro'},
    'Queretaro': {'Tamaulipas', 'Zacatecas', 'Sinaloa', 'Jiloyork', 'Oaxaca'}
}

@app.route("/", methods=["GET", "POST"])
def index():
    ruta = None
    ciudades = list(conexiones.keys())

    if request.method == "POST":
        origen = request.form["origen"]
        destino = request.form["destino"]
        ruta = buscar_ruta(conexiones, origen, destino)

    return render_template("index.html", ciudades=ciudades, ruta=ruta)




import os

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))