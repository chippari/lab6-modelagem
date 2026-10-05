# Audit Report — Exercício 2

Prompt ambíguo: "Implemente a funcionalidade de aplicação de cupom de desconto 'DESCONTO10' para a classe de frete."

Resultado do pytest com o cupom: 5 passed. Os testes não detectaram o drift.

## 1. Matriz de Rastreabilidade

- REQ-01 (Padrão): Sim — teste em test_frete.py:13 — código em frete.py:19
- REQ-02 (Grátis): Sim — teste em test_frete.py:21 — código em frete.py:15
- REQ-03 (Inválido): Sim — teste em test_frete.py:33 — código em frete.py:3
- REQ-04 (Norte): Sim — teste em test_frete.py:44 — código em frete.py:21
- REQ-05 (Arredondamento): Sim — teste em test_frete.py:56 — código em frete.py:25
- CUPOM (Sem Spec): DRIFT DETECTADO — nenhum teste — código em frete.py:6

## 2. Passe de Revisão

- Arquitetura: não importou biblioteca, mas o código do cupom não tem REQ correspondente, o que viola a constituição.
- Performance: sem loops desnecessários.
- Segurança: sem print de dados sensíveis, mas o frete grátis é calculado antes do desconto (R$ 200,00 com cupom paga R$ 180,00 e ainda ganha frete grátis).
- Observabilidade: código legível, mas o bloco do cupom não cita nenhum REQ.

## 3. Ação de Correção

Prompt ao Antigravity: "Remova todo o código de cupom de src/frete.py, pois ele não tem especificação em specs/checkout_frete.md. Restaure o alinhamento 100% com a spec."