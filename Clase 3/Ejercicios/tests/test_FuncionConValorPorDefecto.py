"""
Tests para Ejercicio 3: Función con Valor por Defecto

Estos tests verifican que tu función con valor por defecto funcione correctamente.
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
    return os.path.join(ejercicios_dir, 'FuncionConValorPorDefecto.py')

class TestFuncionConValorPorDefecto(unittest.TestCase):
    """Tests para verificar el Ejercicio 3"""
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['Juan', '25'])
    def test_con_edad(self, mock_input, mock_stdout):
        """Prueba con edad proporcionada"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('Juan', output, "Debe incluir el nombre")
            self.assertIn('25', output, "Debe incluir la edad proporcionada")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['Ana', ''])
    def test_sin_edad(self, mock_input, mock_stdout):
        """Prueba sin edad (debe usar valor por defecto)"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('Ana', output, "Debe incluir el nombre")
            self.assertIn('18', output, "Debe usar el valor por defecto 18")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")

if __name__ == '__main__':
    print("=" * 70)
    print("TESTS PARA EJERCICIO 3: Función con Valor por Defecto")
    print("=" * 70)
    unittest.main(verbosity=2)

