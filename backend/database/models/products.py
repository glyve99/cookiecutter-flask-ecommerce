from database.db import db
from sqlalchemy import Column, Integer, String, Float, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class Product(db.Model):

    id = Column(Integer, primary_key=True)
    title = Column(String)
    price = Column(Float)
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.now())
    photos = relationship("Photo")

    def __repr__(self):
        return f"{self.title}, {self.price}"

    def to_dict(self):
        return {
            "title": self.title,
            "price": self.price,
            "description": self.description,
            "created_at": self.created_at
        }

class Photo(db.Model):

    id = Column(Integer, primary_key=True)
    product = Column(Integer, ForeignKey('product.id'))
    uri = Column(String)