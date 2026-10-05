def calcular_total(subtotal, regiao=None):
    # REQ-03: IF o subtotal do carrinho for menor ou igual a R$ 0,00, THEN exibir erro
    if subtotal <= 0:
        raise ValueError("Valor de carrinho inválido")

    # REQ-02: IF o subtotal do carrinho for maior ou igual a R$ 250,00, THEN frete grátis
    if subtotal >= 250:
        frete = 0.0
    else:
        # REQ-01: Taxa de frete padrão de R$ 15,00
        frete = 15.0
        # REQ-04: WHILE a região de entrega for 'Norte', acrescentar R$ 10,00
        if regiao == "Norte":
            frete += 10.0

    # REQ-05: WHEN o valor total for calculado, arredondá-lo para 2 casas decimais
    return round(subtotal + frete, 2)
