# Guía de Uso - Calculadora 3D

## Inicio Rápido

### Instalación
```bash
# Clonar el repositorio
git clone https://github.com/AvilaCamacho/CalculadoraFunciones.git
cd CalculadoraFunciones

# Instalar dependencias
pip install -r requirements.txt
```

### Ejecución
```bash
python calculadora_3d.py
```

## Ejemplos de Uso

### Ejemplo 1: Paraboloide Simple
```
Función f(x, y) = x**2 + y**2
a (límite inferior de x) = -2
b (límite superior de x) = 2
c (límite inferior de y) = -2
d (límite superior de y) = 2

Resultado: Volumen ≈ 42.67
```

### Ejemplo 2: Campana Gaussiana
```
Función f(x, y) = exp(-(x**2 + y**2))
a (límite inferior de x) = -2
b (límite superior de x) = 2
c (límite inferior de y) = -2
d (límite superior de y) = 2

Resultado: Volumen ≈ 3.11
```

### Ejemplo 3: Ondas Sinusoidales
```
Función f(x, y) = sin(x) * cos(y)
a (límite inferior de x) = 0
b (límite superior de x) = 6.28
c (límite inferior de y) = 0
d (límite superior de y) = 6.28

Resultado: Volumen ≈ 0
```

## Funciones Matemáticas Disponibles

### Operadores Básicos
- `+` : Suma
- `-` : Resta
- `*` : Multiplicación
- `/` : División
- `**` : Potencia

### Funciones Trigonométricas
- `sin(x)` : Seno
- `cos(x)` : Coseno
- `tan(x)` : Tangente

### Funciones Exponenciales y Logarítmicas
- `exp(x)` : e^x
- `log(x)` : Logaritmo natural

### Otras Funciones
- `sqrt(x)` : Raíz cuadrada
- `abs(x)` : Valor absoluto

### Constantes
- `pi` : π ≈ 3.14159
- `e` : e ≈ 2.71828

## Ejemplos de Funciones Comunes

### Superficies Cuadráticas
```
x**2 + y**2           # Paraboloide circular
x**2 - y**2           # Silla de montar (saddle)
x**2 + 2*y**2         # Paraboloide elíptico
```

### Funciones Trigonométricas
```
sin(x) * cos(y)       # Producto de ondas
sin(x + y)            # Onda diagonal
cos(sqrt(x**2 + y**2)) # Ondas radiales
```

### Funciones Exponenciales
```
exp(-x**2 - y**2)     # Campana gaussiana
exp(x + y)            # Crecimiento exponencial
1 / (1 + x**2 + y**2) # Función de Cauchy 2D
```

### Funciones Combinadas
```
x**2 * y**2           # Producto de cuadrados
sin(x) + cos(y)       # Suma de ondas
x**2 * exp(-y)        # Parábola con decaimiento
```

## Pruebas

### Ejecutar Pruebas Unitarias
```bash
python test_calculadora.py
```

### Ejecutar Pruebas de Integración
```bash
python test_integracion.py
```

### Generar Ejemplos Visuales
```bash
python ejemplos.py
```
Esto generará archivos PNG con visualizaciones de ejemplo.

## Solución de Problemas

### Error: "La función produce valores no finitos"
**Causa**: La función evaluada produce valores infinitos o NaN en el dominio.

**Solución**: 
- Verifique que la función sea válida en todo el dominio
- Evite divisiones por cero
- Evite logaritmos de números negativos
- Evite raíces cuadradas de números negativos

**Ejemplo de error**:
```
Función: log(x)
Dominio: [-1, 1] x [-1, 1]  # Error: log de negativos
```

**Corrección**:
```
Función: log(x)
Dominio: [0.1, 2] x [0.1, 2]  # Solo valores positivos
```

### Error: "Debe cumplirse a < b"
**Causa**: Los límites del dominio están invertidos.

**Solución**: Asegúrese que a < b y c < d.

### Error: "Error al evaluar la función"
**Causa**: Sintaxis incorrecta en la función.

**Solución**: 
- Use `**` para potencias, no `^`
- Use paréntesis para aclarar precedencia
- Verifique que los nombres de funciones sean correctos

## Conceptos Matemáticos

### Volumen Bajo una Superficie
El volumen V bajo una superficie z = f(x,y) sobre una región rectangular R = [a,b] × [c,d] se calcula mediante la integral doble:

```
V = ∫∫_R f(x,y) dA = ∫_a^b ∫_c^d f(x,y) dy dx
```

### Método Numérico
La aplicación utiliza **cuadratura adaptativa de Gauss-Kronrod** implementada en `scipy.integrate.dblquad`, que:
- Divide automáticamente el dominio en subdominios
- Aplica fórmulas de cuadratura de alta precisión
- Estima el error de integración
- Es eficiente para funciones suaves

### Precisión
- La precisión típica es de 6-10 dígitos significativos
- El error estimado se reporta junto con el resultado
- Funciones con discontinuidades pueden tener menor precisión

## Limitaciones

1. **Dominio rectangular**: Solo soporta regiones rectangulares [a,b] × [c,d]
2. **Funciones continuas**: Mejores resultados con funciones suaves y continuas
3. **Sintaxis limitada**: Solo funciones matemáticas predefinidas
4. **Memoria**: Dominios muy grandes requieren más memoria para la visualización

## Referencias

- NumPy: https://numpy.org/
- Matplotlib: https://matplotlib.org/
- SciPy Integration: https://docs.scipy.org/doc/scipy/reference/integrate.html
