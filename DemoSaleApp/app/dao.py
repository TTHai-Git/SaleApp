import cloudinary.uploader
from flask_login import current_user
from sqlalchemy import func

from app import db, app
from app.models import Category, Product, User, Receipt, ReceiptDetails, Comment
import hashlib


def loadcategories():
    return Category.query.all()


def loadproducts(kw=None, cate_id=None, page=None):
    products = Product.query.filter(Product.status.__eq__(True))
    if kw:
        products = products.filter(Product.name.contains(kw))

    if cate_id:
        products = products.filter(Product.category_id.__eq__(cate_id))
    if page:
        page = int(page)
        page_size = app.config['PAGE_SIZE']
        start = (page - 1) * page_size

        return products.slice(start, start + page_size)
    return products.all()


def count_products():
    return Product.query.filter(Product.status.__eq__(True)).count()


def add_user(name, username, password, email, avatar, **kwargs):
    u = User(name=name.strip(), username=username.strip(),
             password=str(hashlib.md5(password.strip().encode('utf-8')).hexdigest()), email=email.strip(),
             avatar=avatar)

    if avatar:
        res = cloudinary.uploader.upload(avatar)
        u.avatar = res['secure_url']

    db.session.add(u)
    db.session.commit()


def get_user_by_id(user_id):
    return User.query.get(user_id)


def get_user(username, password):
    return User.query.filter(User.username.__eq__(username),
                             User.password.__eq__(
                                 str(hashlib.md5(password.strip().encode('utf-8')).hexdigest()))).first()


def stats_products():
    return db.session.query(Category.id, Category.name, func.count(Product.id)). \
        outerjoin(Product, Product.category_id == Category.id).group_by(Category.id).all()


def revenue_stats(kw=None):
    query = db.session.query(Product.id, Product.name,
                             func.sum(ReceiptDetails.quantity * ReceiptDetails.unit_price)).outerjoin(
        ReceiptDetails, ReceiptDetails.product_id.__eq__(Product.id))
    if kw:
        query = query.filter(Product.name.contains(kw))
    return query.group_by(Product.id).all()


def revenue_month_stats(year=2024):
    query = db.session.query(func.extract('month', Receipt.created_date),
                             func.sum(ReceiptDetails.quantity * ReceiptDetails.unit_price)) \
        .join(Receipt, Receipt.id.__eq__(ReceiptDetails.receipt_id)). \
        filter(func.extract('year', Receipt.created_date).__eq__(year))
    return query.group_by(func.extract('month', Receipt.created_date)).all()


def add_receipt(cart):
    if cart:
        receipt = Receipt(user=current_user)
        db.session.add(receipt)
        for c in cart.values():
            d = ReceiptDetails(quantity=c['quantity'], unit_price=c['price'], product_id=c['id'], receipt=receipt)
            db.session.add(d)
        db.session.commit()


def get_product_by_id(id):
    return Product.query.get(id)


def get_comments_by_product(id):
    return Comment.query.filter(Comment.product_id.__eq__(id)).order_by(-Comment.id).all()


def add_comment(product_id, content):
    c = Comment(product_id=product_id, content=content, user=current_user)
    db.session.add(c)
    db.session.commit()

    return c

if __name__ == "__main__":
    with app.app_context():
        pass
        # print(count_products())
