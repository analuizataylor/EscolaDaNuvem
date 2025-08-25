
# INSERE DADOS DO VENDEDOR
nome_vendedor = input()
salario_fixo = float(input())
total_vendas = float(input())

# CALCULA COMISSAO (15%)
comissao = total_vendas * 0.15

# CALCULA SALARIO TOTAL
salario_total = salario_fixo + comissao

# EXIBE O RESULTADO
print(f"TOTAL = R$ {salario_total:.2f}")
