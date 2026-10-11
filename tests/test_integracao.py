"""Testes de integração entre carrinho e frete.

Roteiro de testes: roteiro_testes.md (CT-06 a CT-08)
Especificação: specs/checkout_frete.md
"""

import pytest
from carrinho import fechar_pedido


# CT-06 — Carrinho calcula subtotal e aplica frete do Norte
def test_ct06_carrinho_calcula_subtotal_e_aplica_frete_norte():
    # 2 itens de R$ 50,00; região Norte -> subtotal R$ 100,00 + frete R$ 25,00 = R$ 125,00
    assert fechar_pedido([(50.00, 2)], "Norte") == 125.00


# CT-07 — Soma de itens diferentes atinge o frete grátis
def test_ct07_soma_itens_diferentes_atinge_frete_gratis():
    # 1 item de R$ 100,00 e 2 itens de R$ 75,00 -> subtotal R$ 250,00 (frete grátis) = R$ 250,00
    assert fechar_pedido([(100.00, 1), (75.00, 2)]) == 250.00


# CT-08 — Carrinho vazio propaga o erro do frete
def test_ct08_carrinho_vazio_propaga_erro_frete():
    # Lista de itens vazia -> subtotal R$ 0,00 -> erro ValueError("Valor de carrinho inválido")
    with pytest.raises(ValueError, match="Valor de carrinho inválido"):
        fechar_pedido([])
