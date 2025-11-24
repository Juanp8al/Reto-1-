"""
Proyecto Final Módulo 1: Calculadora de Nota Final de Asignatura

Este script calcula la nota definitiva de un estudiante basándose en
el promedio ponderado de tres cortes (o retos) y determina si 
el estudiante aprueba o reprueba la asignatura.
"""

CORTE_1 = 0.30
CORTE_2 = 0.30
CORTE_FINAL = 0.40

NOTA_MINIMA_APROBATORIA = 3.0
NOTA_MAXIMA_POSIBLE = 5.0
NOTA_MINIMA_POSIBLE = 0.0

# --- Funciones de Validación ---

def validar_nota_en_rango(mensaje: str) -> float:
    while True:
        try:
            entrada = input(mensaje)
            nota = float(entrada)
            
            if NOTA_MINIMA_POSIBLE <= nota <= NOTA_MAXIMA_POSIBLE:
                return nota
            else:
                print(f"Error: La nota debe estar entre {NOTA_MINIMA_POSIBLE} y {NOTA_MAXIMA_POSIBLE}.")
        except ValueError:
            print("Error: Debe ingresar un valor numérico (ej: 4.5).")

# --- Funciones de Lógica  ---

def calcular_nota_definitiva(n1: float, n2: float, n_final: float) -> float:
    ponderado_1 = n1 * CORTE_1
    ponderado_2 = n2 * CORTE_2
    ponderado_final = n_final * CORTE_FINAL
    
    nota_definitiva = ponderado_1 + ponderado_2 + ponderado_final
    return nota_definitiva

def obtener_estado_estudiante(nota: float) -> str:
    if nota >= NOTA_MINIMA_APROBATORIA:
        return "APROBADO"
    else:
        return "REPROBADO"

# --- Funciones de Control ---

def ejecutar_calculadora_notas():
    print("\n====== Calcular Nota Final======")
    # 1. Pedir datos usando la validación de rango
    nota_1 = validar_nota_en_rango(f"Ingrese nota del Corte 1 ({CORTE_1 * 100}%): ")
    nota_2 = validar_nota_en_rango(f"Ingrese nota del Corte 2 ({CORTE_2 * 100}%): ")
    nota_final = validar_nota_en_rango(f"Ingrese nota de Corte 3({CORTE_FINAL * 100}%): ")

    # 2. Calcular
    definitiva = calcular_nota_definitiva(nota_1, nota_2, nota_final)
    estado = obtener_estado_estudiante(definitiva)

    # 3. Mostrar resultado
    print("\n========= RESULTADO FINAL =========")
    print(f"Nota Definitiva: {definitiva:.2f} / {NOTA_MAXIMA_POSIBLE}")
    print(f"Estado: {estado}")
    print("===================================")

def main():
    while True:
        print("\n====== CALCULADORA DE NOTA FINAL ======")
        print("1. Calcular nota final")
        print("2. Salir")
        opcion = input("Seleccione una opción (1-2): ").strip()

        if opcion == "1":
            ejecutar_calculadora_notas()
        elif opcion == "2":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()