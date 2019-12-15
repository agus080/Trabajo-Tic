# -*- utf-8 -*-
import os
import zipfile
import getpass
continuar=True
archivoBorra=0
opcion = 0
numearchivo=0
lista=[]
listaRespuestas=[]
listaArchivos=[]
def opciones():
	opcion=5
	try:
		print('1. Mostrar archivos superiores en tamaño a uno especificado')
		print('2. Borrar archivos superiores en tamaño a uno especificado')
		print('3. Comprimir un fichero o carpeta especificada')
		print('4. Borrar los archivos temporales de nuestro navegador')
		print('5. Salir del programa')
		opcion=int(input('Introduzca opción: '))
	except:
		print("¡Solo números!")
		
	return opcion
def leerPeso():
	try:
		peso = int(input('Dime el peso que buscas: '))
	except:
		print('El peso debe ser un número')
	return peso

	
while (opcion!=5) and (continuar==True):
	opcion=opciones()

#La primera opción nos dirá los archivos superiores a un tamaño especificado.
	if opcion==1:
		peso=leerPeso()
		ruta=input('Dime la ruta del archivo: ')
		os.chdir(ruta)
		lista=os.listdir(ruta)
		listaRespuestas.append('Estos son los archivos en relación con el tamaño indicado: ')
		for archivo in lista:
			tamanoarchivo = int(os.path.getsize(archivo))
			if tamanoarchivo>peso:
				print('El archivo %s es mayor que el archivo dado'%archivo)
				respuesta=('El archivo %s es mayor que el archivo dado'%archivo)
				listaRespuestas.append(respuesta)
			elif tamanoarchivo<peso:
				print('El archivo %s es menor que el archivo dado'%archivo)
				respuesta=('El archivo %s es menor que el archivo dado'%archivo)
				listaRespuestas.append(respuesta)
			else:
				print('Son iguales')
				respuesta=('Son iguales')
				listaRespuestas.append(respuesta)	
#La segunda opción borrará los archivos superiores al tamaño que especifiquemos.	
	elif opcion==2:
		peso=leerPeso()
		ruta=input('Dime la ruta del archivo: ')
		os.chdir(ruta)
		lista=os.listdir(ruta)
		for archivo in lista:
			tamanoarchivo = int(os.path.getsize(archivo))
			if tamanoarchivo>peso:
				os.remove(archivo)
				numearchivo=numearchivo+1
				listaArchivos.append(archivo)
		respuesta=str('Hay %i archivos, y son los siguientes: ' %numearchivo)
		listaRespuestas.append(respuesta)
		for archivo in listaArchivos:
			listaRespuestas.append(archivo)
#La tercera comprimirá un archivo o carpeta especificado.
	elif opcion==3:
		ruta=input('Dime la ruta del archivo: ')
		os.chdir(ruta)
		archivo=input('Dime el nombre del archivo: ')
		compressedfile='comprimido.zip'
		comprimido = zipfile.ZipFile(compressedfile,'w', zipfile.ZIP_DEFLATED)
		comprimido.write(archivo)
		comprimido.close()
		respuesta= ('Se ha comprimido el archivo %s' %archivo)
		listaRespuestas.append(respuesta)
#La cuarta borrará los archivos temporales de nuestro navegador.
	elif opcion==4:
		print('Debe cerrar el navegador')
		
		respuesta1 = input('¿Está seguro de que quiere borrarlo?(Si/No): ')
		respuesta1=='si' or 'no'
		respuesta2=respuesta1.lower()
		if respuesta2 == 'si':
			username = getpass.getuser()
			a = ('C:\\Users\\')
			b = ('\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cache')
			lista=os.listdir(a+username+b)
			os.chdir(a+username+b)
			for archivo2 in lista:
				os.remove(archivo2)
				archivoBorra=archivoBorra+1
			respuesta=('Se han eliminado los archivos temporales')
			listaRespuestas.append(respuesta)
#La cuarta nos hará salir del programa.
	
	respuestafinal = input('¿Desea realizar algo más?(Si/No): ')
	respuestafinal2=respuestafinal.lower()
	if respuestafinal2 == 'si':
		continuar=True
	else:
		continuar=False
rutaCodigo=input('Dime la ruta en la que deseas el registro: ')
os.chdir(rutaCodigo)
fichero=open('.\\registro.log','w')
for puesto in listaRespuestas:
	fichero.write(puesto)
	fichero.write('\n')
fichero.close()
