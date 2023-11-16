from app import db, app
from app.models import Category, Product, User
import hashlib


def loadcategories():
    return Category.query.all()


def loadproducts(kw=None, cate_id=None):
    products = Product.query
    if kw:
        products = products.filter(Product.name.contains(kw))
    if cate_id:
        products = products.filter(Product.category_id.__eq__(cate_id))
    else:
        return products.all()
    return products.all()


def add_user(name, username, password, email, **kwargs):
    db.session.add(User(name=name.strip(), username=username.strip(),
                        password=str(hashlib.md5(password.strip().encode('utf-8')).hexdigest()), email=email.strip()))
    db.session.commit()


def get_user_by_id(user_id):
    return User.query.get(user_id)


def get_user(username, password):
    return User.query.filter(User.username.__eq__(username),
                             User.password.__eq__(
                                 str(hashlib.md5(password.strip().encode('utf-8')).hexdigest()))).first()


if __name__ == "__main__":
    with app.app_context():
        pass
