from flask import Flask, request, jsonify

app = Flask(__name__)

# Chave numérica de autenticação
api_key = 12345

# Rota protegida por chave
@app.route('/api/protegida', methods=['GET'])
def rota_protegida():
    # Verifique se a chave numérica foi fornecida nos cabeçalhos da solicitação
    if 'X-API-Key' in request.headers:
        provided_key = int(request.headers['X-API-Key'])
        if provided_key == api_key:
            # A chave é válida, continue com a lógica da API
            return jsonify({"message": "Bem-vindo à API protegida!"})
    
    # Se a chave não for válida, retorne um erro de autenticação
    return jsonify({"error": "Acesso não autorizado"}), 401

if __name__ == '__main__':
    app.run(debug=True)