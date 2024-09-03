import xml.etree.ElementTree as ET
import Nodo


def ImportarArchivo(ruta):
    archivo = ET.parse(ruta)

    root = archivo.getroot()

    listaMatrices = Nodo.ListaCircular()

    for matriz in root.findall('matriz'):
        nombre = matriz.get('nombre')
        filas = matriz.get('n')
        columnas = matriz.get('m')

        vMatriz = Nodo.Matriz(nombre,filas, columnas, None)

        listaValores = Nodo.ListaSimple()
        for valor in matriz.findall('dato'):
            fila = valor.get('x')
            columna = valor.get('y')
            valor1 = valor.text

            listaValores.insertar(Nodo.ValorMatriz(fila,columna,valor1))
            
        vMatriz.listaValores = listaValores

        listaMatrices.agregar(vMatriz)

    listaMatrices.recorre()

    pass
    


