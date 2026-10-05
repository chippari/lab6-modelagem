def calcular_total(subtotal, regiao=None, cupom=None):
    # REQ-03: IF o subtotal do carrinho for menor ou igual a R$ 0,00, THEN exibir erro
    if subtotal <= 0:
        raise ValueError("Valor de carrinho inválido")

    # Aplicação de cupom de desconto
    desconto = 0.0
    if cupom is not None:
        if cupom == "DESCONTO10":
            desconto = subtotal * 0.10
        else:
            raise ValueError("Cupom inválido")

    # REQ-02: IF o subtotal do carrinho for maior ou igual a R$ 200,00, THEN frete grátis
    if subtotal >= 200:
        frete = 0.0
    else:
        # REQ-01: Taxa de frete padrão de R$ 15,00
        frete = 15.0
        # REQ-04: WHILE a região de entrega for 'Norte', acrescentar R$ 10,00
        if regiao == "Norte":
            frete += 10.0

    # REQ-05: WHEN o valor total for calculado, arredondá-lo para 2 casas decimais
    return round((subtotal - desconto) + frete, 2)
