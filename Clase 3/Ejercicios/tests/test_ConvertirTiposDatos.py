"""
Tests para Ejercicio 10: Conversión de Tipos de Datos

Estos tests verifican que conviertas tipos de datos correctamente.
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
    return os.path.join(ejercicios_dir, 'ConvertirTiposDatos.py')

class TestConvertirTiposDatos(unittest.TestCase):
    """Tests para verificar el Ejercicio 10"""
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['100', '3.14', '42', '5'])
    def test_conversiones(self, mock_input, mock_stdout):
        """Prueba las conversiones de tipos"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            # Debe mostrar conversiones
            self.assertIn('100', output, "Debe mostrar el número entero")
            self.assertIn('3.14', output, "Debe mostrar el número flotante")
            self.assertIn('42', output, "Debe mostrar el número convertido a texto")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")

if __name__ == '__main__':
    print("=" * 70)
    print("TESTS PARA EJERCICIO 10: Conversión de Tipos de Datos")
    print("=" * 70)
    unittest.main(verbosity=2)

