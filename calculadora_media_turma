notas = []
print("Digite as notas (0-10) ou 'fim' para calcular a média.")

while True:
    entrada = input("Digite uma nota: ")

    if entrada.lower() == 'fim':
        break  # Sai do loop

    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota inválida. Por favor, digite um valor entre 0 e 10.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número ou 'fim'.")

if notas:
    media = sum(notas) / len(notas)
    print(f"\nNotas válidas inseridas: {notas}")
    print(f"A média da turma é: {media:.2f}")
else:
    print("Nenhuma nota válida foi inserida.")