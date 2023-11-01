from datetime import datetime

from app import db, app
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, ForeignKey, VARCHAR, NCHAR
from sqlalchemy.orm import relationship, backref


class Category(db.Model):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    products = relationship('Product', backref='category', lazy=True)


product_tag = db.Table('product_tag',
                       Column('product_id', Integer, ForeignKey('product.id'), primary_key=True),
                       Column('tag_id', String(10), ForeignKey('tag.id'), primary_key=True))


class Product(db.Model):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(150), nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String(255), nullable=False)
    status = Column(Boolean, nullable=False)
    create_date = Column(DateTime, default=datetime.now())
    url_img = Column(String(255), nullable=False)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)
    tags = relationship('Tag', secondary='product_tag', lazy='subquery',
                        backref=backref('products', lazy=True))
    bills = relationship('Bill', backref('product'), lazy=True)


class Tag(db.Model):
    __tablename__ = "tag"

    id = Column(String(10), primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(255), nullable=False, unique=True)


class Department(db.Model):
    __tablename__ = "department"
    mapb = Column(String(10), primary_key=True)
    tenpb = Column(String(100), nullable=False, default=None)
    nhanviens = relationship('Employee', backref('department'), lazy=True)


class Employee(db.Model):
    __tablename__ = "employee"
    manv = Column(String(10), primary_key=True)
    tennv = Column(String(100), nullable=False,)
    sodienthoai = Column(String(10), unique=True, default=None)
    diachi = Column(String(255), nullable=True, default=None)
    ma_pb = Column(String(10), ForeignKey(Department.mapb), nullable=False)

class Customer(db.Model):
    __tablename__ = "customer"
    makh = Column(String(10), primary_key=True)
    tenkh = Column(String(100), nullable=False, default=None)
    sodienthoai = Column(String(10), nullable=True, default=None)
    diachi = Column(String(255), nullable=True, default=None, unique=True)
    email = Column(String(100), nullable=True, unique=True, default=None)
    bills = relationship('Bill', backref('customer'), lazy=True)

class Bill(db.Model):
    __tablename__ = "bill"
    idhd = Column(Integer, primary_key=True)
    soluong = Column(Integer, nullable=False)
    thanhtien = Column(Float, nullable=False)
    ngaylaphoadon = Column(DateTime, nullable=False, default=datetime.now())
    makh = Column(String(10), ForeignKey(Customer.makh), nullable=False)
    product_id = Column(Integer, ForeignKey(Product.id), nullable=False)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        # c1 = Category(name='Laptop')
        # c2 = Category(name='PC')
        # c3 = Category(name='Tablet')
        # c4 = Category(name='Mobile')
        #
        # db.session.add(c1)
        # db.session.add(c2)
        # db.session.add(c3)
        # db.session.add(c4)

        # p1 = Product(name='Iphone 14 Promax', price=33000000, description='Apple, 32GB, 128MGP', status=True,
        #              url_img='url', category_id=4)
        # p2 = Product(name='Samsung Galaxy S20 Ultra', price=22000000, description='Samsung, 32GB, 128MGP', status=True,
        #              url_img='url', category_id=4)
        # p3 = Product(name='Lenovo Ideapad Gamming 3', price=16000000, description='Lenovo, AMD, 8GB, 250GB SSD, I5 Gen12...',
        #              status=True,
        #              url_img='url', category_id=1)
        # p4 = Product(name='Ipad Pro 2021', price=28000000, description='Apple, 64GB, 128GB', status=True,
        #              url_img='url', category_id=3)
        # p5 = Product(name='PC Vipper', price=12000000, description='Intel, 16GB, 250GB SSD, I3 Gen12', status=True,
        #              url_img='url', category_id=2)
        #
        # db.session.add(p2)
        # db.session.add(p3)
        # db.session.add(p4)
        # db.session.add(p5)
        # db.session.commit()

        # tag1 = Tag(id='pmt', name='promotion', description='khuyến mãi')
        # tag2 = Tag(id='new', name='new', description='Hàng Mới Nhập Khẩu')
        #
        # db.session.add(tag1)
        # db.session.add(tag2)

        # db.session.commit()

        # Thêm dữ liêu từ model ánh xạ xuống database

        # p = Product.query.get(1)
        # print(p.__dict__)
        # print(p.category.__dict__)
        #
        # c = Category.query.get(4)
        # print(c.products)
        #
        # t1 = Tag.query.get('new')
        # t2 = Tag.query.get('pmt')
        #
        # print(t1.name + "\t" + t1.description)
        # print(t2.name + "\t" + t2.description)
        #
        # p.tags.append(t1)
        # p.tags.append(t2)
        #
        # db.session.add(p)
        # db.session.commit()

        # print(p.tags)

        # print(t1.products)

        # print(t2.products)

        # Update And Select Query

        # laptop = db.session.execute(db.select(Product).filter_by(name='Lenovo Ideapad Gamming 3')).scalar_one()
        # laptop.description = 'Lenovo, 16GB, 250GB SSD, I5 Gen12'
        # db.session.commit()
