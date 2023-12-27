from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
from flask_admin import Admin
import cloudinary

app = Flask(__name__)

cloudinary.config(
    cloud_name="dh5jcbzly",
    api_key="956284944785852",
    api_secret="ZYqL_9IS8N4a6uZ1esDJUBHNeq4"
)

app.secret_key = 'Security'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:%s@localhost/saledb?charset=utf8mb4' % quote('123456a@A')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['PAGE_SIZE'] = 3

db = SQLAlchemy(app)

admin = Admin(app=app, name="Quản Trị Bán Hàng", template_mode='bootstrap4')
login = LoginManager(app=app)
