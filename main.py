from flask import Flask, send_file
from flask_sqlalchemy import SQLAlchemy
from flask import request, redirect  # Importa las funciones request y redirect
from werkzeug.security import generate_password_hash  # Importa la función para encriptar contraseñas
from flask import Flask, send_file
from flask_mail import Mail, Message
from flask import Flask, render_template

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://4429487_lacteossanluis:pupitre.123@fdb1034.awardspace.net:3306/4429487_lacteossanluis'

db = SQLAlchemy(app)



@app.route("/")
def index():
    return send_file("html/index.html")

@app.route("/index.html")
def index1():
    return send_file("html/index.html")

@app.route("/login.html")
def login():
    return send_file("html/login.html")

@app.route("/register.html")
def register():
    return send_file("html/register.html")


if __name__ == "__main__":
    app.run()
