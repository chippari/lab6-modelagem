import pytest

try:
    from frete import calcular_total
except ImportError:
    from src.frete import calcular_total


# CT-01 — Frete padrão (REQ-01)
def test_ct01_frete_padrao():
    assert calcular_total(100.00, "Sudeste") == 115.00


# CT-02 — Frete grátis no limite (REQ-02)
def test_ct02_frete_gratis_no_limite():
    assert calcular_total(250.00) == 250.00
    assert calcular_total(249.99) == 264.99


# CT-03 — Carrinho com valor inválido (REQ-03)
def test_ct03_carrinho_com_valor_invalido():
    with pytest.raises(ValueError, match="Valor de carrinho inválido"):
        calcular_total(0.00)


# CT-04 — Adicional da região Norte (REQ-04)
def test_ct04_adicional_regiao_norte():
    assert calcular_total(100.00, "Norte") == 125.00


# CT-05 — Arredondamento em 2 casas (REQ-05)
def test_ct05_arredondamento_em_duas_casas():
    assert calcular_total(10.126) == 25.13
