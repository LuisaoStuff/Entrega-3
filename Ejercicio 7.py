
efectivo=[50.0,20.0,10.0,5.0,2.0,1.0,0.5,0.2,0.1,0.05,0.02,0.01] # <----Lista con los posibles
																	#	valores de monedas y
precio=float(input("\n		Introduce el precio:	"))				#	billetes para el cambio

while True:

	pago=float(input("		Introduce el total pagado:	"))		#	Comprueba que el total pagado
	if pago>=precio:											#	es mayor que el precio, si no
		break													#	muestra un error por pantalla
	else:
		print("		¡Debes entregar una cantidad mayor o igual al precio!")

cambio=[]												#	Inicializa la lista cambio[] y calcula
vuelta=round((pago-precio),2)							#	la vuelta
print("\n		Cantidad a devolver:",vuelta,"\n\n")

for i in range(0,len(efectivo)):

	if vuelta-efectivo[i]>=0:		#	Comprobar que el billete es más pequeño que la vuelta en ese momento
		
		cantidad=int(vuelta*100)//int(efectivo[i]*100)	#	Hace una division entera para saber
														#	cuantos billetes hay que restar a la
		for a in range(0,cantidad):						#	vuelta en ese momento
			vuelta=round((vuelta-efectivo[i]),2)
			cambio.append(round(efectivo[i],2))

	if cambio.count(efectivo[i])>0:			#	Imprimir cantidad de monedas o billetes que hay
		if efectivo[i]>=5:					#	en la lista cambio[]
			print("		",cambio.count(efectivo[i]),"billetes de",int(efectivo[i]),"€")
		elif efectivo[i]==1.0 or efectivo[i]==2.0:
			print("		",cambio.count(efectivo[i]),"monedas de",int(efectivo[i]),"€")
		elif efectivo[i]<1:
			print("		",cambio.count(efectivo[i]),"monedas de",int(efectivo[i]*100),"céntimos")	
						#	cambio.count(efectivo[i]) Es la cantidad de veces que aparece el valor de la lista efectivo en la lista cambio
						#	int(efectivo[i]) Es el valor de ese efectivo
print()
