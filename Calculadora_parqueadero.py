"""
Proyecto Final Módulo 1: Calculadora de Tarifas de Parqueadero

Este script calcula el costo del servicio de parqueadero
basado en el tipo de vehículo y las horas de estadía,
aplicando validaciones robustas y lógica de negocio.


"""

from datetime import datetime


TARIFA_CARRO_HORA = 5000
TARIFA_MOTO_HORA = 2000
HORAS_PARA_DESCUENTO = 10
PORCENTAJE_DESCUENTO = 0.10  

historial_dia = []  

# --- Funciones de Validación ---

def validar_float_positivo(mensaje: str) -> float:
    while True:
        try:
            entrada = input(mensaje)
            valor = float(entrada)
            if valor >= 0:
                return valor
            else:
                print("Error: El número no puede ser negativo.")
        except ValueError:
            print("Error: Debe ingresar un valor numérico (ej: 3.5).")

def validar_tipo_vehiculo() -> str:
    while True:
        tipo = input("Ingrese tipo de vehículo ('carro' o 'moto'): ").strip().lower()
        if tipo == "carro" or tipo == "moto":
            return tipo
        else:
            print("Error: Tipo inválido. Solo se acepta 'carro' o 'moto'.")

# --- Función de Lógica ---

def calcular_total_pagar(horas: float, tipo: str) -> float:
    if tipo == "carro":
        tarifa_base = TARIFA_CARRO_HORA
    else:
        tarifa_base = TARIFA_MOTO_HORA
    
    total = horas * tarifa_base
    
    if horas > HORAS_PARA_DESCUENTO:
        descuento = total * PORCENTAJE_DESCUENTO
        total_final = total - descuento
        print(f"   - Subtotal: ${total:,.0f}")
        print(f"   - Se aplica descuento del {PORCENTAJE_DESCUENTO * 100}%: -${descuento:,.0f}")
    else:
        total_final = total

    return total_final

# --- Funciones de Control ---

def ejecutar_calculadora():
    print("\n--- 1. Calcular Nuevo Ingreso ---")
    
    horas = validar_float_positivo("Ingrese las horas de permanencia (ej: 2.5): ")
    tipo = validar_tipo_vehiculo()
    total_pagar = calcular_total_pagar(horas, tipo)

    print("-" * 30)
    print(f"Vehículo: {tipo.capitalize()}")
    print(f"Horas: {horas}")
    print(f"TOTAL A PAGAR: ${total_pagar:,.0f}")
    print("-" * 30)
    
    
    ahora = datetime.now() 
    
    
    fecha_hora_actual = ahora.strftime("%d/%m/%Y %I:%M %p") 

    registro = {
        "fecha_hora": fecha_hora_actual, 
        "tipo": tipo.capitalize(),
        "horas": horas,
        "cobro": total_pagar
    }
    historial_dia.append(registro)
    print("(Registro guardado en el historial del día)")


def mostrar_historial():
    print("\n--- 2. Historial del Día ---")
    
    if not historial_dia:
        print("No hay registros en el historial de hoy.")
        return 

    total_general = 0.0
    
    print(f"{'Fecha y Hora':<20} | {'Tipo':<10} | {'Horas':<10} | {'Cobro':<15}")
    print("-" * 59) 
    
    for registro in historial_dia:
        
        print(f"{registro['fecha_hora']:<20} | {registro['tipo']:<10} | {registro['horas']:<10.1f} | ${registro['cobro']:<14,.0f}")
        total_general += registro['cobro'] 
    
    print("-" * 59) 
    print(f"Total Acumulado del Día: ${total_general:,.0f}")


def main():
    while True:
        print("\n====== SISTEMA DE PARQUEADERO ======")
        print("1. Registrar y Calcular cobro")
        print("2. Ver Historial del Día")
        print("3. Salir")
        opcion = input("Seleccione una opción (1-3): ").strip()

        if opcion == "1":
            ejecutar_calculadora()
        elif opcion == "2":
            mostrar_historial()
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()