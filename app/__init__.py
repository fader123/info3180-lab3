from flask import Flask
from flask_mail import Mail

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thefadergang'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '465'
app.config['MAIL_USERNAME'] = '	60d5c8fb5d1772'
app.config['MAIL_PASSWORD'] = 'bdaa804e9f00c8'

mail = Mail(app)
from app import views