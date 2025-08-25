# LE AS QUATRO NOTAS COM UMA CASA DECIMAL
n1, n2, n3, n4 = map(float, input().split())

# CALCULA A MEDIA PONDERADA
media = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / 10.0

# EXIBE A MEDIA PONDERADA
print(f"Media: {media:.1f}")

# VERIFICA A SITUACAO DO ALUNO

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else: 
    
    # MEDIA ENTRE 5 E 6.9
    print("Aluno em exame.")
    nota_exame = float(input())
    print(f"Nota do exame: {nota_exame:.1f}")
    
    # RECALCULA A NOTA COM A NOTA DO EXAME
    media_final = (media + nota_exame) / 2.0
    
    if media_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    
    print(f"Media final: {media_final:.1f}")
