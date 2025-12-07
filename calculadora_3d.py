#!/usr/bin/env python3
"""
Visualizador 3D y Calculadora de Volumen
Aplicación que acepta una función z = f(x, y), genera un gráfico 3D
y calcula el volumen bajo la superficie usando integración numérica.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy import integrate
import sys


def parse_function(func_str):
    """
    Convierte una cadena de texto en una función evaluable.
    
    Args:
        func_str: String con la expresión matemática (ej: "x**2 + y**2")
    
    Returns:
        Función que puede ser evaluada con valores x, y
    
    Nota de seguridad: Esta función usa eval() con un namespace restringido
    que solo incluye funciones matemáticas seguras. Para uso en producción,
    considere usar bibliotecas como sympy para parsing más robusto.
    """
    # Crear un namespace seguro con funciones matemáticas comunes
    safe_dict = {
        'sin': np.sin,
        'cos': np.cos,
        'tan': np.tan,
        'exp': np.exp,
        'log': np.log,
        'sqrt': np.sqrt,
        'abs': np.abs,
        'pi': np.pi,
        'e': np.e,
    }
    
    def f(x, y):
        safe_dict['x'] = x
        safe_dict['y'] = y
        try:
            return eval(func_str, {"__builtins__": {}}, safe_dict)
        except Exception as e:
            raise ValueError(f"Error al evaluar la función: {e}")
    
    return f


def plot_surface_3d(func, a, b, c, d, num_points=100):
    """
    Genera un gráfico 3D de la superficie z = f(x, y).
    
    Args:
        func: Función a graficar
        a, b: Límites del dominio en x [a, b]
        c, d: Límites del dominio en y [c, d]
        num_points: Número de puntos para el mallado
    """
    # Crear malla de puntos
    x = np.linspace(a, b, num_points)
    y = np.linspace(c, d, num_points)
    X, Y = np.meshgrid(x, y)
    
    # Evaluar la función en la malla
    try:
        Z = func(X, Y)
        # Verificar que no haya valores infinitos o NaN
        if not np.all(np.isfinite(Z)):
            raise ValueError("La función produce valores no finitos (infinito o NaN) en el dominio")
    except Exception as e:
        raise ValueError(f"Error al evaluar la función en el dominio: {e}")
    
    # Crear figura 3D
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Graficar superficie
    surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8, 
                           edgecolor='none', antialiased=True)
    
    # Configurar etiquetas y título
    ax.set_xlabel('X', fontsize=12)
    ax.set_ylabel('Y', fontsize=12)
    ax.set_zlabel('Z', fontsize=12)
    ax.set_title('Superficie z = f(x, y)', fontsize=14, fontweight='bold')
    
    # Agregar barra de color
    fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)
    
    # Mejorar visualización
    ax.view_init(elev=30, azim=45)
    
    return fig


def calculate_volume(func, a, b, c, d):
    """
    Calcula el volumen bajo la superficie z = f(x, y) usando integración numérica doble.
    
    Args:
        func: Función z = f(x, y)
        a, b: Límites del dominio en x [a, b]
        c, d: Límites del dominio en y [c, d]
    
    Returns:
        Volumen calculado y error estimado
    """
    # Usar scipy.integrate.dblquad para integración doble
    # dblquad(func, a, b, gfun, hfun) integra: ∫ₐᵇ ∫_{gfun(x)}^{hfun(x)} func(y, x) dy dx
    # Para límites constantes en y, usamos funciones lambda que retornan c y d
    
    def integrand(y, x):
        return func(x, y)
    
    volume, error = integrate.dblquad(
        integrand,
        a, b,      # límites de x
        lambda x: c,  # límite inferior de y (constante)
        lambda x: d   # límite superior de y (constante)
    )
    
    return volume, error


def get_user_input():
    """
    Obtiene los datos del usuario de manera interactiva.
    
    Returns:
        tuple: (función, a, b, c, d)
    """
    print("=" * 60)
    print("VISUALIZADOR 3D Y CALCULADORA DE VOLUMEN")
    print("=" * 60)
    print()
    
    # Obtener función
    print("Ingrese la función z = f(x, y)")
    print("Puede usar: +, -, *, /, **, sin, cos, tan, exp, log, sqrt, pi, e")
    print("Ejemplo: x**2 + y**2")
    print("Ejemplo: sin(x) * cos(y)")
    print("Ejemplo: exp(-x**2 - y**2)")
    func_str = input("\nFunción f(x, y) = ").strip()
    
    if not func_str:
        raise ValueError("Debe ingresar una función")
    
    # Obtener dominio
    print("\nIngrese el dominio rectangular [a, b] x [c, d]")
    
    try:
        a = float(input("a (límite inferior de x) = "))
        b = float(input("b (límite superior de x) = "))
        c = float(input("c (límite inferior de y) = "))
        d = float(input("d (límite superior de y) = "))
    except ValueError:
        raise ValueError("Los límites del dominio deben ser números")
    
    # Validar dominio
    if a >= b:
        raise ValueError("Debe cumplirse a < b")
    if c >= d:
        raise ValueError("Debe cumplirse c < d")
    
    return func_str, a, b, c, d


def main():
    """
    Función principal de la aplicación.
    """
    try:
        # Obtener entrada del usuario
        func_str, a, b, c, d = get_user_input()
        
        # Parsear función
        print("\nProcesando función...")
        func = parse_function(func_str)
        
        # Validar función con un punto de prueba
        try:
            test_val = func((a + b) / 2, (c + d) / 2)
            if not np.isfinite(test_val):
                raise ValueError("La función produce valores no finitos en el dominio")
        except Exception as e:
            raise ValueError(f"Error al evaluar la función en el dominio: {e}")
        
        print(f"Función: z = {func_str}")
        print(f"Dominio: [{a}, {b}] x [{c}, {d}]")
        print()
        
        # Calcular volumen
        print("Calculando volumen bajo la superficie...")
        volume, error = calculate_volume(func, a, b, c, d)
        
        print()
        print("=" * 60)
        print("RESULTADOS")
        print("=" * 60)
        print(f"Volumen calculado: {volume:.6f}")
        print(f"Error estimado: {error:.2e}")
        print()
        
        # Generar gráfico 3D
        print("Generando gráfico 3D...")
        fig = plot_surface_3d(func, a, b, c, d)
        
        # Agregar información del volumen al gráfico
        plt.figtext(0.5, 0.02, f'Volumen = {volume:.6f}', 
                   ha='center', fontsize=12, bbox=dict(boxstyle='round', 
                   facecolor='wheat', alpha=0.5))
        
        print("Mostrando gráfico...")
        print("Cierre la ventana del gráfico para finalizar.")
        plt.show()
        
        print("\n¡Proceso completado exitosamente!")
        
    except KeyboardInterrupt:
        print("\n\nOperación cancelada por el usuario.")
        sys.exit(0)
    except Exception as e:
        print(f"\nError: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
