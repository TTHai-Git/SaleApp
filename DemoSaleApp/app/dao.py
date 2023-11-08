from app import db, app
from app.models import Category, Product, User
import hashlib


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
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    user = User(name=name.strip(), username=username.strip(), password=password
                , email=kwargs.get('email'), avatar=kwargs.get('avatar'))
    db.session.add(user)
    db.session.commit()

def get_user_by_id(user_id):
    return User.query.get(user_id)


if __name__ == "__main__":
    pass
