import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha_aleatoria = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha_aleatoria

while True:
    try:
        tamanho_senha = int(input("Digite a quantidade de caracteres para a senha: "))
        if tamanho_senha <= 0:
            print("O tamanho da senha deve ser um número positivo.")
        else:
            senha = gerar_senha(tamanho_senha)
            print(f"Sua senha gerada é: {senha}")
            break
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")