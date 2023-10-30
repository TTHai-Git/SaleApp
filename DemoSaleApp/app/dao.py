from app import db, app
from app.models import Category, Product


def loadnavbaritems():
    navbaritems = db.session.query(Category).all()
    return navbaritems


def loadproducts(kw=None):
    products = db.session.query(Product).all()
    if kw:
        products = [p for p in products if p.name.lower().find(kw.lower()) >= 0]
    else:
        return products
    return products


if __name__ == "__main__":
    pass
