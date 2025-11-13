"""
Tests para Ejercicio 8: Generar Secuencia de Números con range()

Estos tests verifican que uses range() correctamente.
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
    return os.path.join(ejercicios_dir, 'GenerarSecuenciaNumeros.py')

class TestGenerarSecuenciaNumeros(unittest.TestCase):
    """Tests para verificar el Ejercicio 8"""
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['0', '10', '2'])
    def test_secuencia_paso_2(self, mock_input, mock_stdout):
        """Prueba con paso 2"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            # Debe contener números pares
            self.assertIn('0', output or '2', output or '4', output, 
                         "Debe mostrar números de la secuencia")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['5', '20', '3'])
    def test_secuencia_paso_3(self, mock_input, mock_stdout):
        """Prueba con paso 3"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            # Debe contener números de la secuencia
            self.assertIn('5', output or '8', output or '11', output, 
                         "Debe mostrar números de la secuencia")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")

if __name__ == '__main__':
    print("=" * 70)
    print("TESTS PARA EJERCICIO 8: Generar Secuencia de Números")
    print("=" * 70)
    unittest.main(verbosity=2)

