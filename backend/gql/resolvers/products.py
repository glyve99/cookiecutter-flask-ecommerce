from database.models.products import Product
from database.db import db

def resolve_create_product(obj, info, title, description, price, created_at):
    try:
        product = Product(title=title, description=description, price=price, created_at=created_at)
        db.session.add(product)
        db.session.commit()
        payload = {
            "success": True,
            "product": product.to_dict()
        }
    except Exception as Error:
        payload = {
            "success": False,
            errors: [str(error)]
        }
    return payload

def resolve_products(obj, info):
    try:
        products = Product.query.all()
        payload = {
            "success": True,
            "products": products
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload