from flask import Flask, request, jsonify
from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt_identity
)
from flask_cors import CORS
from models import db, Usuario, Produto, Categoria
from config import Config

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)

db.init_app(app)
jwt = JWTManager(app)

with app.app_context():
    db.create_all()

@app.route('/cadastra_usuario', methods= ['POST'])
def cadastraUsuario():
    data = request.json
    if Usuario.query.filter_by(email=data['email']).first():
        return jsonify({"erro": "Email já cadastrado"}), 400
    
    usuario = Usuario(
        nome=data['nome'],
        email=data['email'],
        cpf=data['cpf'],
        cidade=data['cidade'],
        endereco=data['endereco']
    )
    usuario.set_senha(data['senha'])
    db.session.add(usuario)
    db.session.commit()
    return jsonify(usuario.to_dict()), 201

@app.route('/autenticacaoUsuario', methods= ['POST'])
def autenticaUsuario():
    data = request.json
    usuario = Usuario.query.filter_by(email=data['email']).first()
    if usuario and usuario.verificar_senha(data['senha']):
        token = create_access_token(identity=usuario.id)
        return jsonify({
            "mensagem": "login bem sucedido",
            "token": token,
            "usuario": usuario.to_dict()
            }), 200
    return jsonify("Credenciais Inválidas"), 401

@app.route('/listaCategorias', methods= ['GET'])
# @jwt_required()
def lista_categoria():
    categorias = Categoria.query.all()
    
    return jsonify([cat.to_dict() for cat in categorias]), 200

@app.route('/produtos', methods= ['GET'])
# @jwt_required()
def listar_produtos_categoria():
    id = request.args.get('id', type=int)
    produtos = Produto.query.filter_by(categoria_id=id).all()

    return jsonify([prod.to_dict() for prod in produtos]), 200

@app.route('/produto', methods= ['GET'])
# @jwt_required()
def detalhe_info_produto():
    id = request.args.get('id', type=int)
    produto = Produto.query.get_or_404(id)

    return jsonify(produto.to_dict()), 200

@app.route('/maiscomprados', methods= ['GET'])
# @jwt_required()
def prod_mais_comprados():
    produtos = Produto.query.limit(5).all()

    return jsonify([prod.to_dict() for prod in produtos]), 200

if __name__ == '__main__':
    app.run(debug=True, port=3333)
