def verificar_senha(senha):
    """Verifica se a senha é forte."""
    tem_numero = any(char.isdigit() for char in senha)
    tamanho_ok = len(senha) >= 8
    return tem_numero and tamanho_ok

print("Digite uma senha forte (mínimo 8 caracteres e 1 número) ou 'sair' para encerrar.")

while True:
    senha = input("Digite a senha: ")

    if senha.lower() == 'sair':
        print("Programa encerrado.")
        break  # Sai do loop

    if verificar_senha(senha):
        print("Senha forte. Aprovada!")
        break  # Sai do loop
    else:
        print("Senha fraca. A senha deve ter no mínimo 8 caracteres e conter pelo menos um número.")