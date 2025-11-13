"""
Tests para Ejercicio 9: Manipulación de Texto con Métodos de String

Estos tests verifican que uses los métodos de string correctamente.
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
    return os.path.join(ejercicios_dir, 'ManipularTexto.py')

class TestManipularTexto(unittest.TestCase):
    """Tests para verificar el Ejercicio 9"""
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', return_value='Hola mundo Python')
    def test_manipulacion_texto(self, mock_input, mock_stdout):
        """Prueba la manipulación de texto"""
        try:
            with open(get_ejercicio_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            # Debe mostrar mayúsculas
            self.assertIn('HOLA', output, "Debe mostrar la frase en mayúsculas")
            # Debe mostrar minúsculas
            self.assertIn('hola', output.lower(), "Debe mostrar la frase en minúsculas")
            # Debe mostrar información sobre palabras
            self.assertIn('3', output or 'palabra', output.lower(), 
                         "Debe mostrar el número de palabras")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")

if __name__ == '__main__':
    print("=" * 70)
    print("TESTS PARA EJERCICIO 9: Manipulación de Texto")
    print("=" * 70)
    unittest.main(verbosity=2)

