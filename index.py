from flask import Flask, render_template
#creamos nuestra aplicación
app = Flask(__name__)
#agregamos la ruta de la raíz utilizando un decorador
@app.route('/')
def home():
    return render_template("home.htm")

# agregamos funciones que manejarán cada página de nuestra aplicación, decoradas con la ruta correspondiente
@app.route('/about')
def about():
    return render_template("about.htm")

#el siguiente comando permite que el servidor esté siempre esperando requerimientos
if __name__ == '__main__':
    app.run(debug=True)