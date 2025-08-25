
# INSERE OS DADOS
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

# CALCULA O IMC
imc = peso / (altura ** 2)

# CLASSIFICA O IMC
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"

# EXIBE O RESULTADO
print(f"Seu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")
