pares = 0
impares = 0
print("Digite números inteiros ou 'fim' para encerrar.")

while True:
    entrada = input("Digite um número: ")

    if entrada.lower() == 'fim':
        break  # Sai do loop

    try:
        numero = int(entrada)
        if numero % 2 == 0:
            print(f"{numero} é um número par.")
            pares += 1
        else:
            print(f"{numero} é um número ímpar.")
            impares += 1
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro ou 'fim'.")

print("\n--- Resumo ---")
print(f"Total de números pares: {pares}")
print(f"Total de números ímpares: {impares}")