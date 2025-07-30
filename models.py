from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha_hash = db.Column(db.String(128), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    cidade = db.Column(db.String(20), nullable=False)
    endereco = db.Column(db.String(50), nullable=False)

    def set_senha(self, senha):
        self.senha_hash = generate_password_hash(senha)

    def verificar_senha(self, senha):
        return check_password_hash(self.senha_hash, senha)

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "cpf": self.cpf,
            "cidade": self.cidade,
            "endereco": self.endereco
        }

class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    produtos = db.relationship('Produto', backref='categoria', lazy=True)
    imagem_url = db.Column(db.String(200))
    
    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "imagem_url": self.imagem_url
        }

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False) 
    imagem_url = db.Column(db.String(200))
    images_url = db.Column(db.String(200))
    descricao = db.Column(db.String(1000))
    caracteristicas = db.Column(db.String(500))
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "preco": self.preco,
            "imagem_url": self.imagem_url,
            "images_url": self.images_url,
            "categoria_id": self.categoria_id,
            "categoria": self.categoria.nome,
            "descricao": self.descricao,
            "caracteristicas": self.caracteristicas
        }
