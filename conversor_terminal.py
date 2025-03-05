import requests
from datetime import datetime, timedelta

# URL da API de câmbio
URL = "https://open.er-api.com/v6/latest/USD"

# Variáveis globais
ultima_atualizacao = None
dados = {}


def atualizar_taxas():
    global ultima_atualizacao, dados
    try:
        resposta = requests.get(URL, timeout=10)
        resposta.raise_for_status()
        novos_dados = resposta.json()
        if "rates" not in novos_dados:
            raise ValueError("Dados inválidos da API!")

        dados = novos_dados
        ultima_atualizacao = datetime.now()
    except requests.RequestException as e:
        print("⚠ Erro na API, mantendo últimas taxas disponíveis.")

    except ValueError as e:
        print(f"❌ Erro nos dados recebidos: {e}")


def obter_taxa(moeda):
    """Retorna a taxa de câmbio da moeda informada."""
    if moeda not in dados.get("rates", {}):
        print(f"❌ Moeda '{moeda}' não encontrada!")
        return None
    return dados["rates"][moeda]


def converter_moeda(moeda_origem, moeda_destino, valor):
    """Converte um valor entre duas moedas usando as taxas de câmbio atualizadas."""
    taxa_origem = obter_taxa(moeda_origem)
    taxa_destino = obter_taxa(moeda_destino)

    if taxa_origem is None or taxa_destino is None:
        return None

    return (valor / taxa_origem) * taxa_destino


def entrada_usuario():
    """Captura e valida os inputs do usuário."""
    while True:
        moeda_origem = input("Digite a moeda de origem (ou 'sair' para encerrar): ").upper()
        if moeda_origem == "SAIR":
            print("Encerrando o conversor. Até mais!")
            return None, None, None

        moeda_destino = input("Digite a moeda de destino: ").upper()

        try:
            valor = float(input(f"Digite o valor em {moeda_origem}: "))
            return moeda_origem, moeda_destino, valor
        except ValueError:
            print("❌ Erro: Digite um número válido para o valor!")


# Atualiza na inicialização
atualizar_taxas()

print(f"Programa iniciado em: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("Bem-vindo ao Conversor de Moedas!")

# Loop principal
while True:
    moeda_origem, moeda_destino, valor = entrada_usuario()
    if moeda_origem is None:
        break  # Sai do loop se o usuário quiser sair

    if ultima_atualizacao is None:
        atualizar_taxas()  # Atualiza imediatamente se nunca foi atualizado
    elif datetime.now() - ultima_atualizacao > timedelta(minutes=5):
        print("🔄 Atualizando taxas de câmbio...")
        atualizar_taxas()

    print(f"Última atualização em: {ultima_atualizacao.strftime('%Y-%m-%d %H:%M:%S')}")

    convertido = converter_moeda(moeda_origem, moeda_destino, valor)

    if convertido is not None:
        print(f"✅ {valor} {moeda_origem} equivale a {convertido:.2f} {moeda_destino}")
