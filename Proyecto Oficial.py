# Proyecto de Algoritmica - Calculo de Consumo Electrico
# Integrantes: Jesus Atacho Diego Ferrer Ernesto Diaz Andry Rivero

def conversor_a_kwh(amp, hrs, v):
    """Saca los kWh usando el factor de potencia residencial."""
    coseno_fi = 0.85
    watios = v * amp * coseno_fi
    resultado_kwh = (watios * hrs) / 1000
    return resultado_kwh

def total_pagar(total_kwh):
    """Multiplica el consumo acumulado por el precio de la luz."""
    tarifa = 0.20
    return total_kwh * tarifa

# --- Inicio del sistema ---
print("--- SISTEMA DE CONTROL ELECTRICO RESIDENCIAL ---")

kwh_acumulado = 0.0

while True:
    menu = input("\n¿Vas a meter un equipo nuevo? (si/salir): ").lower().strip()
    
    if menu == "salir":
        print("\nCerrando el registro y generando totales...")
        break
        
    if menu != "si":
        print("Pusiste una opcion que no es. Escribe si o salir.")
        continue
        
    print("\n--- Datos del Aparato ---")
    
    voltaje_casa = float(input("Voltaje del equipo (110 o 220): "))
    if voltaje_casa <= 0:
        print("Pusiste un voltaje invalido, chamo. Ponlo positivo.")
        continue
        
    amperaje_equipo = float(input("Amperios que consume: "))
    if amperaje_equipo <= 0:
        print("El amperaje no puede ser cero ni negativo.")
        continue
        
    horas_uso = float(input("Horas que pasa encendido al dia: "))
    if horas_uso <= 0 or horas_uso > 24:
        print("Pusiste horas locas. Tienen que ser entre 1 y 24.")
        continue
    
    # Procesamos con las funciones de arriba
    gasto_equipo = conversor_a_kwh(amperaje_equipo, horas_uso, voltaje_casa)
    kwh_acumulado = kwh_acumulado + gasto_equipo
    print(f"Equipo guardado fino. Consume: {round(gasto_equipo, 3)} kWh")

# --- Reporte final para el usuario ---
cuenta_dolares = total_pagar(kwh_acumulado)

print("\n==============================================")
print("             FACTURA ESTIMADA              ")
print("==============================================")
print(" Gasto total de la casa:", round(kwh_acumulado, 3), "kWh")
print(" Pago estimado por Corpoelec:", round(cuenta_dolares, 2), "$")
print("==============================================")
print("¡Ahorra luz para que no te pegue el bolsillo!")