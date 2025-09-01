# DADOS DE CONVERSAO
valor_reais = 100.00
taxa_dolar = 5.60
taxa_euro = 6.60

# CONVERTE PARA DOLARES E EUROS
valor_dolar = valor_reais / taxa_dolar
valor_euro = valor_reais / taxa_euro

# EXIBE RESULTADOS FORMATADOS
print(f"Valor em Reais: R$ {valor_reais:.2f}")
print(f"Valor em Dólares: US$ {valor_dolar:.2f}")
print(f"Valor em Euros: € {valor_euro:.2f}")
