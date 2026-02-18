from flask import Flask, request, jsonify 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///commerce.db'

db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(200), nullable=True)

@app.route('/api/products/add', methods=['POST'])
def add_product():
    data = request.get_json()
    if 'name' not in data or 'price' not in data:
        return jsonify({'error': 'Nome e preço são obrigatórios!'}), 400
        product = Product(name=data['name'], price=data['price'], description=data.get('description', ''))
        return jsonify(data)
        db.session.add(product)
        db.session.commit()
        return jsonify({'message': 'Produto adicionado com sucesso!'}), 201
    return jsonify({'error': 'Dados inválidos!'}), 400

@app.route('/api/products/delete/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'error': 'Produto não encontrado!'}), 404
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Produto deletado com sucesso!'}), 200

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product_details(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'error': 'Produto não encontrado!'}), 404
    return jsonify({
        'id': product.id,
        'name': product.name,
        'price': product.price,
        'description': product.description
    }), 200

@app.route('/api/products/update/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'error': 'Produto não encontrado!'}), 404
    data = request.get_json()
    if 'name' in data:
        product.name = data['name']
    if 'price' in data:
        product.price = data['price']
    if 'description' in data:
        product.description = data['description']
    db.session.commit()
    return jsonify({'message': 'Produto atualizado com sucesso!'}), 200

#não testei
@app.route('/api/products', methods=['GET'])
def list_products():
    products = Product.query.all()
    return jsonify([{
        'id': product.id,
        'name': product.name,
        'price': product.price,
        'description': product.description
    } for product in products]), 200


@app.route('/')
def home():
    return '200'

if __name__ == '__main__':
    app.run(debug=True)

