
from flask import Flask, jsonify

# Aplicação inicial do TeleCampo
app = Flask(__name__)


@app.route("/")
def inicio():
    """Apresenta informações iniciais do sistema."""
    return jsonify({
        "projeto": "TeleCampo",
        "descricao": "Plataforma de Apoio ao Técnico de Campo",
        "versao": "0.1.0",
        "status": "Em desenvolvimento"
    })


@app.route("/health")
def verificar_saude():
    """Verifica se a aplicação está respondendo."""
    return jsonify({
        "status": "ok",
        "servico": "TeleCampo"
    }), 200


if __name__ == "__main__":
    app.run(debug=False)
