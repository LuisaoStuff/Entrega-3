#	Lee el fichero y crea una lista de diccionarios con la siguiente estructura:
#
#	alumnos = [{"nombre":"Daniel","apellidos":"Fustero López","curso":"1A",
#					"notas":{"FH":3,"LM":4,"ISO":5,"FOL":6,"PAR":7,"SGBD":6}}]

import os.path		#	Funcion para detectar si se ha creado un archivo y así evitar añadir contenido duplicado
					#	con la opción 4 del menú.

def calcular_totales(asignatura):		#	Función para calcular los aprobados totales y el número de alumnos
	
	if int(asignatura)>=5:
		totales[0]=totales[0]+1
	if int(asignatura)>=0:
		totales[1]=totales[1]+1
	return totales

def calcular_media(notas):				#	Función para calcular la media de las notas de un alumno de un curso
	
	media=(int(notas["FH"])+int(notas["LM"])+int(notas["ISO"])+int(notas["FOL"])+int(notas["PAR"])+int(notas["SGBD"]))/6
	media=round(media,2)
	return media

alumnos=[]

with open("notas.csv","0") as fichero:		#	Leer el fichero notas.csv y crear la lista con todos los alumnos
	cont=0	#	----------------------------------\
	for linea in fichero:	#					   | El contador lo uso para empezar a leer el
							#					   | fichero a partir de la segunda linea, ya 
		if cont>0:	#	--------------------------/  que la primera indica el nombre de los campos
			
			nombre=linea.split(",")[1]
			apellidos=linea.split(",")[0]
			curso=linea.split(",")[2]
			FH=linea.split(",")[3]
			LM=linea.split(",")[4]
			ISO=linea.split(",")[5]
			FOL=linea.split(",")[6]
			PAR=linea.split(",")[7]
			SGBD=(linea.split(",")[8]).strip("\n")
			
			alumno={"nombre":nombre,"apellidos":apellidos,"curso":curso,"notas":{"FH":FH,"LM":LM,"ISO":ISO,"FOL":FOL,"PAR":PAR,"SGBD":SGBD}}
			alum=alumno.copy()
			alumno=alumno.clear()
			alumnos.append(alum)
				
	
		cont=cont+1

#-----------------------Menú-------------------------#

while True:
	print('''
		A continuación, escoge una de las siguientes opciones:

		1)	Listar todos los alumnos y su nota media
		2)	Listar las notas de una asignatura de un curso determinado
		3)	Porcentaje de aprobados de un curso por cada asignatura
		4)	Guardar en un fichero alumnos y notas de un curso
		5)	Salir
		''')

	seleccion=int(input("		Opción:	"))

	if seleccion==5:			#	Salir
		
		break
		print("		Fin del programa.")

	elif seleccion==1:			#	Listar alumnos y medias

		for i in range(0,len(alumnos)):
			print("		",alumnos[i]["apellidos"],",",alumnos[i]["nombre"],"[",calcular_media(alumnos[i]["notas"]),"]")

	elif seleccion==2:			#	 Listar alumnos y notas de una asignatura y un curso determinado
		
		curso=str(input("\n		Dime un curso:	"))
		asignatura=(str(input("		Dime una asignatura:	"))).upper()
		
		for i in range(0,len(alumnos)):
			if alumnos[i]["curso"]==curso:
				print("		",alumnos[i]["apellidos"],",",alumnos[i]["nombre"],alumnos[i]["notas"][asignatura])

	elif seleccion==3:			#	Listar porcentaje de aprobados en cada asignatura

		curso=str(input("\n		Dime un curso:	"))

		for z in range(0,6):	#	Al ser diccionarios necesito de un indicador para insertar en la funcion
								#	la asignatura adecuada y de este modo evitar usar un acumulador para cada
								#	una. En su lugar uso una lista que inicializo por cada vuelta (por cada 
								#	asignatura) y así acorto la longitud del código.
			totales=[0,0]

			for i in range(0,len(alumnos)):
					
				if z==0 and alumnos[i]["curso"]==curso:
					totales=calcular_totales(alumnos[i]["notas"]["FH"])
				if z==1 and alumnos[i]["curso"]==curso:
					totales=calcular_totales(alumnos[i]["notas"]["LM"])
				if z==2 and alumnos[i]["curso"]==curso:
					totales=calcular_totales(alumnos[i]["notas"]["ISO"])
				if z==3 and alumnos[i]["curso"]==curso:
					totales=calcular_totales(alumnos[i]["notas"]["FOL"])
				if z==4 and alumnos[i]["curso"]==curso:
					totales=calcular_totales(alumnos[i]["notas"]["PAR"])
				if z==5 and alumnos[i]["curso"]==curso:
					totales=calcular_totales(alumnos[i]["notas"]["SGBD"])

			if z==0:
				print("		FH:	",round((totales[0]/totales[1]*100)),"%")
			elif z==1:
				print("		LM:	",round((totales[0]/totales[1]*100)),"%")
			elif z==2:
				print("		ISO:	",round((totales[0]/totales[1]*100)),"%")
			elif z==3:
				print("		FOL:	",round((totales[0]/totales[1]*100)),"%")
			elif z==4:
				print("		PAR:	",round((totales[0]/totales[1]*100)),"%")
			elif z==5:
				print("		SGBD:	",round((totales[0]/totales[1]*100)),"%")

	elif seleccion==4:

		curso=str(input("\n		Dime un curso:	"))

		if os.path.exists(curso):
			print("	Ya se ha creado un archivo sobre este curso.")
		else:
			
			f=open(curso,"w")
			
			for i in range(0,len(alumnos)):
				if alumnos[i]["curso"]==curso:
					f.write("		")
					f.write(alumnos[i]["apellidos"])
					f.write(",")
					f.write(alumnos[i]["nombre"])
					f.write("[")
					f.write(str(calcular_media(alumnos[i]["notas"])))
					f.write("]\n")
			f.close()


#-----------------------Menú-------------------------#


# Para mejorar el programa, debemos usar LISTA.append(list(DICCIONARIO.keys))
			#	De esta forma añades a una lista los indices de un diccionario