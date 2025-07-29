from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/verprodutos', methods = ['GET'])
def verprodutos():
    produtos = ["Maça", "Pera", "Arroz"]
    
    return jsonify(produtos), 200

if __name__ == '__main__':
    app.run(debug=True, port=3333)
