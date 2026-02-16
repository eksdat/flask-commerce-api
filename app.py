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
    return jsonify(data)


#Definir rota e função
@app.route('/')
def home():
    return '200'

if __name__ == '__main__':
    app.run(debug=True)

