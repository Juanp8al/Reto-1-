# Actividad Final: Módulo 1 Python

## 🎓 Calculadora de Nota Final de Asignatura

### 1. Descripción 

Este proyecto es un script de consola que calcula la nota definitiva de un estudiante en una asignatura. El sistema solicita las notas de tres cortes (dos retos y un proyecto final) y aplica un **promedio ponderado** para determinar si el estudiante "Aprueba" o "Reprueba" la materia.

### 2. Explicación 

El objetivo es demostrar la comprensión de los conceptos del Módulo 1 aplicados a un caso de uso académico común:

* **Modularidad (Funciones `def`):** El código está estructurado en funciones con responsabilidades únicas:
    * `validar_nota_en_rango`: Una función de validación robusta que usa `try-except` y valida que la nota esté entre 0.0 y 5.0.
    * `calcular_nota_definitiva`: Contiene la lógica matemática (el cálculo ponderado).
    * `obtener_estado_estudiante`: Contiene la lógica de decisión (`if/else`) para aprobar o reprobar.
    * `main`: Controla el menú principal.
* **Control de Flujo (`if/else`):** Se usa para la lógica clave de determinar si la nota final es aprobatoria o no.
* **Bucles (`while`):** Se utilizan dos tipos de bucles:
    1.  Un `while True` para el menú principal, permitiendo calcular notas de múltiples estudiantes.
    2.  Un `while True` dentro de la función de validación para forzar al usuario a ingresar una nota válida.
* **Buenas Prácticas:**
    * Uso de **Constantes** (en mayúsculas) para definir los porcentajes (30%, 40%) y la nota de aprobación (3.0). Esto hace que el código sea fácil de mantener.
    * `if __name__ == "__main__"` como punto de entrada.
    * `f-strings` con formato (`:.2f`) para mostrar las notas con dos decimales.





# Actividad Final: Módulo 1 Python

## 🅿️ Calculadora de Tarifas de Parqueadero 

### 1. Descripción 

Este proyecto es un script de consola que calcula el costo total a pagar en un parqueadero. El sistema solicita al usuario las horas de permanencia y el tipo de vehículo (carro o moto) para determinar la tarifa.

Esta versión avanzada (V3.0) aplica descuentos automáticamente por estancias largas y **guarda un historial de todos los cobros del día, incluyendo la fecha y hora** de cada transacción.

### 2. Explicación 

El objetivo es demostrar la aplicación de **todos** los conceptos del Módulo 1 en un programa de consola funcional y profesional:

* **Modularidad (Funciones `def`):** El código está 100% modularizado. Cada función tiene una tarea única:
    * `validar_float_positivo` y `validar_tipo_vehiculo` protegen la entrada.
    * `calcular_total_pagar` contiene la lógica de negocio (tarifas y descuentos).
    * `mostrar_historial` se encarga de leer y presentar los datos guardados.
    * `main` controla el menú principal.
* **Bucles (`while` y `for`):** Se demuestran ambos tipos de bucles:
    * **`while True`**: Se usa para el menú principal y para la validación robusta de entradas (forzando al usuario a ingresar un dato correcto).
    * **`for`**: Se usa en `mostrar_historial` para **iterar** sobre la lista de registros y mostrar la tabla del día.
* **Manejo de Datos (Listas y Diccionarios):** Esta versión es más avanzada porque usa una lista (`historial_dia`) como una base de datos temporal. Cada cobro se guarda como un **diccionario** (`registro`), que es una práctica profesional para estructurar datos.
* **Módulos Externos:** Se importa y utiliza el módulo `datetime` para capturar la fecha y hora (`datetime.now()`) y formatearla (`.strftime()`), una habilidad clave.
* **Control de Flujo (`if/elif/else`):** Se usa para la lógica del menú, para la lógica de negocio (tarifa de carro vs. moto) y para aplicar el descuento (`if horas > 10`).
* **Buenas Prácticas:**
    * Uso de **Constantes** (en mayúsculas) para las tarifas.
    * Validación `try-except` para prevenir que el programa se rompa con entradas inválidas.
    * `if __name__ == "__main__"` como punto de entrada.
    * `f-strings` con formato avanzado (`:,.0f`, `:<10`) para crear una tabla ordenada en el historial.

