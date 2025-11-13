"""
Tests para Ejercicio 6: Manejo de Excepciones - División

Estos tests verifican que tu manejo de excepciones funcione correctamente.
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
    return os.path.join(ejercicios_dir, 'ManejoExcepcionesDivision.py')

class TestManejoExcepcionesDivision(unittest.TestCase):
    """Tests para verificar el Ejercicio 6"""
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['10', '2'])
    def test_division_normal(self, mock_input, mock_stdout):
        """Prueba división normal"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('5', output, "10 / 2 debe ser 5")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['10', '0'])
    def test_division_por_cero(self, mock_input, mock_stdout):
        """Prueba división por cero"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            # Debe manejar el error sin crashear
            self.assertIn('cero', output.lower() or 'zero', output.lower(), 
                         "Debe mostrar mensaje de error por división por cero")
        except ZeroDivisionError:
            self.fail("Debes usar try/except para manejar ZeroDivisionError")
        except Exception as e:
            # Si es otro error, está bien siempre que no sea ZeroDivisionError sin manejar
            pass
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['abc', '2'])
    def test_valor_invalido(self, mock_input, mock_stdout):
        """Prueba con valor inválido"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            # Debe manejar el error sin crashear
            self.assertTrue(len(output) > 0, "Debe manejar el error sin crashear")
        except ValueError:
            self.fail("Debes usar try/except para manejar ValueError")
        except Exception as e:
            # Si es otro error, está bien siempre que no sea ValueError sin manejar
            pass

if __name__ == '__main__':
    print("=" * 70)
    print("TESTS PARA EJERCICIO 6: Manejo de Excepciones - División")
    print("=" * 70)
    unittest.main(verbosity=2)

