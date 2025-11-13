"""
Tests para Ejercicio 2: Calculadora Básica con Funciones

Estos tests verifican que tus funciones de calculadora funcionen correctamente.
"""

import unittest
from unittest.mock import patch
from io import StringIO
import sys
import os

def get_ejercicio_path():
    """Obtiene la ruta al archivo de ejercicio"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    ejercicios_dir = os.path.join(script_dir, '..', 'ejercicios')
    return os.path.join(ejercicios_dir, 'CalculadoraBasica.py')

class TestCalculadoraBasica(unittest.TestCase):
    """Tests para verificar el Ejercicio 2"""
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['10', '5', 'sumar'])
    def test_sumar(self, mock_input, mock_stdout):
        """Prueba la función sumar"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('15', output, "La suma de 10 + 5 debe ser 15")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['10', '5', 'restar'])
    def test_restar(self, mock_input, mock_stdout):
        """Prueba la función restar"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('5', output, "La resta de 10 - 5 debe ser 5")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['10', '5', 'multiplicar'])
    def test_multiplicar(self, mock_input, mock_stdout):
        """Prueba la función multiplicar"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('50', output, "La multiplicación de 10 * 5 debe ser 50")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")

if __name__ == '__main__':
    print("=" * 70)
    print("TESTS PARA EJERCICIO 2: Calculadora Básica")
    print("=" * 70)
    unittest.main(verbosity=2)

