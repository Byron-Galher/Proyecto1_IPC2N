from Archivo import ImportarArchivo


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
        pass
    elif respuesta == 3:
        pass
    elif respuesta == 4:
        print("Nombre: Byron Miguel Galicia Hernandez")
        print("Carnet: 209107177")
        print("Curso: Introduccion a la Programacion y computacion 2 seccion N")
        print("Carrera: Ingenieria en Ciencias y Sistemas")
        print("Semestre: 4to Semestre")
    elif respuesta == 5:
        pass
    elif respuesta == 6:
        break 


