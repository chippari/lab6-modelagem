from frete import calcular_total


# REQ-06 (WHEN): WHEN o pedido for fechado, THE SYSTEM SHALL somar preço × quantidade de cada item do carrinho para obter o subtotal e calcular o total conforme REQ-01 a REQ-05.
def fechar_pedido(itens, regiao=None):
    subtotal = sum(preco * quantidade for preco, quantidade in itens)
    return calcular_total(subtotal, regiao)
