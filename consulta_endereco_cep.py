import requests

def consultar_cep(cep):

    # RETIRA CARACTERES ESPECIAIS DO CEP
    cep = cep.replace("-", "").replace(".", "").strip()

    # VERIFICA SE POSSUI 8 DIGITOS OU SE NAO EH NUMERICO
    if len(cep) != 8 or not cep.isdigit():
        return None, "O CEP deve conter 8 dígitos."

    # API
    url = f"https://viacep.com.br/ws/{cep}/json/"
    
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()
        
        if 'erro' in dados and dados['erro']:
            return None, "CEP não encontrado."
        
        return dados, None
    except requests.exceptions.RequestException as e:
        return None, f"Erro de conexão com a API: {e}"

while True:
    cep_input = input("Digite um CEP (ex: 01001-000) ou 'sair' para encerrar: ")
    if cep_input.lower() == 'sair':
        break
    
    dados_endereco, erro = consultar_cep(cep_input)
    
    if erro:
        print(f"Erro: {erro}")
    elif dados_endereco:
        print("\n--- Informações do Endereço ---")
        print(f"Logradouro: {dados_endereco['logradouro']}")
        print(f"Bairro: {dados_endereco['bairro']}")
        print(f"Cidade: {dados_endereco['localidade']}")
        print(f"Estado: {dados_endereco['uf']}")
        print("-" * 30)