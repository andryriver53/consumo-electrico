def calcular_porcentajes():
    # Bucle para asegurar que el número de notas sea válido sin cerrar el programa
    while True:
        try:
            numerodenotas = int(input("\n¿Cuántas notas deseas ingresar?: "))
            punto_max = float(input("Ingrese el punto máximo de la nota: "))
            
            if numerodenotas <= 0 or punto_max <= 0:
                print("Lo siento, ingresaste un valor inválido. Deben ser mayores a 0.")
                continue
            break  # Sale del bucle si el número es válido
        except ValueError:
            print("Por favor, ingresa un número entero válido.")
            
    # Variables acumuladoras
    total_porcentaje = 0
    total_porcentaje_obtenido = 0

    # Usamos un ciclo while tradicional con contador i
    i = 1
    while i <= numerodenotas:
        while True:
            print("\nEvaluación número", i)
            try:
                porcentajenota = float(input("Ingrese el porcentaje de la nota (ejemplo: 20 para 20%): "))
                punto_obtenido = float(input("Ingrese el punto obtenido: "))
                
                # Validaciones lógicas
                if punto_max <= 0 or punto_obtenido < 0 or porcentajenota < 0:
                    print("-" * 80)
                    print("Los valores no pueden ser negativos y el punto máximo debe ser mayor a 0.")
                    print("-" * 80)
                    continue
                    
                if punto_obtenido > punto_max:
                    print("-" * 80)
                    print("Error: El punto obtenido no puede ser mayor al punto máximo.")
                    print("-" * 80)
                    continue
                
                # Cálculos del programa
                porcentaje_obtenido = (punto_obtenido / punto_max) * porcentajenota
                total_porcentaje = total_porcentaje + porcentajenota
                total_porcentaje_obtenido = total_porcentaje_obtenido + porcentaje_obtenido 
                
                print("De esta nota obtuviste un", round(porcentaje_obtenido, 2), "% de tu nota final.")
                break 
                
            except ValueError:
                print("Por favor, ingresa un número válido.")
        
        # Incrementamos el contador para pasar a la siguiente nota
        i = i + 1
            
    # Validación del acumulado de porcentajes
    if total_porcentaje > 0 and total_porcentaje <= 100:    
        resumen = (total_porcentaje_obtenido / total_porcentaje)
        resumen_puntos = resumen * 20 
        
        print("#" * 42)
        print("             RESUMEN DE NOTUNI            ")
        print("#" * 42)
        print("Porcentaje total evaluado:", round(total_porcentaje, 1), "%")
        print("PORCENTAJE TOTAL OBTENIDO:", round(total_porcentaje_obtenido, 2), "%")
        print("TU PROMEDIO EN PUNTOS:", round(resumen_puntos, 2), "/ 20.00") 
        
        if total_porcentaje < 100:
            restante = 100 - total_porcentaje
            print("Todavía falta por evaluar un", round(restante, 2), "% de la materia.")
        print("-" * 42)
    else:
        print("\nEl porcentaje total sumó", round(total_porcentaje, 1), "%. No puede superar el 100%.")


def calcular_puntos():
    while True:
        try:
            resumennotas = 0 
            
            numerodenotas = int(input("\nDigite el número de notas: "))
            numero_max = int(input("Digite el número máximo de puntos: "))
            
            # CORRECCIÓN DE REINGENIERÍA: usaremos estrictamente > 0 para evitar ZeroDivisionError
            if numerodenotas > 0 and numero_max > 0:
                i = 1
                while i <= numerodenotas:
                    while True:
                        try:
                            print("Digite la nota", i, ":")
                            notas = float(input())
                            if notas < 0 or notas > numero_max:
                                print("La nota debe estar entre 0 y el máximo permitido.")
                                continue
                            resumennotas = resumennotas + notas
                            break
                        except ValueError:
                            print("Por favor, ingresa una nota válida.")
                    
                    # Incrementamos el contador
                    i = i + 1
                        
                resumenpuntos = (resumennotas / numerodenotas)
                
                if resumenpuntos > numero_max:
                    print("-" * 80)
                    print("Error: El promedio no puede ser mayor al número máximo de puntos.")
                    print("-" * 80)
                    continue
                    
                print("#" * 42)
                print("             RESUMEN DE NOTUNI            ")
                print("#" * 42)
                print("Su promedio en puntos es:", round(resumenpuntos, 2))
                print("-" * 42)
                break  
            else:
                print("El número de notas y los puntos máximos deben ser estrictamente mayores a 0.")
                continue
        except ValueError:
            print("Por favor, ingresa un número entero válido.")

    
def main():
    print("#" * 42)
    print("                NOTUNI                    ")
    print("#" * 42)
    print("¡Bienvenido a NOTUNI!\nEl programa que te ayudará a calcular tus notas de manera fácil y rápida.")
    
    seguir = "s"
    
    while seguir == "s" or seguir == "si":
        while True:
            try:
                print("\n¿Qué desea hacer?")
                print("1. Calcular notas (puntos a puntos)")
                print("2. Calcular porcentajes de notas")
                opcion = int(input("Ingrese el número de la opción: "))
                
                if opcion == 1:
                    calcular_puntos()
                    break
                elif opcion == 2:
                    calcular_porcentajes()
                    break
                else:
                    print("Opción no válida. Por favor, ingrese 1 o 2.")
            except ValueError:
                print("Por favor, ingresa un número entero válido.")
        
        seguir = input("\n¿Deseas calcular tus notas nuevamente? (s/n): ").lower()

    print("\nPrograma finalizado. ¡Gracias por usar NOTUNI!")

main()