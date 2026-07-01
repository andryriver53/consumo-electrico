# Proyecto de Algorítmica - Cálculo de Consumo Eléctrico
# Integrantes: Jesús Atacho, Diego Ferrer, Ernesto Díaz, Andry Rivero

def conversor_a_kwh(amp, hrs, v):
    """Calcula los kWh usando el factor de potencia residencial estándar."""
    coseno_fi = 0.85
    watios = v * amp * coseno_fi
    resultado_kwh = (watios * hrs) / 1000
    return resultado_kwh

def total_pagar(total_kwh):
    """Calcula el costo estimado basado en la tarifa estipulada."""
    tarifa = 0.20  # Precio por kWh en $
    return total_kwh * tarifa

def semaforo_consumo(total_kwh):
    """
    Evalúa el consumo acumulado y devuelve un mensaje personalizado
    junto a un indicador visual (semáforo).
    """
    # Rango Verde: Menos de 150 kWh
    if total_kwh < 150.0:
        return "🟢 EXCELENTE: Tu consumo está bajo el rango subsidiado."
    
    # Rango Amarillo: Entre 150 y 400 kWh
    elif 150.0 <= total_kwh <= 400.0:
        return "🟡 CONSUMO MODERADO: Apaga lo que no uses para ahorrar."
    
    # Rango Rojo: Más de 400 kWh
    else:
        return "🔴 ALERTA DE CONSUMO: Te pasaste del límite. Revisa los equipos de alto consumo (220V)."

# --- Inicio del sistema ---
print("--- SISTEMA DE CONTROL ELÉCTRICO RESIDENCIAL ---")

kwh_acumulado = 0.0
equipos_registrados = 0

while True:
    menu = input("\n¿Vas a meter un equipo nuevo? (si/salir): ").lower().strip()
    
    if menu == "salir":
        print("\nCerrando el registro y generando totales...")
        break
        
    if menu != "si":
        print("Opción inválida. Por favor, escribe 'si' o 'salir'.")
        continue
        
    print("\n--- Datos del Aparato ---")
    
    # Validación de datos para evitar que el programa se rompa si ingresan texto
    try:
        voltaje_casa = float(input("Voltaje del equipo (110 o 220): "))
        if voltaje_casa <= 0:
            print("El voltaje debe ser un valor positivo, chamo.")
            continue
            
        amperaje_equipo = float(input("Amperios que consume: "))
        if amperaje_equipo <= 0:
            print("El amperaje no puede ser cero ni negativo.")
            continue
            
        horas_uso = float(input("Horas que pasa encendido al día: "))
        if horas_uso <= 0 or horas_uso > 24:
            print("Horas inválidas. Deben estar entre 1 y 24.")
            continue
            
    except ValueError:
        print("Error: Ingrese solo números válidos.")
        continue
    
    # Procesamiento de datos del equipo actual
    gasto_equipo = conversor_a_kwh(amperaje_equipo, horas_uso, voltaje_casa)
    kwh_acumulado += gasto_equipo
    equipos_registrados += 1
    
    print(f"¡Equipo guardado con éxito! Consume: {round(gasto_equipo, 3)} kWh")

# --- Reporte final para el usuario ---
cuenta_dolares = total_pagar(kwh_acumulado)
estado_consumo = semaforo_consumo(kwh_acumulado)

print("\n==============================================")
print("              FACTURA ESTIMADA                ")
print("==============================================")
print(f" Equipos Registrados:       {equipos_registrados}")
print(f" Gasto total de la casa:    {round(kwh_acumulado, 3)} kWh")
print(f" Pago estimado (Corpoelec): {round(cuenta_dolares, 2)} $")
print("----------------------------------------------")
print(f" Estado: {estado_consumo}")
print("==============================================")
print("¡Ahorra luz para que no te pegue en el bolsillo!")
