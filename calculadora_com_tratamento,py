
while True:
    try:
        # INSERE NUMERO E OPERACAO
        num1 = float(input("Digite o primeiro número: "))
        operacao = input("Digite a operação (+, -, *, /): ")
        num2 = float(input("Digite o segundo número: "))

        # REALIZA OPERACAO COM BASE NA ENTRADA
        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            if num2 == 0:

                # TRATAMENTO DE ERRO
                print("Erro: Divisão por zero não é permitida.")
                continue  # VOLTA PARA O LOOP
            resultado = num1 / num2
        else:

            # TRATA OPERACAO INVALIDA
            print("Erro: Operação inválida. Use +, -, * ou /.")
            continue  # Volta para o início do loop

        # EXIBE O RESULTADO
        print(f"O resultado é: {resultado}")
        break  # SAI DO LOOP

    except ValueError:
        # TRATA ERRO DE ENTRADA NAO NUMERICA
        print("Erro: Entrada inválida. Por favor, digite apenas números.")