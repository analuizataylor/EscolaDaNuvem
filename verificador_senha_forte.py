print("Crie uma senha forte. Ela deve ter no mínimo 8 caracteres e um número. Digite 'sair' para sair.")

while True:
    senha = input("Digite a sua senha: ")

    if senha.lower() == 'sair':
        print("Programa encerrado.")
        break

    if len(senha) < 8:
        print("Senha fraca: A senha deve ter pelo menos 8 caracteres.")
        continue

    contem_numero = False
    for caractere in senha:
        if caractere.isdigit():
            contem_numero = True
            break
    
    if not contem_numero:
        print("Senha fraca: A senha deve conter pelo menos um número.")
        continue
    
    print("Senha forte! Senha registrada com sucesso.")
    break