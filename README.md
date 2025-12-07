# CalculadoraFunciones

Visualizador 3D y Calculadora de Volumen - Aplicación Python para graficar superficies 3D y calcular volúmenes bajo ellas usando integración numérica.

## 📋 Descripción

Esta aplicación permite:
- ✅ Aceptar una función matemática z = f(x, y) del usuario
- ✅ Definir un dominio rectangular [a, b] x [c, d]
- ✅ Generar un gráfico 3D interactivo de la superficie
- ✅ Calcular el volumen bajo la superficie usando integración doble numérica

## 🚀 Instalación

### Requisitos previos
- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Pasos de instalación

1. Clone el repositorio:
```bash
git clone https://github.com/AvilaCamacho/CalculadoraFunciones.git
cd CalculadoraFunciones
```

2. Instale las dependencias:
```bash
pip install -r requirements.txt
```

## 💻 Uso

### Ejecución del programa

```bash
python calculadora_3d.py
```

### Ejemplo de uso interactivo

```
============================================================
VISUALIZADOR 3D Y CALCULADORA DE VOLUMEN
============================================================

Ingrese la función z = f(x, y)
Puede usar: +, -, *, /, **, sin, cos, tan, exp, log, sqrt, pi, e
Ejemplo: x**2 + y**2
Ejemplo: sin(x) * cos(y)
Ejemplo: exp(-x**2 - y**2)

Función f(x, y) = x**2 + y**2

Ingrese el dominio rectangular [a, b] x [c, d]
a (límite inferior de x) = -2
b (límite superior de x) = 2
c (límite inferior de y) = -2
d (límite superior de y) = 2

Procesando función...
Función: z = x**2 + y**2
Dominio: [-2, 2] x [-2, 2]

Calculando volumen bajo la superficie...

============================================================
RESULTADOS
============================================================
Volumen calculado: 42.666667
Error estimado: 4.74e-13

Generando gráfico 3D...
Mostrando gráfico...
```

## 📝 Ejemplos de funciones

### Funciones básicas
- `x**2 + y**2` - Paraboloide
- `x + y` - Plano inclinado
- `x * y` - Silla de montar (saddle)
- `1` - Plano constante

### Funciones trigonométricas
- `sin(x) * cos(y)` - Ondas en 2D
- `sin(sqrt(x**2 + y**2))` - Ondas radiales
- `cos(x) + sin(y)` - Suma de ondas

### Funciones exponenciales
- `exp(-x**2 - y**2)` - Campana gaussiana 2D
- `exp(-(x**2 + y**2)/2)` - Distribución normal
- `1 / (1 + x**2 + y**2)` - Función racional

### Funciones combinadas
- `x**2 - y**2` - Paraboloide hiperbólico
- `sin(x) + cos(y)` - Superficies onduladas
- `sqrt(abs(x * y))` - Raíces con valores absolutos

## 🧪 Pruebas

Para ejecutar las pruebas del sistema:

```bash
python test_calculadora.py
```

Las pruebas verifican:
- Correcto parsing de funciones matemáticas
- Precisión en el cálculo de volúmenes con casos conocidos
- Manejo de funciones especiales (trigonométricas, exponenciales)

## 🛠️ Tecnologías utilizadas

- **NumPy**: Cálculos numéricos y manejo de arrays
- **Matplotlib**: Visualización 3D de superficies
- **SciPy**: Integración numérica doble para cálculo de volumen

## 📚 Conceptos matemáticos

### Integración doble
El volumen bajo una superficie z = f(x, y) sobre un dominio rectangular [a, b] x [c, d] se calcula como:

```
V = ∫∫[R] f(x, y) dA = ∫[a,b] ∫[c,d] f(x, y) dy dx
```

La aplicación utiliza el método `scipy.integrate.dblquad` que emplea cuadratura adaptativa de Gauss-Kronrod para obtener resultados precisos.

### Visualización 3D
El gráfico se genera mediante:
1. Creación de una malla rectangular de puntos (x, y)
2. Evaluación de la función en cada punto de la malla
3. Renderizado de la superficie usando interpolación

## ⚠️ Limitaciones

- Las funciones deben ser continuas y finitas en el dominio especificado
- Funciones con discontinuidades pueden producir resultados incorrectos
- El tiempo de cálculo aumenta con dominios muy grandes
- Se recomienda usar dominios moderados para mejor visualización

## 🌐 Aplicación Web Flask + Plotly

### Descripción
Además de la aplicación de línea de comandos, este proyecto incluye una **aplicación web interactiva** desarrollada con Flask y Plotly que permite visualizar funciones 3D y calcular volúmenes desde el navegador.

### Características
- ✅ Interfaz web intuitiva y moderna
- ✅ Visualización 3D interactiva con Plotly (rotar, zoom, pan)
- ✅ Cálculo de volumen en tiempo real
- ✅ Ejemplos rápidos predefinidos
- ✅ Validación de errores en el navegador
- ✅ Responsive design para móviles y tablets

### Instalación

1. Instale las dependencias de la aplicación web:
```bash
pip install -r requirements-web.txt
```

### Ejecución

Para iniciar la aplicación web:

```bash
export FLASK_APP=webapp.app
flask run
```

O alternativamente:
```bash
python -m webapp.app
```

Luego abra su navegador en: **http://127.0.0.1:5000**

### Uso de la aplicación web

1. Introduzca una función matemática en el campo "Función z = f(x, y)"
   - Ejemplo: `x**2 + y**2`
2. Defina el dominio rectangular especificando los límites:
   - `a` y `b` para el eje x
   - `c` y `d` para el eje y
3. Ajuste la resolución de la malla (20-200 puntos)
4. Haga clic en "Calcular y Visualizar"
5. Visualice el resultado:
   - Volumen calculado con error estimado
   - Gráfico 3D interactivo (puede rotar con el mouse)

### Ejemplos incluidos

La aplicación incluye botones de ejemplo para funciones comunes:
- **Paraboloide**: `x**2 + y**2`
- **Ondas 2D**: `sin(x) * cos(y)`
- **Gaussiana**: `exp(-(x**2 + y**2))`
- **Silla de montar**: `x**2 - y**2`

### Nota sobre rendimiento

⚠️ **Importante**: El cálculo del volumen usando integración doble puede tardar varios segundos para:
- Funciones complejas (múltiples operaciones trigonométricas o exponenciales)
- Dominios muy grandes
- Alta resolución (>100 puntos)

La aplicación muestra un indicador de carga mientras procesa la solicitud.

## 📄 Licencia

Este proyecto es de código abierto y está disponible para uso educativo.

## 👥 Autores

Desarrollado como tarea integradora para el curso de Cálculo Multivariable.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:
1. Fork el proyecto
2. Cree una rama para su característica (`git checkout -b feature/nuevaCaracteristica`)
3. Commit sus cambios (`git commit -m 'Agregar nueva característica'`)
4. Push a la rama (`git push origin feature/nuevaCaracteristica`)
5. Abra un Pull Request