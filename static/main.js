/**
 * JavaScript para la aplicación web de Calculadora 3D
 * Maneja el formulario, comunicación con el servidor y visualización con Plotly
 */

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('calculator-form');
    const calculateBtn = document.getElementById('calculate-btn');
    const loadingDiv = document.getElementById('loading');
    const resultsDiv = document.getElementById('results');
    const errorDiv = document.getElementById('error-message');
    const plotContainer = document.getElementById('plot-container');
    
    // Manejar el envío del formulario
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        calculateAndPlot();
    });
    
    /**
     * Función principal que obtiene los datos del formulario,
     * hace la petición al servidor y renderiza el gráfico
     */
    async function calculateAndPlot() {
        // Ocultar mensajes previos
        hideMessages();
        
        // Mostrar indicador de carga
        loadingDiv.style.display = 'block';
        calculateBtn.disabled = true;
        
        // Obtener datos del formulario
        const formData = {
            function: document.getElementById('function').value,
            a: parseFloat(document.getElementById('a').value),
            b: parseFloat(document.getElementById('b').value),
            c: parseFloat(document.getElementById('c').value),
            d: parseFloat(document.getElementById('d').value),
            resolution: parseInt(document.getElementById('resolution').value)
        };
        
        try {
            // Hacer petición POST al servidor
            const response = await fetch('/calculate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(formData)
            });
            
            const data = await response.json();
            
            if (!response.ok || !data.success) {
                throw new Error(data.message || 'Error al procesar la solicitud');
            }
            
            // Mostrar resultados
            displayResults(data);
            
            // Crear gráfico 3D con Plotly
            createPlot(data, formData.function);
            
        } catch (error) {
            showError(error.message);
        } finally {
            // Ocultar indicador de carga
            loadingDiv.style.display = 'none';
            calculateBtn.disabled = false;
        }
    }
    
    /**
     * Muestra los resultados del cálculo (volumen y error)
     */
    function displayResults(data) {
        document.getElementById('volume-value').textContent = data.volume.toFixed(6);
        document.getElementById('error-value').textContent = data.error.toExponential(2);
        resultsDiv.style.display = 'block';
    }
    
    /**
     * Crea y renderiza el gráfico 3D usando Plotly
     */
    function createPlot(data, functionStr) {
        // Crear datos para el surface plot
        const plotData = [{
            type: 'surface',
            x: data.x,
            y: data.y,
            z: data.z,
            colorscale: 'Viridis',
            showscale: true,
            colorbar: {
                title: 'z',
                titleside: 'right'
            },
            contours: {
                z: {
                    show: true,
                    usecolormap: true,
                    highlightcolor: "#42f462",
                    project: { z: true }
                }
            }
        }];
        
        // Configurar el layout del gráfico
        const layout = {
            title: {
                text: `Superficie z = ${functionStr}`,
                font: {
                    size: 20,
                    family: 'Arial, sans-serif'
                }
            },
            autosize: true,
            height: 600,
            scene: {
                xaxis: {
                    title: 'X',
                    gridcolor: 'rgb(255, 255, 255)',
                    showbackground: true,
                    backgroundcolor: 'rgb(230, 230,230)'
                },
                yaxis: {
                    title: 'Y',
                    gridcolor: 'rgb(255, 255, 255)',
                    showbackground: true,
                    backgroundcolor: 'rgb(230, 230,230)'
                },
                zaxis: {
                    title: 'Z',
                    gridcolor: 'rgb(255, 255, 255)',
                    showbackground: true,
                    backgroundcolor: 'rgb(230, 230,230)'
                },
                camera: {
                    eye: {
                        x: 1.5,
                        y: 1.5,
                        z: 1.3
                    }
                }
            },
            margin: {
                l: 0,
                r: 0,
                b: 0,
                t: 40
            }
        };
        
        // Configuración adicional
        const config = {
            responsive: true,
            displayModeBar: true,
            displaylogo: false,
            modeBarButtonsToRemove: ['lasso2d', 'select2d']
        };
        
        // Renderizar el gráfico
        Plotly.newPlot(plotContainer, plotData, layout, config);
    }
    
    /**
     * Muestra un mensaje de error
     */
    function showError(message) {
        document.getElementById('error-text').textContent = message;
        errorDiv.style.display = 'block';
        
        // Limpiar el gráfico si existe
        plotContainer.innerHTML = '';
    }
    
    /**
     * Oculta todos los mensajes (error, resultados)
     */
    function hideMessages() {
        errorDiv.style.display = 'none';
        resultsDiv.style.display = 'none';
    }
});
