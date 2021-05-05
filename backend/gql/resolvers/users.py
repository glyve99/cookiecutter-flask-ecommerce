from database.models.user import User
from database.db import db

def resolve_create_user(obj, info, name, email):
    try:
        user = User(name=name, email=email)
        db.session.add(user)
        db.session.commit()
        payload = {
            "success": True,
            "user": user.to_dict()
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

def resolve_users(obj, info):
    try:
        users = [user for user in User.query.all()]
        payload = {
            "success": True,
            "users": users
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload