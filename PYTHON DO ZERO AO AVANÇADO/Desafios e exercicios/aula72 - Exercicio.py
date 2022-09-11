carrinho = []
carrinho.append(("Produto 1", 30))
carrinho.append(("Produto 2", 20))
carrinho.append(("Produto 3", 50))

total = sum([prod[1] for prod in carrinho])
print(total)
