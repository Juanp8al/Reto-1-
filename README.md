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

