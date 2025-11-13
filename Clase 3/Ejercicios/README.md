# 🐍 Funciones, Excepciones y Métodos en Python

Bienvenido/a a los ejercicios de Clase 3. En este directorio encontrarás 10 ejercicios diseñados para practicar funciones, manejo de excepciones, `range()`, métodos de strings y conversión de tipos en Python.

## 📝 Cómo Trabajar

### Paso 1: Completar el Ejercicio

Cada archivo contiene:
- El enunciado del ejercicio (en un docstring al inicio)
- Un espacio para que escribas tu código

**Tu tarea:** Escribe el código necesario para resolver cada ejercicio.

### Paso 2: Ejecutar tu Programa

```bash
# Desde la raíz de Ejercicios/
python ejercicios/FuncionSaludo.py

# O entrando a la carpeta
cd ejercicios
python FuncionSaludo.py
```

El programa te pedirá información y mostrará resultados.

### Paso 3: Verificar con Tests ✅

Una vez que tu programa funciona, verifica que esté correcto:

```bash
# Verificar un ejercicio específico
python run_all_tests.py 1

# O ejecutar todos los tests
python run_all_tests.py
```

Los tests te dirán automáticamente si tu solución es correcta.

---

## 📋 Ejercicios Disponibles

| # | Ejercicio | Archivo | Dificultad | Conceptos |
|---|-----------|---------|------------|-----------|
| 1 | Función de Saludo | `FuncionSaludo.py` | ⭐ Fácil | `def`, parámetros, `return` |
| 2 | Calculadora Básica | `CalculadoraBasica.py` | ⭐ Fácil | múltiples funciones |
| 3 | Función con Valor por Defecto | `FuncionConValorPorDefecto.py` | ⭐⭐ Media | parámetros opcionales |
| 4 | Sumar Múltiples Números | `SumarMultiplesNumeros.py` | ⭐⭐ Media | `*args` |
| 5 | Funciones Lambda | `FuncionesLambda.py` | ⭐⭐ Media | `lambda` |
| 6 | Manejo de Excepciones - División | `ManejoExcepcionesDivision.py` | ⭐⭐ Media | `try/except`, `ZeroDivisionError`, `ValueError` |
| 7 | Validar Índice de Lista | `ValidarIndiceLista.py` | ⭐⭐ Media | `try/except`, `IndexError` |
| 8 | Generar Secuencia de Números | `GenerarSecuenciaNumeros.py` | ⭐ Fácil | `range()` |
| 9 | Manipulación de Texto | `ManipularTexto.py` | ⭐⭐ Media | métodos de string (`.upper()`, `.lower()`, `.split()`, etc.) |
| 10 | Conversión de Tipos de Datos | `ConvertirTiposDatos.py` | ⭐ Fácil | `str()`, `int()`, `float()`, `bool()` |

### Descripción Breve de Cada Ejercicio

**1. Función de Saludo**  
Crea una función que reciba un nombre y retorne un saludo personalizado.

**2. Calculadora Básica**  
Crea funciones para sumar, restar y multiplicar dos números.

**3. Función con Valor por Defecto**  
Crea una función con parámetros opcionales usando valores por defecto.

**4. Sumar Múltiples Números**  
Usa `*args` para crear una función que sume una cantidad variable de números.

**5. Funciones Lambda**  
Crea funciones lambda para calcular el doble, verificar si es par y encontrar el mayor.

**6. Manejo de Excepciones - División**  
Maneja errores al dividir números, incluyendo división por cero y valores inválidos.

**7. Validar Índice de Lista**  
Maneja errores al acceder a elementos de una lista por índice.

**8. Generar Secuencia de Números**  
Usa `range()` para generar secuencias de números con inicio, fin y paso.

**9. Manipulación de Texto**  
Practica con métodos de string como `.upper()`, `.lower()`, `.split()`, `.count()`, etc.

**10. Conversión de Tipos de Datos**  
Convierte entre diferentes tipos de datos usando `str()`, `int()`, `float()` y `bool()`.

---

## 🧪 Sistema de Validación Automática

### Cómo Usar los Tests

#### Opción 1: Verificar UN ejercicio

```bash
python run_all_tests.py 1
python run_all_tests.py 5
# ... etc
```

#### Opción 2: Verificar TODOS los ejercicios

```bash
python run_all_tests.py
```

También puedes verificar solo un ejercicio específico por número:

```bash
python run_all_tests.py 1    # Solo ejercicio 1
python run_all_tests.py 5    # Solo ejercicio 5
```

### Interpretar los Resultados

✅ **OK** - ¡Perfecto! Tu código funciona correctamente.

```
Ran 3 tests in 0.002s
OK
```

❌ **FAIL** - Tu código tiene un problema. Lee el mensaje de error.

```
FAIL: test_saludo_nombre_simple
AssertionError: Debe incluir el nombre ingresado
```

⚠️ **ERROR** - Tu código tiene un error de sintaxis o ejecución.

```
ERROR: test_saludo_nombre_simple
NameError: name 'nombre' is not defined
```

---

## 💡 Flujo de Trabajo Recomendado

1. **Lee el enunciado** completo en el archivo `.py`
2. **Piensa en la lógica** antes de escribir código
3. **Escribe tu código** usando funciones, excepciones o métodos según corresponda
4. **Ejecuta tu programa** manualmente varias veces con diferentes datos
5. **Verifica con tests** para asegurar que funcione en todos los casos
6. **Corrige errores** si los tests fallan
7. **Continúa** con el siguiente ejercicio

---

## 📚 Conceptos Clave

### Funciones

