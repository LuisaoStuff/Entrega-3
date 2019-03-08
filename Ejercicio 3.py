from crypt import crypt

user=str(input("\n			Dame un usuario: "))


usertrue=False
passwdtrue=False
with open("shadow","r") as fichero:		#	Leer el fichero shadow

	for linea in fichero:				#	Recorre el fichero linea a linea
		
		if linea.split(":")[0]==user:	#	Si encuentra el usuario dentro del fichero:

			sal=linea.split(":")[1][0:12]		#	Esta es la sal de encriptado
			cryptpass=linea.split(":")[1]		#	Esta es la clave encriptada
			usertrue=True						#	Notifica que ha encontrado al usuario
			break								#	Para el bucle

with open("diccionario.txt","r") as diccionario:	#	Leer el diccionario
	cont=0
	for i in diccionario:
					
		if cont==0:
			print ("\n"*30,"				[                    ] 0% ")		#	\
		elif cont==8419:														#	|
			print ("\n"*30,"				[==                  ] 10%")		#	|
		elif cont==16839:														#	|
			print ("\n"*30,"				[====                ] 20%")		#	|
		elif cont==25258:														#	|
			print ("\n"*30,"				[======              ] 30%")		#	|
		elif cont==33678:														#	|
			print ("\n"*30,"				[========            ] 40%")		#	|
		elif cont==42097:														#	|
			print ("\n"*30,"				[==========          ] 50%")		#	|	Barras de
		elif cont==50517:														#	|
			print ("\n"*30,"				[============        ] 60%")		#	|	progreso
		elif cont==58936:														#	|
			print ("\n"*30,"				[==============      ] 70%")		#	|
		elif cont==67356:														#	|
			print ("\n"*30,"				[================    ] 80%")		#	|
		elif cont==75775:														#	|
			print ("\n"*30,"				[==================  ] 90%")		#	|
		elif cont==84195:														#	|
			print ("\n"*30,"				[====================] 100%")		#	/
		
		passwd=crypt(str(i.splitlines()[0]),sal)	#	Es necesario usar splitlines, ya que
													#	al leer el fichero, añade a la cadena
													#	el \n como literal.

		if passwd==cryptpass:		#	Si la palabra encriptada es igual a la clave encriptada:
				
			passwdclear=i			#	Guarda la clave en claro
			passwdtrue=True			#	Notifica que ha encontrado la clave
		
			break					#	Para el bucle

		cont=cont+1					#	Contador para la barra de progreso

if usertrue and passwdtrue==False:		#	Si ha encontrado al usuario pero no la contraseña
	print("\n"*30,"				El usuario es válido, pero no se ha obtenido la contraseña.\n")

elif not usertrue:						#	Si no ha encontrado al usuario
	print("\n"*30,"				El usuario introducido no existe.\n")
else:									#	Si ha encontrado el usuario y la contraseña
	print("\n"*30,"				La contraseña es:	",passwdclear,"\n")