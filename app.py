from flask import Flask, render_template, request, jsonify
import requests
from datetime import datetime, timedelta

app = Flask(__name__)

# URL da API de câmbio
URL = "https://open.er-api.com/v6/latest/USD"

# Cache para evitar chamadas frequentes
ultima_atualizacao = None
dados = {}

def atualizar_taxas():
    """Busca taxas de câmbio e atualiza os dados globalmente."""
    global ultima_atualizacao, dados
    try:
        resposta = requests.get(URL, timeout=10)
        resposta.raise_for_status()
        dados = resposta.json()
        if "rates" not in dados:
            raise ValueError("Dados inválidos da API!")
        ultima_atualizacao = datetime.now()
    except requests.RequestException as e:
        print(f"Erro ao buscar taxas: {e}")
    except ValueError as e:
        print(f"Erro nos dados recebidos: {e}")


@app.route("/")
def index():
    global ultima_atualizacao, dados
    if ultima_atualizacao is None or (datetime.now() - ultima_atualizacao > timedelta(minutes=5)):
        atualizar_taxas()  # Garante que os dados estão atualizados

    ultima_atualizacao_formatada = ultima_atualizacao.strftime(
        "%d/%m/%Y %H:%M:%S") if ultima_atualizacao else "Desconhecida"
    return render_template("index.html", taxas=dados.get("rates", {}), ultima_atualizacao=ultima_atualizacao_formatada)


@app.route("/converter", methods=["POST"])
def converter():
    """API para conversão dinâmica de moedas."""
    global dados

    if not dados.get("rates"):
        return jsonify({"erro": "Falha ao obter taxas de câmbio."}), 400

    moeda_origem = request.json.get("moeda_origem", "").upper()
    moeda_destino = request.json.get("moeda_destino", "").upper()
    valor = request.json.get("valor")

    try:
        valor = float(valor)

        if moeda_origem not in dados["rates"] or moeda_destino not in dados["rates"]:
            return jsonify({"erro": "Moeda inválida."}), 400

        taxa_origem = dados["rates"][moeda_origem]
        taxa_destino = dados["rates"][moeda_destino]
        taxa_convertida = (valor / taxa_origem) * taxa_destino

        return jsonify({
            "convertido": round(taxa_convertida, 2),
            "ultima_atualizacao": ultima_atualizacao.strftime("%d/%m/%Y %H:%M:%S") if ultima_atualizacao else "Desconhecida"
        })

    except (ValueError, TypeError):
        return jsonify({"erro": "Valor inválido."}), 400

if __name__ == "__main__":
    app.run(debug=True)
