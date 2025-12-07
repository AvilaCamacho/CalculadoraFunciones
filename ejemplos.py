#!/usr/bin/env python3
"""
Script de ejemplo que demuestra el uso de la calculadora 3D
con funciones predefinidas para pruebas rápidas.
"""

import sys
import os
import numpy as np

# Agregar el directorio actual al path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from calculadora_3d import parse_function, calculate_volume, plot_surface_3d
import matplotlib.pyplot as plt


def demo_paraboloid():
    """Ejemplo: Paraboloide z = x² + y²"""
    print("\n" + "="*60)
    print("EJEMPLO 1: PARABOLOIDE")
    print("="*60)
    
    func_str = "x**2 + y**2"
    a, b, c, d = -2, 2, -2, 2
    
    print(f"Función: z = {func_str}")
    print(f"Dominio: [{a}, {b}] x [{c}, {d}]")
    
    func = parse_function(func_str)
    volume, error = calculate_volume(func, a, b, c, d)
    
    print(f"\nVolumen calculado: {volume:.6f}")
    print(f"Error estimado: {error:.2e}")
    
    fig = plot_surface_3d(func, a, b, c, d)
    plt.figtext(0.5, 0.02, f'Volumen = {volume:.6f}', 
               ha='center', fontsize=12, bbox=dict(boxstyle='round', 
               facecolor='wheat', alpha=0.5))
    plt.savefig('ejemplo_paraboloide.png', dpi=150, bbox_inches='tight')
    print("Gráfico guardado como: ejemplo_paraboloide.png")
    plt.close()


def demo_gaussian():
    """Ejemplo: Campana gaussiana z = exp(-(x² + y²))"""
    print("\n" + "="*60)
    print("EJEMPLO 2: CAMPANA GAUSSIANA")
    print("="*60)
    
    func_str = "exp(-(x**2 + y**2))"
    a, b, c, d = -2, 2, -2, 2
    
    print(f"Función: z = {func_str}")
    print(f"Dominio: [{a}, {b}] x [{c}, {d}]")
    
    func = parse_function(func_str)
    volume, error = calculate_volume(func, a, b, c, d)
    
    print(f"\nVolumen calculado: {volume:.6f}")
    print(f"Error estimado: {error:.2e}")
    
    fig = plot_surface_3d(func, a, b, c, d)
    plt.figtext(0.5, 0.02, f'Volumen = {volume:.6f}', 
               ha='center', fontsize=12, bbox=dict(boxstyle='round', 
               facecolor='wheat', alpha=0.5))
    plt.savefig('ejemplo_gaussiana.png', dpi=150, bbox_inches='tight')
    print("Gráfico guardado como: ejemplo_gaussiana.png")
    plt.close()


def demo_sine_waves():
    """Ejemplo: Ondas sinusoidales z = sin(x) * cos(y)"""
    print("\n" + "="*60)
    print("EJEMPLO 3: ONDAS SINUSOIDALES")
    print("="*60)
    
    func_str = "sin(x) * cos(y)"
    a, b, c, d = 0, 2*np.pi, 0, 2*np.pi
    
    print(f"Función: z = {func_str}")
    print(f"Dominio: [{a:.2f}, {b:.2f}] x [{c:.2f}, {d:.2f}]")
    
    func = parse_function(func_str)
    volume, error = calculate_volume(func, a, b, c, d)
    
    print(f"\nVolumen calculado: {volume:.6f}")
    print(f"Error estimado: {error:.2e}")
    
    fig = plot_surface_3d(func, a, b, c, d)
    plt.figtext(0.5, 0.02, f'Volumen = {volume:.6f}', 
               ha='center', fontsize=12, bbox=dict(boxstyle='round', 
               facecolor='wheat', alpha=0.5))
    plt.savefig('ejemplo_ondas.png', dpi=150, bbox_inches='tight')
    print("Gráfico guardado como: ejemplo_ondas.png")
    plt.close()


def demo_saddle():
    """Ejemplo: Silla de montar z = x² - y²"""
    print("\n" + "="*60)
    print("EJEMPLO 4: SILLA DE MONTAR (SADDLE)")
    print("="*60)
    
    func_str = "x**2 - y**2"
    a, b, c, d = -2, 2, -2, 2
    
    print(f"Función: z = {func_str}")
    print(f"Dominio: [{a}, {b}] x [{c}, {d}]")
    
    func = parse_function(func_str)
    volume, error = calculate_volume(func, a, b, c, d)
    
    print(f"\nVolumen calculado: {volume:.6f}")
    print(f"Error estimado: {error:.2e}")
    
    fig = plot_surface_3d(func, a, b, c, d)
    plt.figtext(0.5, 0.02, f'Volumen = {volume:.6f}', 
               ha='center', fontsize=12, bbox=dict(boxstyle='round', 
               facecolor='wheat', alpha=0.5))
    plt.savefig('ejemplo_saddle.png', dpi=150, bbox_inches='tight')
    print("Gráfico guardado como: ejemplo_saddle.png")
    plt.close()


def main():
    """Ejecuta todos los ejemplos."""
    print("=" * 60)
    print("EJEMPLOS DE USO - CALCULADORA 3D")
    print("=" * 60)
    print("\nGenerando ejemplos y guardando gráficos...")
    
    try:
        demo_paraboloid()
        demo_gaussian()
        demo_sine_waves()
        demo_saddle()
        
        print("\n" + "="*60)
        print("TODOS LOS EJEMPLOS COMPLETADOS")
        print("="*60)
        print("\nSe han generado los siguientes archivos:")
        print("  - ejemplo_paraboloide.png")
        print("  - ejemplo_gaussiana.png")
        print("  - ejemplo_ondas.png")
        print("  - ejemplo_saddle.png")
        print("\nPuede ver estos archivos para observar los resultados.")
        
    except Exception as e:
        print(f"\nError al ejecutar ejemplos: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
