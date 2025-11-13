"""
Tests para Ejercicio 4: Sumar Múltiples Números con *args

Estos tests verifican que tu función con *args funcione correctamente.
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
    return os.path.join(ejercicios_dir, 'SumarMultiplesNumeros.py')

class TestSumarMultiplesNumeros(unittest.TestCase):
    """Tests para verificar el Ejercicio 4"""
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', return_value='5, 10, 15, 20')
    def test_sumar_varios_numeros(self, mock_input, mock_stdout):
        """Prueba sumando varios números"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('50', output, "La suma de 5+10+15+20 debe ser 50")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', return_value='1, 2, 3')
    def test_sumar_tres_numeros(self, mock_input, mock_stdout):
        """Prueba sumando tres números"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('6', output, "La suma de 1+2+3 debe ser 6")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")

if __name__ == '__main__':
    print("=" * 70)
    print("TESTS PARA EJERCICIO 4: Sumar Múltiples Números")
    print("=" * 70)
    unittest.main(verbosity=2)

