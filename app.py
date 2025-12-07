#!/usr/bin/env python3
"""
Aplicación web Flask para el Visualizador 3D y Calculadora de Volumen.
Expone la funcionalidad de calculadora_3d.py a través de una interfaz web.
"""

from flask import Flask, render_template, request, jsonify
import numpy as np
from calculadora_3d import parse_function, calculate_volume

app = Flask(__name__)

# Límite máximo de resolución para evitar payloads enormes
MAX_RESOLUTION = 150


@app.route('/')
def index():
    """
    Ruta principal que sirve la página HTML con el formulario.
    """
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    """
    Ruta POST que recibe datos del formulario, calcula el volumen
    y genera los datos para el gráfico 3D.
    
    Espera JSON con:
    - function: string con la función z = f(x,y)
    - a, b, c, d: floats con los límites del dominio
    - resolution: int con el número de puntos para el gráfico
    
    Retorna JSON con:
    - volume: volumen calculado
    - error: error estimado
    - x, y, z: arrays para el gráfico 3D (listas)
    - success: bool indicando éxito
    - message: mensaje de error en caso de fallo
    """
    try:
        # Obtener datos del request
        data = request.get_json()
        
        # Validar que se recibieron todos los campos
        required_fields = ['function', 'a', 'b', 'c', 'd', 'resolution']
        for field in required_fields:
            if field not in data:
                return jsonify({
                    'success': False,
                    'message': f'Falta el campo requerido: {field}'
                }), 400
        
        # Extraer y validar parámetros
        func_str = data['function'].strip()
        if not func_str:
            return jsonify({
                'success': False,
                'message': 'La función no puede estar vacía'
            }), 400
        
        try:
            a = float(data['a'])
            b = float(data['b'])
            c = float(data['c'])
            d = float(data['d'])
            resolution = int(data['resolution'])
        except (ValueError, TypeError) as e:
            return jsonify({
                'success': False,
                'message': f'Error en los parámetros numéricos: {str(e)}'
            }), 400
        
        # Validar dominio
        if a >= b:
            return jsonify({
                'success': False,
                'message': 'Debe cumplirse a < b'
            }), 400
        
        if c >= d:
            return jsonify({
                'success': False,
                'message': 'Debe cumplirse c < d'
            }), 400
        
        # Validar resolución
        if resolution < 10:
            return jsonify({
                'success': False,
                'message': 'La resolución debe ser al menos 10'
            }), 400
        
        if resolution > MAX_RESOLUTION:
            return jsonify({
                'success': False,
                'message': f'La resolución máxima permitida es {MAX_RESOLUTION}'
            }), 400
        
        # Parsear la función
        try:
            func = parse_function(func_str)
        except Exception as e:
            return jsonify({
                'success': False,
                'message': f'Error al parsear la función: {str(e)}'
            }), 400
        
        # Validar función con un punto de prueba
        try:
            test_val = func((a + b) / 2, (c + d) / 2)
            if not np.isfinite(test_val):
                return jsonify({
                    'success': False,
                    'message': 'La función produce valores no finitos en el dominio'
                }), 400
        except Exception as e:
            return jsonify({
                'success': False,
                'message': f'Error al evaluar la función: {str(e)}'
            }), 400
        
        # Calcular volumen
        try:
            volume, error = calculate_volume(func, a, b, c, d)
        except Exception as e:
            return jsonify({
                'success': False,
                'message': f'Error al calcular el volumen: {str(e)}'
            }), 500
        
        # Generar datos para el gráfico 3D
        try:
            x = np.linspace(a, b, resolution)
            y = np.linspace(c, d, resolution)
            X, Y = np.meshgrid(x, y)
            Z = func(X, Y)
            
            # Verificar que no haya valores infinitos o NaN
            if not np.all(np.isfinite(Z)):
                return jsonify({
                    'success': False,
                    'message': 'La función produce valores no finitos (infinito o NaN) en el dominio'
                }), 400
            
            # Convertir a listas para serialización JSON
            x_list = X.tolist()
            y_list = Y.tolist()
            z_list = Z.tolist()
            
        except Exception as e:
            return jsonify({
                'success': False,
                'message': f'Error al generar datos del gráfico: {str(e)}'
            }), 500
        
        # Retornar resultados
        return jsonify({
            'success': True,
            'volume': float(volume),
            'error': float(error),
            'x': x_list,
            'y': y_list,
            'z': z_list,
            'message': 'Cálculo completado exitosamente'
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error inesperado: {str(e)}'
        }), 500


if __name__ == '__main__':
    app.run(debug=True)
