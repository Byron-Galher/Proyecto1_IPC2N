import xml.etree.ElementTree as ET
import Nodo


def ImportarArchivo(ruta):
    import Nodo
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
    

def indent(elem, level=0):
    """Agrega indentación al XML para mejorar la legibilidad."""
    i = "\n" + level * "  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level + 1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

def crear_archivo_salida(matriz_reducida, nombre_archivo):
    matrices = ET.Element("matrices")
    nombre_matriz = matriz_reducida.nombre
    filas = str(matriz_reducida.filas)
    columnas = str(matriz_reducida.columnas)
    
    matriz = ET.SubElement(matrices, "matriz", nombre=nombre_matriz, n=filas, m=columnas)
    
    nodo_actual = matriz_reducida.listaValores.primero
    while nodo_actual:
        fila = str(nodo_actual.valor.fila)
        columna = str(nodo_actual.valor.columna)
        valor = str(nodo_actual.valor.valor)
        ET.SubElement(matriz, "dato", x=fila, y=columna).text = valor
        nodo_actual = nodo_actual.siguiente

    indent(matrices)  # Aplica la función de indentación al XML
    
    tree = ET.ElementTree(matrices)
    with open(nombre_archivo, 'wb') as file:
        tree.write(file, encoding='utf-8', xml_declaration=True)
