#!/usr/bin/env python3
"""
Script de prueba para el visualizador 3D y calculadora de volumen.
Ejecuta casos de prueba con funciones conocidas.
"""

import numpy as np
import sys
import os

# Agregar el directorio actual al path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from calculadora_3d import parse_function, calculate_volume


def test_parse_function():
    """Prueba el parser de funciones."""
    print("Test 1: Parseando funciones...")
    
    # Función simple
    f1 = parse_function("x + y")
    assert f1(2, 3) == 5, "Error en función simple"
    
    # Función cuadrática
    f2 = parse_function("x**2 + y**2")
    assert f2(3, 4) == 25, "Error en función cuadrática"
    
    # Función trigonométrica
    f3 = parse_function("sin(x) + cos(y)")
    result = f3(0, 0)
    assert abs(result - 1.0) < 1e-10, "Error en función trigonométrica"
    
    print("✓ Parser de funciones funciona correctamente\n")


def test_volume_calculation():
    """Prueba el cálculo de volúmenes con casos conocidos."""
    print("Test 2: Calculando volúmenes...")
    
    # Caso 1: función constante f(x,y) = 1 en [0,1] x [0,1]
    # Volumen esperado = 1 * 1 * 1 = 1
    f1 = parse_function("1")
    vol1, err1 = calculate_volume(f1, 0, 1, 0, 1)
    assert abs(vol1 - 1.0) < 1e-6, f"Error: esperado 1.0, obtenido {vol1}"
    print(f"  Caso 1 (constante): Volumen = {vol1:.6f} (esperado: 1.0) ✓")
    
    # Caso 2: función lineal f(x,y) = x en [0,2] x [0,1]
    # Volumen = ∫₀² ∫₀¹ x dy dx = ∫₀² x dx = [x²/2]₀² = 2
    f2 = parse_function("x")
    vol2, err2 = calculate_volume(f2, 0, 2, 0, 1)
    assert abs(vol2 - 2.0) < 1e-6, f"Error: esperado 2.0, obtenido {vol2}"
    print(f"  Caso 2 (lineal): Volumen = {vol2:.6f} (esperado: 2.0) ✓")
    
    # Caso 3: función cuadrática f(x,y) = x² en [0,1] x [0,1]
    # Volumen = ∫₀¹ ∫₀¹ x² dy dx = ∫₀¹ x² dx = [x³/3]₀¹ = 1/3
    f3 = parse_function("x**2")
    vol3, err3 = calculate_volume(f3, 0, 1, 0, 1)
    expected3 = 1.0 / 3.0
    assert abs(vol3 - expected3) < 1e-6, f"Error: esperado {expected3}, obtenido {vol3}"
    print(f"  Caso 3 (cuadrática): Volumen = {vol3:.6f} (esperado: {expected3:.6f}) ✓")
    
    # Caso 4: función de dos variables f(x,y) = x + y en [0,1] x [0,1]
    # Volumen = ∫₀¹ ∫₀¹ (x+y) dy dx = ∫₀¹ [xy + y²/2]₀¹ dx = ∫₀¹ (x + 1/2) dx = [x²/2 + x/2]₀¹ = 1
    f4 = parse_function("x + y")
    vol4, err4 = calculate_volume(f4, 0, 1, 0, 1)
    assert abs(vol4 - 1.0) < 1e-6, f"Error: esperado 1.0, obtenido {vol4}"
    print(f"  Caso 4 (dos variables): Volumen = {vol4:.6f} (esperado: 1.0) ✓")
    
    print("\n✓ Cálculo de volúmenes funciona correctamente\n")


def test_special_functions():
    """Prueba funciones especiales (trigonométricas, exponenciales)."""
    print("Test 3: Funciones especiales...")
    
    # Función exponencial
    f1 = parse_function("exp(-(x**2 + y**2))")
    vol1, err1 = calculate_volume(f1, -1, 1, -1, 1)
    print(f"  Gaussiana 2D: Volumen = {vol1:.6f} ✓")
    
    # Función trigonométrica
    f2 = parse_function("sin(x) * cos(y)")
    vol2, err2 = calculate_volume(f2, 0, np.pi, 0, np.pi/2)
    # El volumen esperado es ∫₀^π sin(x) dx * ∫₀^(π/2) cos(y) dy = 2 * 1 = 2
    expected2 = 2.0
    assert abs(vol2 - expected2) < 1e-6, f"Error: esperado {expected2}, obtenido {vol2}"
    print(f"  Trigonométrica: Volumen = {vol2:.6f} (esperado: {expected2:.6f}) ✓")
    
    print("\n✓ Funciones especiales funcionan correctamente\n")


def run_all_tests():
    """Ejecuta todas las pruebas."""
    print("=" * 60)
    print("EJECUTANDO PRUEBAS DEL SISTEMA")
    print("=" * 60)
    print()
    
    try:
        test_parse_function()
        test_volume_calculation()
        test_special_functions()
        
        print("=" * 60)
        print("TODAS LAS PRUEBAS PASARON EXITOSAMENTE ✓")
        print("=" * 60)
        return 0
        
    except AssertionError as e:
        print(f"\n✗ PRUEBA FALLIDA: {e}")
        return 1
    except Exception as e:
        print(f"\n✗ ERROR INESPERADO: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(run_all_tests())
