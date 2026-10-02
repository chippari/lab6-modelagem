from decimal import Decimal

import pytest

from frete import calcular_total


# REQ-01
def test_adiciona_frete_padrao_ao_subtotal():
    assert calcular_total(Decimal("100.00")) == Decimal("115.00")


# REQ-02
@pytest.mark.parametrize("subtotal", [Decimal("200.00"), Decimal("250.00")])
def test_concede_frete_gratis_a_partir_de_duzentos_reais(subtotal):
    assert calcular_total(subtotal) == subtotal

# REQ-01: fronteira — um centavo abaixo do limite ainda paga frete
def test_um_centavo_abaixo_do_limite_paga_frete():
    assert calcular_total(Decimal("199.99")) == Decimal("214.99")
