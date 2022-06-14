from tax_calculator import __version__
from tax_calculator import app


def test_version():
    assert __version__ == '0.1.0'

def test_calculate_sales_tax():
    expected = 104.0
    results = app.calculate_sales_tax(100, 4)
    assert expected == results
