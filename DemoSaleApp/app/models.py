import hashlib
from datetime import datetime

from flask_login import UserMixin

from app import db, app
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, ForeignKey, Enum
from sqlalchemy.orm import relationship, backref
import enum


class UserRole(enum.Enum):
    ADMIN = 1
    USER = 2


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    avatar = Column(String(255),
                    default='https://res.cloudinary.com/dh5jcbzly/image/upload/v1703666812/hme7xdtwowv4rloj1dzq.jpg')
    email = Column(String(100), unique=True)
    phone = Column(String(10), nullable=True, default='Text')
    address = Column(String(255), nullable=True, default='Text')
    active = Column(Boolean, default=True)
    joined_data = Column(DateTime, default=datetime.now())
    user_role = Column(Enum(UserRole), default=UserRole.USER)
    receipts = relationship('Receipt', backref='user', lazy=True)
    comments = relationship('Comment', backref='user', lazy=True)

    def __str__(self):
        return self.name


class Category(db.Model):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    products = relationship('Product', backref='category', lazy=True)

    def __str__(self):
        return self.name


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
    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)
    tags = relationship('Tag', secondary='product_tag', lazy='subquery',
                        backref=backref('products', lazy=True))
    receipt_details = relationship('ReceiptDetails', backref='product', lazy=True)
    comments = relationship('Comment', backref='product', lazy=True)

    def __str__(self):
        return self.name


class Tag(db.Model):
    __tablename__ = "tag"

    id = Column(String(10), primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(255), nullable=False, unique=True)

    def __str__(self):
        return self.name


class Department(db.Model):
    __tablename__ = "department"
    maphongban = Column(String(10), primary_key=True)
    tenphongban = Column(String(100), nullable=False, default=None)
    nhanviens = relationship('Employee', backref='department', lazy=True)

    def __str__(self):
        return self.tenphongban


class Employee(db.Model):
    __tablename__ = "employee"
    manhanvien = Column(String(10), primary_key=True)
    tennhanvien = Column(String(100), nullable=False)
    sodienthoai = Column(String(10), unique=True, default=None)
    diachi = Column(String(255), nullable=True, default=None)
    ma_phongban = Column(String(10), ForeignKey('department.maphongban'), nullable=False)

    def __str__(self):
        return self.tennhanvien


class Customer(db.Model):
    __tablename__ = "customer"
    makhachhang = Column(String(10), primary_key=True)
    tenkhachhang = Column(String(100), nullable=False, default=None)
    sodienthoai = Column(String(10), nullable=True, default=None, unique=True)
    diachi = Column(String(255), nullable=True, default=None, unique=True)
    email = Column(String(100), nullable=True, unique=True, default=None)

    def __str__(self):
        return self.tenkhachhang


class BaseModel(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    active = Column(Boolean, default=True)
    created_date = Column(DateTime, default=datetime.now())


class Receipt(BaseModel):
    user_id = Column(Integer, ForeignKey(User.id), nullable=True)
    receipt_details = relationship('ReceiptDetails', backref='receipt', lazy=True)


class ReceiptDetails(BaseModel):
    quantity = Column(Integer, default=0)
    unit_price = Column(Float, default=0)
    receipt_id = Column(Integer, ForeignKey(Receipt.id), nullable=False)
    product_id = Column(Integer, ForeignKey(Product.id), nullable=False)


class Interaction(BaseModel):
    __abstract__ = True
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    product_id = Column(Integer, ForeignKey(Product.id), nullable=False)


class Comment(Interaction):
    content = Column(String(255), nullable=False)
    created_date = Column(DateTime, default=datetime.now())


if __name__ == "__main__":
    with app.app_context():
        # pass
        db.drop_all()
        #
        db.create_all()
        c1 = Category(name='Laptop')
        c2 = Category(name='PC')
        c3 = Category(name='Tablet')
        c4 = Category(name='Mobile')

        db.session.add_all([c1, c2, c3, c4])
        db.session.commit()

        p1 = Product(name='Iphone 14 Promax', price=33000000, description='Apple, 32GB, 128MGP', status=True,
                     url_img='https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg',
                     category_id=4)
        p2 = Product(name='Samsung Galaxy S20 Ultra', price=22000000, description='Samsung, 32GB, 128MGP', status=True,
                     url_img='https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg',
                     category_id=4)
        p3 = Product(name='Lenovo Ideapad Gamming 3', price=16000000,
                     description='Lenovo, AMD, 8GB, 250GB SSD, I5 Gen12...',
                     status=True,
                     url_img='https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg',
                     category_id=1)
        p4 = Product(name='Ipad Pro 2021', price=28000000, description='Apple, 64GB, 128GB', status=True,
                     url_img='https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg',
                     category_id=3)
        p5 = Product(name='PC Vipper', price=12000000, description='Intel, 16GB, 250GB SSD, I3 Gen12', status=True,
                     url_img='https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg',
                     category_id=2)

        db.session.add_all([p1, p2, p3, p4, p5])
        db.session.commit()
        #
        # tag1 = Tag(id='pmt', name='promotion', description='khuyến mãi')
        # tag2 = Tag(id='new', name='new', description='Hàng Mới Nhập Khẩu')
        #
        # db.session.add_all([tag1, tag2])
        # db.session.commit()
        #
        u1 = User(name='User', username='user', password=str(hashlib.md5('123456'.strip().encode('utf-8')).hexdigest()))
        u2 = User(name='Admin', username='admin',
                  password=str(hashlib.md5('123456'.strip().encode('utf-8')).hexdigest()), user_role=UserRole.ADMIN)

        db.session.add_all([u1, u2])
        db.session.commit()

        # Thêm dữ liêu từ model ánh xạ xuống database

        # p = Product.query.get(1)
        # print(p.name)
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

        # ods = Order_Details(makhachhangmua='KH_01', masanphammua=1, soluongmua=2, thanhtien=66000000,
        #                     ghichu="Khách hàng đã thanh toán qua the. Yêu cầu giao hàng tận nợi")
        # db.session.add(ods)
        # db.session.commit()
