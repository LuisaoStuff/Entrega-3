#	Pedir contraseña y usuario. Leer el fichero /etc/shadow y comprobar si existe o no.

from crypt import crypt

user=str(input("\n		Dame un usuario: "))
passwd=str(input("		Dame una contraseña:	"))

usertrue=False
passwdtrue=False

with open("shadow","r") as fichero:

	for linea in fichero:

		if linea.split(":")[0]==user:

			usertrue=True

			if crypt(passwd,linea.split(":")[1][0:12])==linea.split(":")[1]:
				print("		Usuario y contraseña válidos.\n")
				passwdtrue=True

if usertrue and passwdtrue==False:
	print("		El usuario es válido, pero la contraseña es incorrecta.\n")

elif not usertrue:
	print("		El usuario introducido no existe.\n")
