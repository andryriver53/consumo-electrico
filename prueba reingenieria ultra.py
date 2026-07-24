calculos_de_puntos = 0
calculos_de_porcentajes = 0
def tabla_converciones():
    print("en prueba")
def confirmacion_de_salida():
    seguir = input("\n¿Deseas calcular tus notas nuevamente o de alguna otra materia? (s/n): ").lower().strip()
    if seguir == "s":
        main()
    elif seguir == "n":
        print("programa finalizado")
        exit()
    else:
        print("Porfavor ingrese s o n")
        confirmacion_de_salida()
def calcular_porcentajes():
            global calculos_de_porcentajes
  
            #bucle para asegurar que el número de notas sea valido sin cerrar el programa
            while True:
                try:
                    numerodenotas = int(input("\n¿Cuántas notas deseas ingresar?: "))
                    if numerodenotas <= 0:
                        print("losiento, ingresaste un valor inválido.")
                        continue
                    break
                except ValueError:
                    print("Por favor, ingresa un número entero valido.")
            while True:
                try:
                    punto_max = float(input("Ingrese el punto máximo de la nota: "))
                    if punto_max <= 0:
                        print("Lo siento, ingresaste un valor inválido.")
                        continue
                    break  #sale del bucle si el numero es valido
                except ValueError:
                    print("Por favor, ingresa un número entero valido.")
            
            #variables en 0
            total_porcentaje = 0
            total_porcentaje_obtenido = 0

            #colocamos un for para que el usuario pueda ingresar las notas que quiera
            for i in range(1, numerodenotas + 1):
                
                #el while True sirve para reintentar la entrada en caso de error en esta nota específica
                while True:
                    print(f"\nEvaluación número {i}")
                    
                    try:
                        porcentajenota = float(input("Ingrese el porcentaje de la nota (ejemplo: 20 para 20%): "))
                        if porcentajenota < 0:
                            print("-" * 80)
                            print("los valores no pueden ser negativos")
                            print("-" * 80)
                            continue
                        break
                    except ValueError:
                        print("porfavor ingrese un valor valido")
                while True:
                    try:
                        punto_obtenido = float(input("Ingrese el punto obtenido: "))
                        
                        #validaciones
                        if punto_max <= 0 or punto_obtenido < 0:
                            print("-" * 80)
                            print("Los valores no pueden ser negativos y el punto máximo debe ser mayor a 0.")
                            print("-" * 80)
                            continue
                            
                        if punto_obtenido > punto_max:
                            print("-" * 80)
                            print("Error: El punto obtenido no puede ser mayor al punto máximo.")
                            print("-" * 80)
                            continue
                        
                        #estos son los calculos del programa
                        porcentaje_obtenido = (punto_obtenido / punto_max) * porcentajenota
                        total_porcentaje += porcentajenota
                        total_porcentaje_obtenido += porcentaje_obtenido 
                        
                        #se rompe el ciclo interno para seguir con la siguiente nota
                        print(f"De esta nota obtuviste un {porcentaje_obtenido:.2f}% de tu nota final.")
                        break 
                        
                    except ValueError:
                        print("Por favor, ingresa un número válido.")
            
            #validacion del acumulado de los porcentajes
            if 0 < total_porcentaje <= 100:    
                
                #calculo del promedio escalado a base 20
                resumen = (total_porcentaje_obtenido / total_porcentaje)
                resumen_puntos = resumen * 20 
                
                print("#" * 42)
                print("             RESUMEN DE NOTUNI            ")
                print("#" * 42)
                print(f"Porcentaje total evaluado de las {numerodenotas} notas: {total_porcentaje:.1f}%")
                print(f"PORCENTAJE TOTAL OBTENIDO: {total_porcentaje_obtenido:.2f}%")
                print(f"TU PROMEDIO EN PUNTOS: {resumen_puntos:.2f} / {punto_max:.2f}") 
                
                #si el porcentaje no llega al 100%, le avisa al usuario cuanto falta por evaluar
                if total_porcentaje < 100:
                    restante = 100 - total_porcentaje
                    print(f"Todavía falta por evaluar un {restante:.2f}% de la materia.")
                print("-" * 42)
                calculos_de_porcentajes += 1
            
            else:
                print(f"\nEl porcentaje total sumó {total_porcentaje:.1f}%. No puede ser mayor a 100%.")
            #se llama a la confirmacion para que vaya al menu de salida
            confirmacion_de_salida()
