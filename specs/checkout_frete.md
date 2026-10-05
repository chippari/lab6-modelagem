# Spec: Checkout — Cálculo de Frete

[ Especificação EARS - Parâmetros do Sistema ]

REQ-01 (Ubiquitous): THE SYSTEM SHALL calcular o valor total adicionando a taxa de frete padrão de R$ 15,00 ao subtotal do carrinho.

REQ-02 (IF/THEN): IF o subtotal do carrinho for maior ou igual a R$ 200,00, THEN THE SYSTEM SHALL conceder frete grátis (taxa = R$ 0,00).

REQ-03 (IF/THEN): IF o subtotal do carrinho for menor ou igual a R$ 0,00, THEN THE SYSTEM SHALL exibir o erro 'Valor de carrinho inválido'.

REQ-04 (WHILE): WHILE a região de entrega for 'Norte', THE SYSTEM SHALL acrescentar R$ 10,00 à taxa de frete. Demais regiões: manter taxa padrão.

REQ-05 (WHEN): WHEN o valor total for calculado, THE SYSTEM SHALL arredondá-lo para 2 casas decimais.
