from app import db, app
from app.models import Category, Product, User
import hashlib
import bcrypt


def loadnavbaritems():
    navbaritems = Category.query.all()
    return navbaritems


def loadproducts(kw=None):
    products = Product.query.all()
    if kw:
        products = [p for p in products if p.name.lower().find(kw.lower()) >= 0]
    else:
        return products
    return products


def add_user(name, username, password, email, **kwargs):
    # password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    salt = bcrypt.gensalt(rounds=12)
    hashed_password = bcrypt.hashpw(password.strip().encode('utf-8'), salt)# HashPassword then cover tostring => string_password = user.password.decode('utf-8')
    user = User(name=name.strip(), username=username.strip(), password=hashed_password
                , email=kwargs.get('email'), avatar=kwargs.get('avatar'))
    db.session.add(user)
    db.session.commit()


def check_user(username, password):
    return bcrypt.checkpw(password.strip().encode('utf8'),
                          User.query.filter_by(username=username).first().password.encode('utf8'))


def get_user_by_id(user_id):
    return User.query.get(user_id)

def get_user(username,password):
    password

if __name__ == "__main__":
    with app.app_context():
       pass

