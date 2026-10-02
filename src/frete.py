# REQ-01: adiciona a taxa padrão ao subtotal.
# REQ-02: concede frete grátis para subtotal a partir de R$ 200,00.
def calcular_total(subtotal):
    if subtotal >= 200:
        return subtotal
    return subtotal + 15