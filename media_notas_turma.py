notas = []
print("Digite as notas dos alunos (entre 0 e 10). Digite 'fim' para terminar.")

while True:
    entrada = input("Digite a nota: ")

    if entrada.lower() == 'fim':
        break

    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota inválida. A nota deve ser entre 0 e 10.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número ou 'fim'.")

if notas:
    media = sum(notas) / len(notas)
    print(f"\nNotas inseridas: {notas}")
    print(f"A média da turma é: {media:.2f}")
else:
    print("\nNenhuma nota válida foi inserida.")