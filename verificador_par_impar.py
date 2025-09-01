pares_count = 0
impares_count = 0

print("Digite números inteiros. Digite 'fim' para exibir os resultados.")

while True:
    entrada = input("Digite um número: ")

    if entrada.lower() == 'fim':
        break

    try:
        numero = int(entrada)
        if numero % 2 == 0:
            print(f"{numero} é um número par.")
            pares_count += 1
        else:
            print(f"{numero} é um número ímpar.")
            impares_count += 1
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite um número inteiro ou 'fim'.")

print("\n--- Resultados Finais ---")
print(f"Quantidade de números pares inseridos: {pares_count}")
print(f"Quantidade de números ímpares inseridos: {impares_count}")