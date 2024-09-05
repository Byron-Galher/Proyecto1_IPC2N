import xml.etree.ElementTree as ET
import Nodo


def ImportarArchivo(ruta):
    import Nodo  # Importar aquí para evitar problemas de importación circular
    import xml.etree.ElementTree as ET

    archivo = ET.parse(ruta)
    root = archivo.getroot()

    listaMatrices = Nodo.ListaCircular()

    for matriz in root.findall('matriz'):
        nombre = matriz.get('nombre')
        filas = matriz.get('n')
        columnas = matriz.get('m')

        vMatriz = Nodo.Matriz(nombre, filas, columnas, None)
        listaValores = Nodo.ListaSimple()
        
        for valor in matriz.findall('dato'):
            fila = valor.get('x')
            columna = valor.get('y')
            valor1 = valor.text
            listaValores.insertar(Nodo.ValorMatriz(fila, columna, valor1))

        vMatriz.listaValores = listaValores
        listaMatrices.agregar(vMatriz)

    return listaMatrices
    

def crear_archivo_salida(matriz_reducida, nombre_archivo):
    # Crear el elemento raíz
    matrices = ET.Element("matrices")

    # Extraer los valores de la matriz reducida
    matriz_actual = matriz_reducida.primero
    while matriz_actual:
        matriz = ET.SubElement(matrices, "matriz", nombre=matriz_actual.valor.nombre, n=str(matriz_actual.valor.filas), m=str(matriz_actual.valor.columnas))
        
        nodo_actual = matriz_actual.valor.listaValores.primero
        while nodo_actual:
            # Crear un elemento "dato" para cada valor en la matriz
            ET.SubElement(matriz, "dato", x=str(nodo_actual.valor.fila), y=str(nodo_actual.valor.columna)).text = str(nodo_actual.valor.valor)
            nodo_actual = nodo_actual.siguiente
        
        matriz_actual = matriz_actual.siguiente

    # Crear el árbol XML y escribir en el archivo
    tree = ET.ElementTree(matrices)
    with open(nombre_archivo, 'wb') as file:
        tree.write(file)
