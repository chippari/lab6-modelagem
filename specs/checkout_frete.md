# Spec: Checkout — Cálculo de Frete

Fonte Única da Verdade (SSOT) para o cálculo de frete do checkout.
Notação: EARS (Easy Approach to Requirements Syntax).

## Requisitos

**REQ-01 (Ubiquitous):** THE SYSTEM SHALL calcular o valor total adicionando a taxa de frete padrão de R$ 15,00 ao subtotal do carrinho.

**REQ-02 (IF/THEN):** IF o subtotal do carrinho for maior ou igual a R$ 200,00, THEN THE SYSTEM SHALL conceder frete grátis (taxa = R$ 0,00).

## Fora de escopo

- Cupons de desconto
- Frete por região
- Persistência e logs
