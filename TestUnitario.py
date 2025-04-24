from decimal import Decimal
import unittest

# Generación de data para pruebas.
def calcular_total_compra(productos):
    total = Decimal('0.0')
    for producto in productos:
        total += Decimal(str(producto['precio'])) * Decimal(str(producto['cantidad']))
    return float(total)

# Define test cases
casos_de_prueba = [
    # ... otros casos de prueba ...
    {
        "productos": [
            {"precio": -10.99, "cantidad": 2},
            {"precio": 5.5, "cantidad": -3}
        ],
        "total_esperado": -38.48  # Valor corregido
    }
]

class TestCalcularTotalCompra(unittest.TestCase):
    def test_calcular_total_compra(self):
        for caso in casos_de_prueba:
            productos = caso["productos"]
            total_esperado = caso["total_esperado"]
            self.assertAlmostEqual(calcular_total_compra(productos), total_esperado, places=2)

if __name__ == "__main__":
    unittest.main()