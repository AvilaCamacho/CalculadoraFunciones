#!/usr/bin/env python3
"""
Aplicación web Flask para visualización 3D y cálculo de volumen.
Permite a los usuarios introducir funciones z = f(x,y) y obtener
visualizaciones interactivas con Plotly.
"""

from flask import Flask, render_template, request, jsonify
import numpy as np
import plotly.graph_objects as go
import plotly.io as pio
import sys
import os

# Agregar el directorio padre al path para importar calculadora_3d
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from calculadora_3d import parse_function, calculate_volume

app = Flask(__name__)


@app.route('/')
def index():
    """Renderiza la página principal con el formulario."""
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    """
    Endpoint para calcular volumen y generar gráfico 3D.
    Acepta datos en formato form-encoded o JSON.
    
    Parámetros esperados:
    - function: Expresión matemática z = f(x,y)
    - a, b: Límites del dominio en x [a, b]
    - c, d: Límites del dominio en y [c, d]
    - num_points: Resolución de la malla (opcional, default 50)
    
    Retorna JSON con:
    - volume: Volumen calculado
    - error: Error estimado
    - plot_html: HTML div del gráfico Plotly
    O en caso de error:
    - error: Mensaje de error
    """
    try:
        # Obtener datos del request (form-encoded o JSON)
        if request.is_json:
            data = request.get_json()
        else:
            data = request.form
        
        # Extraer parámetros
        func_str = data.get('function', '').strip()
        
        # Validar que la función no esté vacía
        if not func_str:
            return jsonify({'error': 'La función no puede estar vacía'}), 400
        
        # Parsear límites del dominio
        try:
            a = float(data.get('a'))
            b = float(data.get('b'))
            c = float(data.get('c'))
            d = float(data.get('d'))
        except (ValueError, TypeError):
            return jsonify({'error': 'Los límites del dominio deben ser números válidos'}), 400
        
        # Validar dominio
        if a >= b:
            return jsonify({'error': 'Debe cumplirse a < b'}), 400
        if c >= d:
            return jsonify({'error': 'Debe cumplirse c < d'}), 400
        
        # Obtener resolución (limitada a 20-200)
        try:
            num_points = int(data.get('num_points', 50))
            num_points = max(20, min(200, num_points))
        except (ValueError, TypeError):
            num_points = 50
        
        # Parsear función usando la función existente
        try:
            func = parse_function(func_str)
        except Exception as e:
            return jsonify({'error': f'Error al parsear la función: {str(e)}'}), 400
        
        # Validar función con un punto de prueba
        try:
            test_val = func((a + b) / 2, (c + d) / 2)
            if not np.isfinite(test_val):
                return jsonify({'error': 'La función produce valores no finitos en el dominio'}), 400
        except Exception as e:
            return jsonify({'error': f'Error al evaluar la función: {str(e)}'}), 400
        
        # Calcular volumen usando la función existente
        try:
            volume, error = calculate_volume(func, a, b, c, d)
        except Exception as e:
            return jsonify({'error': f'Error al calcular el volumen: {str(e)}'}), 500
        
        # Generar superficie 3D con Plotly
        try:
            # Crear meshgrid
            x = np.linspace(a, b, num_points)
            y = np.linspace(c, d, num_points)
            X, Y = np.meshgrid(x, y)
            
            # Evaluar función
            Z = func(X, Y)
            
            # Verificar valores finitos
            if not np.all(np.isfinite(Z)):
                # Reemplazar valores no finitos con NaN para visualización
                Z = np.where(np.isfinite(Z), Z, np.nan)
            
            # Crear figura Plotly
            fig = go.Figure(data=[go.Surface(
                x=X,
                y=Y,
                z=Z,
                colorscale='Viridis',
                showscale=True,
                hovertemplate='x: %{x:.3f}<br>y: %{y:.3f}<br>z: %{z:.3f}<extra></extra>'
            )])
            
            # Configurar layout
            fig.update_layout(
                title={
                    'text': f'Superficie z = {func_str}',
                    'x': 0.5,
                    'xanchor': 'center'
                },
                scene=dict(
                    xaxis_title='X',
                    yaxis_title='Y',
                    zaxis_title='Z',
                    camera=dict(
                        eye=dict(x=1.5, y=1.5, z=1.3)
                    )
                ),
                autosize=True,
                margin=dict(l=0, r=0, t=40, b=0),
                height=600
            )
            
            # Convertir a HTML div (sin incluir Plotly.js ya que se carga desde CDN)
            plot_html = pio.to_html(fig, include_plotlyjs=False, full_html=False)
            
        except Exception as e:
            return jsonify({'error': f'Error al generar el gráfico: {str(e)}'}), 500
        
        # Retornar resultados
        return jsonify({
            'volume': float(volume),
            'error': float(error),
            'plot_html': plot_html,
            'function': func_str,
            'domain': {
                'a': a,
                'b': b,
                'c': c,
                'd': d
            }
        })
        
    except Exception as e:
        # Error genérico no capturado
        return jsonify({'error': f'Error inesperado: {str(e)}'}), 500


if __name__ == '__main__':
    app.run(debug=True)
