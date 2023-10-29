from app import db, app
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

class Category(db.Model):
   __tablename__ = "category"

   id = Column(Integer, primary_key=True, autoincrement=True)
   name = Column(String(100), nullable=False)
   products = relationship('Product', backref='category', lazy=True)


class Product(db.Model):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(150), nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String(255), nullable= False)
    status = Column(String(50), nullable=False)
    url_img = Column(String(255), nullable=False)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
