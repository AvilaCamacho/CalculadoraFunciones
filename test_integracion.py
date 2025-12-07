#!/usr/bin/env python3
"""
Script de demostración interactiva que simula el uso del programa principal
sin requerir entrada manual del usuario.
"""

import sys
import os
from io import StringIO

# Agregar el directorio actual al path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from calculadora_3d import get_user_input, parse_function, calculate_volume, plot_surface_3d
import matplotlib.pyplot as plt


def simulate_user_input(input_text):
    """Simula entrada del usuario para pruebas."""
    return StringIO(input_text)


def test_interactive_flow():
    """
    Prueba el flujo interactivo completo con entrada simulada.
    """
    print("=" * 60)
    print("PRUEBA DE FLUJO INTERACTIVO")
    print("=" * 60)
    print()
    
    # Simular entrada del usuario para la función x**2 + y**2
    # en el dominio [-1, 1] x [-1, 1]
    input_data = "x**2 + y**2\n-1\n1\n-1\n1\n"
    
    # Guardar stdin original
    original_stdin = sys.stdin
    
    try:
        # Reemplazar stdin con entrada simulada
        sys.stdin = StringIO(input_data)
        
        # Obtener entrada del usuario
        func_str, a, b, c, d = get_user_input()
        
        print(f"\nEntrada capturada:")
        print(f"  Función: {func_str}")
        print(f"  Dominio: [{a}, {b}] x [{c}, {d}]")
        
        # Verificar que los valores sean correctos
        assert func_str == "x**2 + y**2", "Error en la función"
        assert a == -1 and b == 1, "Error en límites de x"
        assert c == -1 and d == 1, "Error en límites de y"
        
        # Parsear función
        func = parse_function(func_str)
        
        # Calcular volumen
        volume, error = calculate_volume(func, a, b, c, d)
        
        # El volumen esperado para x² + y² en [-1,1]×[-1,1] es:
        # ∫₋₁¹ ∫₋₁¹ (x² + y²) dy dx = ∫₋₁¹ [x²y + y³/3]₋₁¹ dx
        # = ∫₋₁¹ (2x² + 2/3) dx = [2x³/3 + 2x/3]₋₁¹
        # = (2/3 + 2/3) - (-2/3 - 2/3) = 4/3 + 4/3 = 8/3 ≈ 2.6667
        expected_volume = 8.0 / 3.0
        
        print(f"\nVolumen calculado: {volume:.6f}")
        print(f"Volumen esperado: {expected_volume:.6f}")
        print(f"Error: {abs(volume - expected_volume):.2e}")
        
        assert abs(volume - expected_volume) < 1e-6, "Error en cálculo de volumen"
        
        print("\n✓ Flujo interactivo funciona correctamente")
        
        return True
        
    finally:
        # Restaurar stdin original
        sys.stdin = original_stdin


def test_error_handling():
    """
    Prueba el manejo de errores con entradas inválidas.
    """
    print("\n" + "=" * 60)
    print("PRUEBA DE MANEJO DE ERRORES")
    print("=" * 60)
    print()
    
    # Probar función con logaritmo de negativo
    print("Test 1: Función con logaritmo de número negativo...")
    try:
        func = parse_function("log(x)")
        # Esto debería fallar para valores negativos de x
        from calculadora_3d import plot_surface_3d
        plot_surface_3d(func, -2, -1, 0, 1)
        print("✗ Debería haber detectado valores NaN/infinitos")
        return False
    except ValueError as e:
        print(f"✓ Error detectado correctamente: {str(e)[:60]}...")
    
    # Probar función con raíz cuadrada de negativo
    print("\nTest 2: Función con raíz cuadrada de negativo...")
    try:
        func = parse_function("sqrt(x)")
        # Esto debería fallar para valores negativos de x
        from calculadora_3d import plot_surface_3d
        plot_surface_3d(func, -2, -1, 0, 1)
        print("✗ Debería haber detectado valores NaN")
        return False
    except ValueError as e:
        print(f"✓ Error detectado correctamente: {str(e)[:60]}...")
    
    print("\n✓ Manejo de errores funciona correctamente")
    return True


def main():
    """Ejecuta todas las pruebas de integración."""
    print("=" * 60)
    print("PRUEBAS DE INTEGRACIÓN")
    print("=" * 60)
    print()
    
    try:
        # Ejecutar pruebas
        test_interactive_flow()
        test_error_handling()
        
        print("\n" + "=" * 60)
        print("TODAS LAS PRUEBAS DE INTEGRACIÓN PASARON ✓")
        print("=" * 60)
        return 0
        
    except Exception as e:
        print(f"\n✗ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
