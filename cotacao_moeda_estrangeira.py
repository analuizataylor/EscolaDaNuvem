import pip
import requests
import datetime

def consultar_cotacao(moeda):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()
        
        chave_moeda = f"{moeda}BRL"
        if chave_moeda not in dados:
            return None, "Código de moeda inválido."

        cotacao = dados[chave_moeda]
        return cotacao, None
    except requests.exceptions.RequestException as e:
        return None, f"Erro de conexão com a API: {e}"

while True:
    moeda_input = input("Digite o código da moeda (ex: USD, EUR, BTC) ou 'sair' para encerrar: ").upper()
    if moeda_input == 'SAIR':
        break

    cotacao, erro = consultar_cotacao(moeda_input)

    if erro:
        print(f"Erro: {erro}")
    elif cotacao:
        data_hora = datetime.datetime.fromtimestamp(int(cotacao['timestamp']))
        print("\n--- Cotação da Moeda ---")
        print(f"Moeda: {cotacao['name']}")
        print(f"Valor de Venda (Ask): R$ {float(cotacao['ask']):.4f}")
        print(f"Valor Máximo (High): R$ {float(cotacao['high']):.4f}")
        print(f"Valor Mínimo (Low): R$ {float(cotacao['low']):.4f}")
        print(f"Última Atualização: {data_hora.strftime('%d/%m/%Y %H:%M:%S')}")
        print("-" * 30)