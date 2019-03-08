#	Código de la cuenta = 00 AAAA BBBB CC DDDDDDDDDD

#	Leer el número de cuenta: String
#	Compruebas que tenga 20 caracteres numéricos
#	Crear una lista con los 8 primeros numeros y los dos 0 a la izquierda
#	Calculamos el codigo de control 1 y comprobamos que es igual a la primera "C"
#	Calculas el codigo de control 2 y comprobamos que es igual a la segunda "C"


def calcula_dc(lista):
	"""Calcula el dígito de control de una CCC.
	Recibe una lista con 10 numeros enteros y devuelve el DC
	correspondiente"""
	pesos = [1, 2, 4, 8, 5, 10, 9, 7, 3, 6]
	aux = []
	for i in range(10):
		aux.append(lista[i]*pesos[i])
	resto = 11 - sum(aux) %11
	if resto == 10:
		return 1
	elif resto == 11:
		return 0
	else:
		return resto

while True:


	while True:
		charnum=True
		codigo=str(input("		Dame el código de cuenta:	"))
	
		for i in range(0,len(codigo)):
			if not codigo.isdigit():
				charnum=False
	
		if charnum==True and len(codigo)==20:	#Validación de la longitud y uso exclusivo de números
			break
		else:
			print("		El código no es válido, debe tener 20 caracteres numéricos.")

	control1=[0,0]		#Inicializamos la lista con dos 0
	
	for i in range(0,8):
		control1.append(int(codigo[i]))		#Vamos añadiendo los números del codigo a la lista

	control2=[]

	for i in range(10,20):
		control2.append(int(codigo[i]))		#Vamos añadiendo los números del codigo a la lista

	#	Uso de la funcion calcula_dc para calcular los números de control y comprobacion de estos

	if calcula_dc(control1)==int(codigo[8]) and calcula_dc(control2)==int(codigo[9]):
		print("		El codigo es valido.")
		break
	else:
		print("		El código no es válido")


#Leer el archivo bancos.txt y comprobar el número de la linea coincide con los 4 primeros números del código de cuenta

with open("bancos.txt","r") as fichero:
    for linea in fichero:
        if int(linea.split(",")[0])==int(codigo[0:4:]):
        	print("		La entidad es:	",linea.split(",")[1])
