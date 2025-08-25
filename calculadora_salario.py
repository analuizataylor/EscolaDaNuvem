# LE INFORMACOES DO USUARIO
numero_funcionario = int(input())
horas_trabalhadas = int(input())
valor_por_hora = float(input())

# CALCULA SALARIO TOTAL
salario = horas_trabalhadas * valor_por_hora

# EXIBE RESULTADO FORMATADO
print(f"NUMBER = {numero_funcionario}")
print(f"SALARY = R$ {salario:.2f}")
