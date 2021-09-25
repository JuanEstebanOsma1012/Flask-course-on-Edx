import sys

from flask import Flask, request, render_template, url_for, session
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('index.html')


@app.route('/home', methods=['GET'])
def home():
    return app.send_static_file('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        missing = []
        fields = ['email', 'passwd', 'login_submit']
        for field in fields:
            value = request.form.get(field, None)
            if value is None or value == '':
                missing.append(field)
        if missing:
            return render_template('missingFields.html', inputs=missing, next=url_for("login"))

        datosUsuario = [request.form[field] for field in fields if field != 'login_submit']
        fields = ['email', 'passwd']
        cantidadDatos = len(fields)

        return render_template('processFields.html', datos=datosUsuario, fields=fields, cantidadDatos=cantidadDatos, function='login')
    return app.send_static_file('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        missing = []
        fields = ['nickname', 'email', 'passwd', 'confirm', 'signup_submit']
        for field in fields:
            value = request.form.get(field, None)
            if value is None or value == '':
                missing.append(field)
        if missing:
            return render_template('missingFields.html', inputs=missing, next=url_for("signup"))

        datosUsuario = [request.form[field] for field in fields if field != 'signup_submit']
        fields = ['nickname', 'email', 'passwd', 'confirm']
        cantidadDatos = len(fields)

        return render_template('processFields.html', datos=datosUsuario, cantidadDatos=cantidadDatos, fields=fields, function='signup')
    return app.send_static_file('signup.html')

@app.route('/sesiones', methods=['GET'])
def sesiones():
    return app.send_static_file('sesiones.html')

@app.route('/procesarNombre', methods=['POST'])
def procesarNombre():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    session['nombre'] = nombre
    session['apellido'] = apellido
    return 'Hola ' + nombre + ' ' + apellido

@app.route('/leerSesiones', methods=['GET'])
def leerSesiones():
    return session

# start the server with the 'run()' method
if __name__ == '__main__':
    if sys.platform == 'darwin':  # different port if running on MacOsX
        app.run(debug=True, port=8080)
    else:
        app.run(debug=True, port=80)
