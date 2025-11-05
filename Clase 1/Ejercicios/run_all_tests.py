"""
Script para ejecutar todos los tests de las actividades
========================================================

Este script ejecuta automáticamente todos los tests para las 10 actividades.
Los alumnos pueden usar este script para verificar todas sus soluciones de una vez.

Uso:
    python run_all_tests.py
"""

import unittest
import sys
import os

def run_all_tests():
    """Ejecuta todos los tests de las actividades."""
    
    print("=" * 70)
    print("EJECUTANDO TODOS LOS TESTS DE LAS ACTIVIDADES")
    print("=" * 70)
    print()
    
    # Asegurar que estamos en el directorio correcto
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Descubrir todos los tests
    loader = unittest.TestLoader()
    start_dir = '.'
    pattern = 'test_actividad_*.py'
    
    suite = loader.discover(start_dir, pattern=pattern)
    
    # Ejecutar los tests con verbosidad
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Mostrar resumen
    print()
    print("=" * 70)
    print("RESUMEN DE RESULTADOS")
    print("=" * 70)
    print(f"Tests ejecutados: {result.testsRun}")
    print(f"Tests exitosos: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Tests fallidos: {len(result.failures)}")
    print(f"Errores: {len(result.errors)}")
    print()
    
    if result.wasSuccessful():
        print("✅ ¡FELICITACIONES! Todos los tests pasaron correctamente.")
        print("   Has completado exitosamente todas las actividades.")
    else:
        print("⚠️  Algunos tests no pasaron.")
        print("   Revisa los mensajes de error arriba para ver qué necesitas corregir.")
        print()
        if result.failures:
            print(f"   Actividades con tests fallidos: {len(result.failures)}")
        if result.errors:
            print(f"   Actividades con errores: {len(result.errors)}")
    
    print("=" * 70)
    print()
    
    # Retornar código de salida apropiado
    return 0 if result.wasSuccessful() else 1


def run_specific_test(activity_number):
    """Ejecuta el test de una actividad específica."""
    
    test_file = f'test_actividad_{activity_number}.py'
    
    if not os.path.exists(test_file):
        print(f"❌ Error: No se encontró el archivo {test_file}")
        return 1
    
    print("=" * 70)
    print(f"EJECUTANDO TESTS PARA ACTIVIDAD {activity_number}")
    print("=" * 70)
    print()
    
    loader = unittest.TestLoader()
    suite = loader.discover('.', pattern=test_file)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print()
    if result.wasSuccessful():
        print(f"✅ ¡Bien hecho! La actividad {activity_number} pasó todos los tests.")
    else:
        print(f"⚠️  La actividad {activity_number} tiene tests que no pasaron.")
        print("   Revisa los mensajes de error arriba.")
    print()
    
    return 0 if result.wasSuccessful() else 1


if __name__ == '__main__':
    # Si se proporciona un número de actividad, ejecutar solo ese test
    if len(sys.argv) > 1:
        try:
            activity_num = int(sys.argv[1])
            if 1 <= activity_num <= 10:
                sys.exit(run_specific_test(activity_num))
            else:
                print("❌ Error: El número de actividad debe estar entre 1 y 10")
                print("Uso: python run_all_tests.py [número_actividad]")
                print("Ejemplo: python run_all_tests.py 1")
                sys.exit(1)
        except ValueError:
            print("❌ Error: Debes proporcionar un número válido")
            print("Uso: python run_all_tests.py [número_actividad]")
            sys.exit(1)
    else:
        # Ejecutar todos los tests
        sys.exit(run_all_tests())

