from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from ariadne import graphql_sync, ObjectType, load_schema_from_path, make_executable_schema, \
    snake_case_fallback_resolvers, convert_kwargs_to_snake_case, UnionType
from ariadne.constants import PLAYGROUND_HTML
from database.models.user import User
from database.db import db
from gql.resolvers.users import resolve_users, resolve_create_user
from gql.resolvers.products import resolve_create_product, resolve_products
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres@localhost/flask_cookiecutter"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)

query = ObjectType("Query")
mutation = ObjectType("Mutation")
mutation.set_field("createUser", resolve_create_user)
mutation.set_field("createProduct", resolve_create_product)
query.set_field("users", resolve_users)
query.set_field("products", resolve_products)

type_defs = load_schema_from_path("gql/schema/")
schema = make_executable_schema(type_defs, [query, mutation, snake_case_fallback_resolvers])

@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200

@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()

    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code

if __name__ == "__main__":
    app.run(debug=True)