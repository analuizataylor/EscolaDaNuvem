idade = int(input("Digite sua idade: "))


if 0 <= idade <= 12:
    classificacao = "Criança"
elif 13 <= idade <= 17:
    classificacao = "Adolescente"
elif 18 <= idade <= 59:
    classificacao = "Adulto"
else:
    classificacao = "Idoso"


print(f"Você se encaixa na categoria: {classificacao}")
