from app import db, app
from app.models import Category, Product


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


if __name__ == "__main__":
    pass
