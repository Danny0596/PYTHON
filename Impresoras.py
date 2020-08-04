
	Definir impInicio, impFin, impTotal, tipoImpresora Como Entero
	
	Escribir "Impresiones al inicio: " Sin Saltar
	Leer impInicio
	Escribir "Impresiones al final: " Sin Saltar
	Leer ImpFin
	Si  (impInicio>=0 Y impFin>=0) Entonces
		Si (impFin<impInicio) Entonces
			Escribir ""
			Escribir "Las impresiones de final de mes deben ser mayores que las de inicio"
		SiNo
			impTotal <- impFin-impInicio
			Escribir "(1) Blanco/Negro"
			Escribir "(2) Color" 
			Escribir "Elegir tipo impresora..." Sin Saltar
			Leer tipoImpresora
			Escribir ""
			Escribir "Número de impresiones = ", impTotal
			Segun tipoImpresora Hacer
				1:
					Escribir "Costo total = ", impTotal*0.06
				2:
					Escribir "Costo total = ", impTotal*0.12
				De Otro Modo:
					Escribir "La opción de impresora no es correcta"
			FinSegun
		FinSi
	SiNo
		Escribir ""
		Escribir "Los valores de las impresiones no pueden ser negativos"
	FinSi
FinAlgoritmo
