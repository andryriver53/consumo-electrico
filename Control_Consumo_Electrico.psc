Función resultado_kwh <- conversor_a_kwh(amp,hrs,v)
	Definir coseno_fi, watios, resultado_kwh Como Real
	coseno_fi <- 0.85
	watios <- v*amp*coseno_fi
	resultado_kwh <- (watios*hrs)/1000
FinFunción

Función pago <- total_pagar(total_kwh)
	Definir tarifa, pago Como Real
	tarifa <- 0.20
	pago <- total_kwh*tarifa
FinFunción

Algoritmo Control_Consumo_Electrico
	Definir kwh_acumulado, voltaje_casa, amperaje_equipo, horas_uso, gasto_equipo, cuenta_dolares Como Real
	Definir kwh_redondeado Como Real
	Definir menu Como Cadena
	kwh_acumulado <- 0.0
	menu <- 'si'
	Escribir '--- SISTEMA DE CONTROL ELECTRICO RESIDENCIAL ---'
	Mientras menu<>'salir' Hacer
		Escribir ''
		Escribir '¿Vas a meter un equipo nuevo? (si/salir): '
		Leer menu
		menu <- Minusculas(menu)
		Si menu='si' Entonces
			Escribir ''
			Escribir '--- Datos del Aparato ---'
			Escribir 'Voltaje del equipo (110 o 220): '
			Leer voltaje_casa
			Si voltaje_casa<=0 Entonces
				Escribir 'Pusiste un voltaje invalido, chamo. Ponlo positivo.'
			SiNo
				Escribir 'Amperios que consume: '
				Leer amperaje_equipo
				Si amperaje_equipo<=0 Entonces
					Escribir 'El amperaje no puede ser cero ni negativo.'
				SiNo
					Escribir 'Horas que pasa encendido al dia: '
					Leer horas_uso
					Si horas_uso<=0 O horas_uso>24 Entonces
						Escribir 'Pusiste horas locas. Tienen que ser entre 1 y 24.'
					SiNo
						gasto_equipo <- conversor_a_kwh(amperaje_equipo,horas_uso,voltaje_casa)
						kwh_acumulado <- kwh_acumulado+gasto_equipo
						Escribir 'Equipo guardado fino. Consume: ', gasto_equipo, ' kWh'
					FinSi
				FinSi
			FinSi
		SiNo
			Si menu<>'salir' Entonces
				Escribir 'Pusiste una opcion que no es. Escribe si o salir.'
			FinSi
		FinSi
	FinMientras
	Escribir ''
	Escribir 'Cerrando el registro y generando totales...'
	cuenta_dolares <- total_pagar(kwh_acumulado)
	// Truco matematico: 1000 para 3 decimales en kWh, y 100 para 2 decimales en dinero
	kwh_redondeado <- Trunc(kwh_acumulado*1000)/1000
	cuenta_dolares <- Trunc(cuenta_dolares*100)/100
	Escribir ''
	Escribir '=============================================='
	Escribir '             FACTURA ESTIMADA              '
	Escribir '=============================================='
	Escribir ' Gasto total de la casa: ', kwh_redondeado, ' kWh'
	Escribir ' Pago estimado por Corpoelec: ', cuenta_dolares, ' $'
	Escribir '=============================================='
	Escribir '¡Ahorra luz para que no te pegue el bolsillo!'
FinAlgoritmo
