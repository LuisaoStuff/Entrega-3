#	La funcion dict declarada al inicio del programa es para filtrar de cada linea del archivo
#	los datos pertinentes con la siguiente estructura:
#		---->	_id,55702,city,ALBORN,loc,-92.557937,46.978229,pop,601,state,MN
#	Y de esta forma introducirlos en un diccionario para facilitar la seleccion y uso de los
#	mismos

def dict(linea):
	
	linea=linea.replace("{","")		#	\
	linea=linea.replace("}","")		#	|
	linea=linea.replace("[","")		#	|	Limpio cada linea para dejar un
	linea=linea.replace("]","")		#	|	flujo  de  texto  que  contiene
	linea=linea.replace(":",",")	#	|	palabras   separadas  por   ","
	linea=linea.replace('"',"")		#	|
	linea=linea.replace(" ","")		#	/

	_id=linea.split(",")[1]							#	\
	city=linea.split(",")[3]						#	|	Con esto introduzco todos
	loc=[linea.split(",")[5],linea.split(",")[6]]	#	|	datos  en  un diccionario
	pop=linea.split(",")[8]							#	|						^
	state=linea.split(",")[10]						#	/						|
													#							|
	CP={"_id":_id,"city":city,"loc":loc,"pop":pop,"state":state.strip("\n")}# __/

	return CP	#	La funcion devuelve un diccionario del Codigo Postal.

CPs = open("zips.json", "r")

print ("\n	El archivo tiene",len(CPs.readlines()),"códigos postales.\n")	#	Muestra el número
																			#	de códigos postales
CPs.seek(0)

CPs.close()

with open("zips.json","r") as fichero:	#Abrir el fichero zips.json
	
	estados={}		#	Inicializar el diccionario contador de codigos de estados

	for linea in fichero:

		if dict(linea)["state"] in estados:		#	Si encuentra el estado en el diccionario, suma 1 al valor
			estados[dict(linea)["state"]]=estados[dict(linea)["state"]]+1		
		else:									#	Si no lo encuentra, añade el estado al diccionario
			estados[dict(linea)["state"]]=1
		'''
		if dict(linea)["city"]==str("AKASKA"):	#	Si encuentra el codigo de la ciudad AKASKA,
												#	obtiene la localización, con su respectiva
			longitud=dict(linea)["loc"][0]		#	longitud y latitud.
			latitud=dict(linea)["loc"][1]
		'''
															#	Imprimir resultados:
	print("	Diccionario con el número de códigos postales de cada estado:\n\n",estados)
	
fichero.close()		#	Cerrar el fichero para evitar la corrupción del mismo

while True:
	
	Encontrado=False
	
	with open("zips.json","r") as fichero:
		
		Ciudad=str(input("\n		Dime una ciudad:	")).upper()
		Estado=str(input("		Dime un estado:		")).upper()

		for linea in fichero:
			if dict(linea)["city"]==Ciudad and dict(linea)["state"]==Estado:
				Encontrado=True
				latitud=dict(linea)["loc"][1]
				longitud=dict(linea)["loc"][0]
				break
		if Encontrado:
			
			zoom=str(input("		Especifica el zoom que quieres usar:	"))
			URL="http://www.openstreetmap.org/#map="+zoom+"/"+latitud+"/"+longitud	#	Creo la URL
			print("\n\n 	URL mapa de",dict(linea)["city"],":\n	",URL,"\n")		#	y la imprimo
			
			otra=input("		¿Quieres introducir otra ciudad?\n		(SI)		Respuesta:	").upper()
			if otra!='SI':
				print()
				break
		else:
			print("		",Ciudad,"no existe.")
			
			otra=input("		¿Quieres introducir otra ciudad?\n		(SI)		Respuesta:	").upper()
			if otra!='SI':
				print()
				break

	fichero.close()