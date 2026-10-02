# TASK-01 — Frete padrão e frete grátis por valor

## Contexto fornecido ao agente (isolamento estrito)
Apenas: `constitution.md`, `specs/checkout_frete.md` e `tasks/TASK-01.md`.

## Escopo (tamanho mínimo)
- Cobrir somente REQ-01 (frete padrão R$ 15,00) e REQ-02 (frete grátis a partir de R$ 200,00).
- Sem cupons, sem regiões, sem logs, sem persistência.

## Entregáveis
- `tests/test_frete.py` — suíte pytest escrita ANTES do código (Red).
- `src/frete.py` — implementação mínima para os testes passarem (Green).

## Rastreabilidade
Cada teste e cada trecho de código deve citar REQ-01 ou REQ-02 em comentário.

## Critério de pronto
`pytest` com 100% de aprovação.