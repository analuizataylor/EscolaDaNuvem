import requests

try:
    url = "https://randomuser.me/api/"
    resposta = requests.get(url)
    resposta.raise_for_status()  # Lança um erro para códigos de status HTTP 4xx/5xx
    
    dados = resposta.json()
    usuario = dados['results'][0]
    
    nome = f"{usuario['name']['first']} {usuario['name']['last']}"
    email = usuario['email']
    pais = usuario['location']['country']
    
    print("--- Perfil de Usuário Aleatório ---")
    print(f"Nome: {nome}")
    print(f"Email: {email}")
    print(f"País: {pais}")

except requests.exceptions.RequestException as e:
    print(f"Erro de conexão com a API: {e}")
except KeyError:
    print("Erro ao processar os dados da API. A estrutura da resposta pode ter mudado.")