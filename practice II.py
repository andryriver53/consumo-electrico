def buscar_mayor(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

while True:
    opcion = input("¿Quieres comparar numeros? (si/salir): ").lower()
    
    if opcion == "salir":
        print("Fin del programa. ¡Exito mañana, chamo!")
        break
        
    n1 = int(input("Introduce el primer numero: "))
    n2 = int(input("Introduce el segundo numero: "))
    
    mayor = buscar_mayor(n1, n2)
    
    print("El numero mayor es:", mayor)
    print("--------------------------------")