def calcular_puntos():
    global calculos_de_puntos
    while True:
            try:
                # Mover el acumulador aquí asegura que se limpie si el usuario repite por un error
                resumennotas = 0 
                
                numerodenotas = int(input("Digite el número de notas: "))
                if numerodenotas <=0:
                    print("ingrese un valor positivo")
                    continue
                break
            except ValueError:
                print("porfavor ingrese un número valido")
    while True:
            try:
                numero_max = int(input("Digite el número máximo de puntos: "))
                if numero_max <=0:
                    print("ingrese un valor positivo")
                    continue
                break
            except ValueError:
                print("porfavor ingrese un número valido")
                
                #elima el error de division por cero
    while True:
            try:
                if numerodenotas >= 0 and numero_max >= 0:
                    for i in range(1, numerodenotas + 1):
                        while True:
                            try:
                                notas = float(input(f"Digite la nota {i}: "))
                                if notas<=0:
                                    print("las notas no pueden ser negativas, porfavor ingrese un valor positivo")
                                else:
                                    resumennotas += notas
                                    break
                            except ValueError:
                                print("porfavor ingrese un número entero valido")


                    resumenpuntos = (resumennotas / numerodenotas)
                    
                    #Controla que el resultado no sea lógicamente imposible
                    if resumenpuntos > numero_max:
                        print("-" * 80)
                        print("Error: El promedio en puntos no puede ser mayor al número máximo de puntos.")
                        print("-" * 80)
                        continue
                        
                    print("#" * 42)
                    print("             RESUMEN DE NOTUNI            ")
                    print("#" * 42)
                    
                    print(f"Su promedio en puntos es: {resumenpuntos:.2f}")
                    
                    print("-" * 42)
                    calculos_de_puntos +=1
                    confirmacion_de_salida()
                    break
            except ValueError:
                    print("Por favor, ingresa un número entero válido.")
            else:
                    
                    print("El número de notas debe ser mayor a 0 y los puntos máximos no pueden ser negativos. Intente de nuevo.")
                    continue
                
def contador_de_porcentajes_y_puntos_calculados():
    print("#" * 42)
    print ("           Estadistica de calculos           ")
    print("#" * 42)
    print(f"Cálculos de Puntos a puntos realizado:   {calculos_de_puntos}")
    print(f"Cálculos de Porcentajes realizados:      {calculos_de_porcentajes}")
    total_de_calculos = calculos_de_puntos + calculos_de_porcentajes
    print(f"Total de Calculos realizados:            {total_de_calculos}")
    print("-" * 42)
    input("\nPresiona cualquier tecla para volver al menú")
    main()
    
def main():
    
    #presentacion para cuando se abra por primera vez el programa
    print("#" * 42)
    print("                NOTUNI                    ")
    print("#" * 42)
    print("¡Bienvenido a NOTUNI!\nEl programa que te ayudará a calcular tus notas de manera fácil y rápida.")
    
    seguir = "s"
    
    # colocamos un while para que el usuario pueda calcular sus notas cuantas veces quiera
    while seguir == "s" or seguir == "si":
        # bucle para asegurar que el usuario ingrese una opción valida sin cerrar el programa
        while True:
            try:
                opcion = int(input("\n¿Que desea hacer?\n1. Calcular notas(puntos a puntos)\n2. Calcular porcentajes de notas \n3 Ver total de calculos realizados. \nIngrese el número de la opción: "))
                
                if opcion == 1:
                    calcular_puntos()
                    break  # Este break te saca del 'while True' de la opción
                elif opcion == 2:
                    calcular_porcentajes()
                    break  # Este break te saca del 'while True' de la opción
                elif opcion == 3:
                    contador_de_porcentajes_y_puntos_calculados()
                else:
                    print("Opción no válida. Por favor, ingrese 1, 2 o 3.")
            except ValueError:
                print("Por favor, ingresa un número entero válido.")
          
main()
