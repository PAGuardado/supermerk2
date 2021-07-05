from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, marshal_with, fields
from flask_apispec import MethodResource, doc, use_kwargs
from marshmallow import Schema
from marshmallow.fields import String, Integer
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
api = Api(app)
app.config.update({
    'APISPEC_SPEC': APISpec(
        title='OBIO REST API',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_URL': '/swagger/',  # URI to access API Doc JSON 
    'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'  # URI to access UI of API Doc
})
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
docs = FlaskApiSpec(app)

inventory_post_args = reqparse.RequestParser()
inventory_post_args.add_argument("ID", type = int, help = "El ID del producto es obligatorio", required = True)
inventory_post_args.add_argument("nombre", type = str, help = "El nombre del producto es obligatorio", required = True)
inventory_post_args.add_argument("cantidad", type = int, help = "La cantidad del producto es obligatoria", required = True)

resource_fields = {
	'id': fields.Integer,
	'nombre': fields.String,
	'cantidad': fields.Integer
}

class ProductSchema(Schema):

    id = Integer()
    nombre = String()
    cantidad = Integer()

class ProductModel(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Producto(id={self.id}, nombre={self.nombre}, cantidad={self.cantidad})"

class Inventory(MethodResource, Resource):

    @doc(description='Método GET HTTP para consultar un elemento de la base de datos.', tags=['Inventory'])
    @marshal_with(resource_fields)
    def get(self, product_id):

        product = ProductModel.query.filter_by(id=product_id).first()
        if not product:
            abort(404, message="No se encontró un producto con ese id")
        return product

    @doc(description='Método POST HTTP para añadir un elemento a la base de datos.', tags=['Inventory'])
    @use_kwargs(ProductSchema)
    @marshal_with(resource_fields)
    def post(self, product_id, **kwargs):

        args = inventory_post_args.parse_args()
        existing_product = ProductModel.query.filter_by(id=product_id).first()
        if existing_product:
            abort(409, message="Ya hay un producto con ese id...")

        product = ProductModel(id=product_id, nombre=args['nombre'], cantidad=args['cantidad'])
        db.session.add(product)
        db.session.commit()
        return product, 201

    @doc(description='Método PATCH HTTP para actualizar un elemento de la base de datos.', tags=['Inventory'])
    @use_kwargs(ProductSchema)
    @marshal_with(resource_fields)
    def patch(self, product_id, **kwargs):

        args = inventory_post_args.parse_args()
        product = ProductModel.query.filter_by(id=product_id).first()
        if not product:
            abort(404, message = 'No existe el producto, no se puede actualizar')

        if args['id']:
            product.id = args['id']
        if args['nombre']:
            product.nombre = args['nombre']
        if args['cantidad']:
            product.cantidad = args['cantidad']

        db.session.commit()

        return product

    @doc(description='Método DELETE HTTP para borrar un elemento de la base de datos', tags=['Inventory'])
    def delete(self, product_id):

        product = ProductModel.query.filter_by(id=product_id).first()
        if not product:
            abort(404, message = 'No existe el producto')

        db.session.delete(product)
        db.session.commit()
        return {'message':'Producto eliminado'}, 204

api.add_resource(Inventory, '/product/<int:product_id>')
docs.register(Inventory)

if __name__ == "__main__":
    app.run(debug=True)