```python
# Función básica
def saludar(nombre):
    return f"Hola, {nombre}!"

# Función con valor por defecto
def presentar(nombre, edad=18):
    return f"Mi nombre es {nombre} y tengo {edad} años."

# Función con *args
def sumar(*args):
    total = 0
    for num in args:
        total += num
    return total

# Función lambda
doble = lambda x: x * 2
```

### Manejo de Excepciones

```python
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir por cero")
except ValueError:
    print("Valor inválido")
except Exception as e:
    print(f"Error: {e}")
```

### Función range()

```python
# range(stop)
list(range(5))  # [0, 1, 2, 3, 4]

# range(start, stop)
list(range(2, 10))  # [2, 3, 4, 5, 6, 7, 8, 9]

# range(start, stop, step)
list(range(2, 10, 2))  # [2, 4, 6, 8]
```

### Métodos de String

```python
texto = "Hola Mundo"

texto.upper()      # "HOLA MUNDO"
texto.lower()      # "hola mundo"
texto.split()      # ["Hola", "Mundo"]
texto.count('o')   # 2
texto.replace('o', 'a')  # "Hala Munda"
len(texto)         # 10
```

### Conversión de Tipos

```python
str(100)      # "100"
int("100")    # 100
float("3.14") # 3.14
bool(0)       # False
bool(1)       # True
```

---

## 📁 Estructura del Proyecto

```
Ejercicios/
├── ejercicios/                    # 📝 Tus ejercicios aquí
│   ├── FuncionSaludo.py
│   ├── CalculadoraBasica.py
│   └── ...                        # (ejercicios 3-10)
├── tests/                         # ✅ Tests de validación
│   ├── test_FuncionSaludo.py
│   ├── test_CalculadoraBasica.py
│   └── ...                        # (tests 3-10)
├── run_all_tests.py               # Script ejecutor
└── README.md                      # Este archivo
```

---

## 💡 Consejos para Resolver los Ejercicios

1. **Lee bien el enunciado**: Presta atención a los detalles y casos especiales
2. **Prueba casos extremos**: Prueba con valores límite (0, negativos, strings vacíos, etc.)
3. **Usa comentarios**: Explica tu lógica con comentarios en el código
4. **Un paso a la vez**: Si un ejercicio es complejo, divídelo en partes
5. **Revisa los tests**: Los mensajes de error te dicen exactamente qué esperar
6. **Maneja errores apropiadamente**: En ejercicios con excepciones, asegúrate de capturar todos los casos posibles

### Errores Comunes a Evitar

❌ **Mal:**
```python
def saludar(nombre):
    print(f"Hola, {nombre}!")  # No retorna nada
```

✅ **Bien:**
```python
def saludar(nombre):
    return f"Hola, {nombre}!"  # Retorna el valor
```

❌ **Mal:**
```python
resultado = 10 / 0  # Crashea sin manejar el error
```

✅ **Bien:**
```python
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir por cero")
```

---

## ❓ Preguntas Frecuentes

**P: ¿Debo usar funciones o puedo escribir código directo?**  
R: Para estos ejercicios, debes usar funciones cuando el enunciado lo pida. Algunos ejercicios requieren funciones específicas.

**P: ¿En qué orden debo hacer los ejercicios?**  
R: Se recomienda hacerlos en orden (1-10) ya que aumentan progresivamente en dificultad y conceptos.

**P: Mi programa funciona pero los tests fallan. ¿Por qué?**  
R: Los tests verifican detalles específicos. Lee el mensaje de error - te dirá qué espera exactamente. Quizás falta retornar un valor o el formato no es el correcto.

**P: ¿Puedo usar otras estructuras como loops o condicionales?**  
R: Sí, puedes usar cualquier estructura que hayas aprendido. Los ejercicios se enfocan en funciones y excepciones, pero puedes combinar conceptos.

**P: El ejercicio de *args es muy difícil. ¿Hay algún consejo?**  
R: Recuerda que `*args` convierte los argumentos en una tupla. Puedes iterar sobre ella con un `for` o usar funciones como `sum()`.

---

## 🎯 Objetivos de Aprendizaje

Al completar estas actividades, habrás practicado:

- ✅ Crear y usar funciones (`def`)
- ✅ Parámetros y valores por defecto
- ✅ Funciones con `*args` y `**kwargs`
- ✅ Funciones lambda
- ✅ Manejo de excepciones (`try/except`)
- ✅ Tipos de excepciones comunes (`ZeroDivisionError`, `ValueError`, `IndexError`)
- ✅ Uso de `range()` para generar secuencias
- ✅ Métodos de strings (`.upper()`, `.lower()`, `.split()`, `.count()`, etc.)
- ✅ Conversión de tipos (`str()`, `int()`, `float()`, `bool()`)
- ✅ Validación de código con tests

---

## 🚀 ¡Comienza Ahora!

```bash
# 1. Abre ejercicios/FuncionSaludo.py y escribe tu código

# 2. Ejecuta tu programa
python ejercicios/FuncionSaludo.py

# 3. Verifica que esté correcto
python run_all_tests.py 1

# 4. ¡Continúa con el siguiente!
```

---

## 📞 ¿Necesitas Ayuda?

- **Documentación de Python:** https://docs.python.org/es/3/tutorial/controlflow.html#defining-functions
- **Consulta con tu profesor** si tienes dudas sobre los ejercicios
- **Lee los mensajes de error** de los tests - te guían hacia la solución

---

¡Buena suerte con tus ejercicios! 🎓

Recuerda: las funciones y el manejo de excepciones son fundamentales en programación. Practica hasta que te sientas cómodo/a con ellas.

