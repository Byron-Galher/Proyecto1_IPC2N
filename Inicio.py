from Archivo import ImportarArchivo, crear_archivo_salida
from Graficador import generar_dot
import ProcesarArchivo

menu = ("""
    Menu Principal:
        1. Cargar Archivo
        2. Procesar Archivo
        3. Escribir archivo salida
        4. Mostrar datos del estudiante
        5. Generar Grafica
        6. Salida
        
      """)

while True:
    print(menu)

    respuesta = int(input("Ingrese el # de la opcion que quiere realizar\n"))
    if respuesta == 1:
        ruta = input("Ingrese ruta de archivo\n")
        ArchivoXML = ImportarArchivo(ruta)
    elif respuesta == 2:
        print
        procesar = ProcesarArchivo.crearPatron(ArchivoXML)
        
        nombreM = input("Ingrese nombre de matriz\n")
        matriz = ArchivoXML.busqueda(nombreM)
        matrizPatron = procesar.busqueda(nombreM)
        print("Obtiene matriz a procesar")
        filas = matrizPatron.comparar_filas()
        print("Realiza comparacion de patrones de filas")
        matrizRed = ProcesarArchivo.Prueba(matriz,filas)
        print("Obtiene matriz reducida")
        #imprimir = matrizRed.recorre()
        
    elif respuesta == 3:
        nombreArchivo = input("Ingrese nombre de archivo de salida\n")
        nombreRed = input("Ingrese nombre de matriz\n")
        matrizBusqueda = ArchivoXML.busqueda(nombreRed)
        filas = matrizPatron.comparar_filas()
        matrizRed = ProcesarArchivo.Prueba(matrizBusqueda,filas)
        nombreRed = nombreRed + "_Reducida"
        matrizR = matrizRed.busqueda(nombreRed)
        crear_archivo_salida(matrizRed, nombreArchivo)
        print("Archivo de salida creado")
    elif respuesta == 4:
        print("Nombre: Byron Miguel Galicia Hernandez")
        print("Carnet: 209107177")
        print("Curso: Introduccion a la Programacion y computacion 2 seccion N")
        print("Carrera: Ingenieria en Ciencias y Sistemas")
        print("Semestre: 4to Semestre")
    elif respuesta == 5:
        nombreRed = input("Ingrese nombre de matriz\n")
        matrizBusqueda = ArchivoXML.busqueda(nombreRed)
        filas = matrizPatron.comparar_filas()
        matrizRed = ProcesarArchivo.Prueba(matrizBusqueda,filas)
        nombreRed = nombreRed + "_Reducida"
        matrizR = matrizRed.busqueda(nombreRed)

        if ArchivoXML is not None:            
            if matriz:
                generar_dot(matrizBusqueda, matrizR,"matriz.dot")
            else:
                print("Matriz no encontrada.")
        else:
            print("Primero cargue un archivo.")
    elif respuesta == 6:
        break
    else:
        print("Opcion no valida")
        pass 


