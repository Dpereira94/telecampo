
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Dados fictícios utilizados na demonstração inicial
ATENDIMENTOS = {
    "FTTH-2026-001": {
        "codigo": "FTTH-2026-001",
        "pon": "PON-DEMO-001",
        "status": "ABERTO"
    }
}


@app.route("/")
def inicio():
    codigo = request.args.get("codigo", "").strip()
    atendimento = None
    mensagem = None

    if codigo:
        atendimento = ATENDIMENTOS.get(codigo)

        if atendimento is None:
            mensagem = "Atendimento não localizado."

    return render_template(
        "index.html",
        atendimento=atendimento,
        mensagem=mensagem
    )


@app.route("/health")
def verificar_saude():
    return jsonify({
        "status": "ok",
        "servico": "TeleCampo"
    }), 200


if __name__ == "__main__":
    app.run(debug=False)
