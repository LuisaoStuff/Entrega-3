#	La funcion declarada al inicio es para eliminar algunas cadenas que aparecen en todas
#	las lineas del archivo html y así mostrarlas por pantalla más limpias.
#	Tambien he usado la funcion .decode('UTF-8') para eliminar algunos caracteres.

def limpiar(dato):
	dato=dato.strip()
	dato=dato.replace(" ","")
	dato=dato.replace("<td>","")
	dato=dato.replace("</td>","")
	dato=dato.replace("&","")
	return dato

from urllib.request import urlopen
response = urlopen('http://tiempoytemperatura.es/espana/sevilla/dos-hermanas.html#ahora')
lineas=response.readlines()

for i in range(0,len(lineas)):
	if lineas[i].decode('UTF-8').find("Ahora")!=-1 and lineas[i+1].decode('UTF-8').find("class")!=-1:
		
		presion=limpiar(lineas[i+8].decode('UTF-8'))
		humedad=limpiar(lineas[i+7].decode('UTF-8'))
		temperatura=limpiar(lineas[i+2].decode('UTF-8'))[16:18:]
		
		break

print("\n		Tiempo atmosférico actual en Dos Hermanas:")
print("\n		Temperatura:",temperatura,"ºC\n		Presión:",presion,"\n		Humedad:",humedad,"\n")

