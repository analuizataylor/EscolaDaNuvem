# Informações do produto
nome_produto = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 20

# Calcula o valor do desconto e o preço final
valor_desconto = preco_original * (porcentagem_desconto / 100)
preco_final = preco_original - valor_desconto

# Exibe todos os detalhes da compra
print(f"Produto: {nome_produto}")
print(f"Preço Original: R$ {preco_original:.2f}")
print(f"Desconto ({porcentagem_desconto}%): R$ {valor_desconto:.2f}")
print(f"Preço Final: R$ {preco_final:.2f}")
