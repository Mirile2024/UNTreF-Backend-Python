"""
Tests para Ejercicio 1: Función de Saludo

Estos tests verifican que tu función saludar funcione correctamente.
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
    return os.path.join(ejercicios_dir, 'FuncionSaludo.py')

class TestFuncionSaludo(unittest.TestCase):
    """Tests para verificar el Ejercicio 1"""
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', return_value='María')
    def test_saludo_nombre_simple(self, mock_input, mock_stdout):
        """Prueba con nombre simple"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('María', output, "El saludo debe incluir el nombre ingresado")
            self.assertIn('Hola', output, "El saludo debe contener 'Hola'")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', return_value='Juan')
    def test_saludo_nombre_juan(self, mock_input, mock_stdout):
        """Prueba con nombre 'Juan'"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('Juan', output, "El saludo debe incluir el nombre ingresado")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")

if __name__ == '__main__':
    print("=" * 70)
    print("TESTS PARA EJERCICIO 1: Función de Saludo")
    print("=" * 70)
    unittest.main(verbosity=2)

