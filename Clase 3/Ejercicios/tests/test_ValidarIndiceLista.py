"""
Tests para Ejercicio 7: Validar Índice de Lista con Excepciones

Estos tests verifican que tu manejo de excepciones con listas funcione correctamente.
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
    return os.path.join(ejercicios_dir, 'ValidarIndiceLista.py')

class TestValidarIndiceLista(unittest.TestCase):
    """Tests para verificar el Ejercicio 7"""
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', return_value='2')
    def test_indice_valido(self, mock_input, mock_stdout):
        """Prueba con índice válido"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            # Debe mostrar algún elemento de la lista
            self.assertTrue(len(output) > 0, "Debe mostrar el elemento")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', return_value='10')
    def test_indice_fuera_rango(self, mock_input, mock_stdout):
        """Prueba con índice fuera de rango"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            # Debe manejar el error sin crashear
            self.assertTrue(len(output) > 0, "Debe manejar el error sin crashear")
        except IndexError:
            self.fail("Debes usar try/except para manejar IndexError")
        except Exception as e:
            # Si es otro error, está bien siempre que no sea IndexError sin manejar
            pass
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', return_value='abc')
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
    print("TESTS PARA EJERCICIO 7: Validar Índice de Lista")
    print("=" * 70)
    unittest.main(verbosity=2)

