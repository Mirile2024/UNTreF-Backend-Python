"""
Tests para Ejercicio 5: Funciones Lambda

Estos tests verifican que tus funciones lambda funcionen correctamente.
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
    return os.path.join(ejercicios_dir, 'FuncionesLambda.py')

class TestFuncionesLambda(unittest.TestCase):
    """Tests para verificar el Ejercicio 5"""
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', return_value='7')
    def test_funciones_lambda_numero_impar(self, mock_input, mock_stdout):
        """Prueba con número impar"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('14', output, "El doble de 7 debe ser 14")
            self.assertIn('impar', output.lower(), "7 es impar")
            self.assertIn('10', output, "Debe comparar con 10")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', return_value='8')
    def test_funciones_lambda_numero_par(self, mock_input, mock_stdout):
        """Prueba con número par"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('16', output, "El doble de 8 debe ser 16")
            self.assertIn('par', output.lower(), "8 es par")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")

if __name__ == '__main__':
    print("=" * 70)
    print("TESTS PARA EJERCICIO 5: Funciones Lambda")
    print("=" * 70)
    unittest.main(verbosity=2)

