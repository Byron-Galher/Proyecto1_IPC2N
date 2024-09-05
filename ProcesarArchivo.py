class MatrizPatrones:
    def __init__(self,nombre, filas, columnas, listaValores=None):
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas
        self.listaValores = listaValores


    def comparar_filas(self):
        # Lista para almacenar las filas repetidas
        filas = int(self.filas)
        columnas = int(self.columnas)
        filas_repetidas = ListaSimpleFilasRepetidas()
        filas_analizadas = ListaSimpleFilasRepetidas()  # Para marcar filas ya verificadas

        # Iterar sobre las filas de la matriz
        for i in range(1, filas + 1):
            # Extraer valores de la fila actual
            valores_fila_actual = self.obtener_valores_fila(i)
            
            # Verificar si esta fila ya ha sido analizada
            if self.es_fila_analizada(i, filas_analizadas):
                continue  # Saltar si ya fue analizada

            # Comparar la fila actual con las otras filas
            for j in range(i + 1, filas + 1):
                valores_fila_comparar = self.obtener_valores_fila(j)
                # Comparar las filas para ver si son iguales
                if self.comparar_valores(valores_fila_actual, valores_fila_comparar):
                    # Agregar las filas repetidas si aún no están marcadas
                    if not self.es_fila_analizada(i, filas_repetidas):
                        filas_repetidas.insertar(FilasRepetidas(i))
                    if not self.es_fila_analizada(j, filas_repetidas):
                        filas_repetidas.insertar(FilasRepetidas(j))
            
            # Marcar la fila como analizada
            filas_analizadas.insertar(FilasRepetidas(i))
        
        # Imprimir o retornar las filas repetidas
        #filas_repetidas.recorrer()
        return filas_repetidas

    def obtener_valores_fila(self, fila):
        # Extrae los valores de una fila específica en una ListaSimple
        valores = ListaSimple()
        actual = self.listaValores.primero
        while actual:
            if actual.valor.fila == fila:
                valores.insertar(ValorMatrizPatrones(actual.valor.fila, actual.valor.columna, actual.valor.valor))
            actual = actual.siguiente
        return valores

    def comparar_valores(self, lista1, lista2):
        # Compara los valores de dos listas simples de la misma longitud
        nodo1 = lista1.primero
        nodo2 = lista2.primero
        while nodo1 and nodo2:
            if nodo1.valor.valor != nodo2.valor.valor:
                return False
            nodo1 = nodo1.siguiente
            nodo2 = nodo2.siguiente
        return nodo1 is None and nodo2 is None

    def es_fila_analizada(self, fila, lista):
        # Verifica si una fila ya está en la lista de filas analizadas
        actual = lista.primero
        while actual:
            if actual.fila.fila == fila:
                return True
            actual = actual.siguiente
        return False

class ValorMatrizPatrones:
    def __init__(self, fila, columna, valor):
        self.fila = fila
        self.columna = columna
        self.valor = valor

class FilasRepetidas:
    def __init__(self, fila):
        self.fila = fila

class NodoFilasRepetidas:
    def __init__(self, fila=None, siguiente=None):
        self.fila = fila
        self.siguiente = siguiente

class ListaSimpleFilasRepetidas:
    def __init__(self):
        self.primero = None

    def insertar(self, fila):
        if self.primero is None:
            self.primero = NodoFilasRepetidas(fila=fila)
            return

        actual = self.primero

        while actual.siguiente:
            actual = actual.siguiente

        actual.siguiente = NodoFilasRepetidas(fila=fila)

    def recorrer(self):
        actual = self.primero

        while actual != None:
            print(actual.fila.fila)
            actual = actual.siguiente

    def esta_fila_presenta(self, fila):
        actual = self.primero
        while actual:
            if actual.fila.fila == fila:
                return True
            actual = actual.siguiente
        return False

class NodoPatrones:
    def __init__(self, matriz=None, siguiente=None):
        self.matriz = matriz
        self.siguiente = siguiente

class NodoValorPatrones:
    def __init__(self, valor=None, siguiente=None):
        self.valor = valor
        self.siguiente = siguiente

class ListaCircular:
    def __init__(self):
        self.primero = None

    def agregar(self,nodo):
        if self.primero is None:
            self.primero = NodoPatrones(matriz=nodo)
            self.primero.siguiente = self.primero
        else:
            actual = NodoPatrones(matriz=nodo, siguiente=self.primero.siguiente)
            self.primero.siguiente = actual

    def recorre(self):  
        if self.primero is None:
            return
        actual = self.primero
        print("Matriz: ", actual.matriz.nombre, "Filas: ", actual.matriz.filas, "Columnas: ", actual.matriz.columnas)
        fila = 1
        columna = 1
        listaVal = actual.matriz.listaValores
        nodoVal = listaVal.obtenerNodo()
        print(nodoVal.valor.valor, nodoVal.valor.fila, nodoVal.valor.columna)

    def busqueda(self, nombre):
        if self.primero is None:
            return None

        actual = self.primero
        while True:
            if actual.matriz.nombre == nombre:
                return actual.matriz  # Devuelve el objeto Matriz
            actual = actual.siguiente
            if actual == self.primero:  # Salir del bucle si hemos recorrido toda la lista
                break
        return None


class ListaSimple:
    def __init__(self):
       self.primero = None
    
    def insertar(self,valor):
        if self.primero is None:
            self.primero = NodoValorPatrones(valor=valor)
            return
        
        actual = self.primero

        while actual.siguiente:
            actual = actual.siguiente
            
        actual.siguiente = NodoValorPatrones(valor=valor)

    def mostrar_datos(self):
        actual = self.primero

        while actual is not None:
            print("Fila:", actual.valor.fila)
            print("Columna:", actual.valor.columna)
            print("Valor:", actual.valor.valor)
            actual = actual.siguiente
    

def crearPatron(listaCircular):
    actual = listaCircular.primero
    listaPatron = ListaCircular()
    while True:
        matriz = actual.matriz
        filas = int(matriz.filas)
        columnas = int(matriz.columnas)
        listaValores = matriz.listaValores
        ListaSimplePatron = ListaSimple()
        for p in range(1, filas + 1):
            for c in range(1, columnas + 1):
                valor = ""
                nodo_actual = listaValores.primero
                while nodo_actual:
                    # Comparar fila y columna para encontrar el valor correcto
                    if int(nodo_actual.valor.fila) == p and int(nodo_actual.valor.columna) == c:
                        valor = nodo_actual.valor.valor
                        # Convertir valor a "0" o "1" según corresponda
                        if int(valor) == 0:
                            valorPatron = ValorMatrizPatrones(p, c, "0")
                        else:
                            valorPatron = ValorMatrizPatrones(p, c, "1")
                        ListaSimplePatron.insertar(valorPatron)
                        break
                    nodo_actual = nodo_actual.siguiente
                
        listaPatron.agregar(MatrizPatrones(matriz.nombre, matriz.filas, matriz.columnas, ListaSimplePatron))
        actual = actual.siguiente
        if actual == listaCircular.primero:
            return listaPatron
          # Salir del bucle si hemos recorrido toda la lista
    print("Patrones creados")
    return None   

def sumar_filas(matriz, filas_a_sumar):
    """
    Suma los valores de las filas especificadas y devuelve una ListaSimple con los resultados.
    """
    # Crear una lista para almacenar los valores sumados
    suma_fila = ListaSimple()

    # Inicializar valores sumados a cero
    for col in range(1, int(matriz.columnas) + 1):
        suma_fila.insertar(ValorMatrizPatrones(1, col, "0"))
    suma_fila.recorrer()
    # Sumar los valores de las filas especificadas
    actual = matriz.listaValores.primero
    print("Actual: ", actual.valor.valor)
    # Convertir filas_a_sumar a un conjunto para facilitar la búsqueda de filas
    '''filas_set = set()  # Asegúrate de que aquí se obtienen los números de filas
    nodo_filas = filas_a_sumar.primero
    while nodo_filas:
        filas_set.add(nodo_filas.fila)  # Agregar las filas repetidas al conjunto
        nodo_filas = nodo_filas.siguiente

    while actual:
        if actual.valor.fila in filas_set:  # Comprobar si la fila actual está en el conjunto
            # Buscar la posición correspondiente en la lista de suma
            nodo_suma = suma_fila.obtenerNodo()
            while nodo_suma:
                if nodo_suma.valor.columna == actual.valor.columna:
                    nodo_suma.valor.valor = str(int(nodo_suma.valor.valor) + int(actual.valor.valor))
                    break
                nodo_suma = nodo_suma.siguiente
        actual = actual.siguiente

    return suma_fila'''

def crear_matriz_reducida(matriz, filas_a_sumar):
    """
    Crea una nueva matriz reducida sumando filas especificadas y reorganizando las filas restantes.
    """
    # Sumar las filas especificadas
    suma_fila = sumar_filas(matriz, filas_a_sumar)

    # Crear una lista para los valores de la nueva matriz
    nueva_lista_valores = ListaSimple()

    # Insertar la fila sumada como la primera fila
    nodo_suma = suma_fila.obtenerNodo()
    while nodo_suma:
        nueva_lista_valores.insertar(ValorMatrizPatrones(1, nodo_suma.valor.columna, nodo_suma.valor.valor))
        nodo_suma = nodo_suma.siguiente

    # Agregar las filas que no fueron sumadas, asignándoles nuevas posiciones
    fila_nueva = 2
    actual = matriz.listaValores.primero
    while actual:
        if actual.valor.fila not in filas_a_sumar:
            nueva_lista_valores.insertar(ValorMatrizPatrones(fila_nueva, actual.valor.columna, actual.valor.valor))
            if actual.valor.columna == matriz.columnas:
                fila_nueva += 1
        actual = actual.siguiente

    # Crear la nueva matriz con las filas sumadas y restantes
    nueva_matriz = MatrizPatrones(matriz.nombre + "_Reducida", fila_nueva - 1, matriz.columnas, nueva_lista_valores)
    return nueva_matriz


def Prueba(matriz, filas_a_sumar):
    filasM = int(matriz.filas)
    columnasM = int(matriz.columnas)
    listaValores = matriz.listaValores

    listaFilasRepetidas = ListaSimple()
    filaRep = filas_a_sumar.primero
    contadorFilas = 0

    # Recorrer cada fila repetida
    while filaRep:
        fila_actual = int(filaRep.fila.fila)
        nodo_actual = listaValores.primero
        
        # Recorrer los valores de listaValores
        while nodo_actual:
            if int(nodo_actual.valor.fila) == fila_actual:
                listaFilasRepetidas.insertar(ValorMatrizPatrones(
                    nodo_actual.valor.fila, 
                    nodo_actual.valor.columna, 
                    nodo_actual.valor.valor
                ))
            nodo_actual = nodo_actual.siguiente
        contadorFilas += 1
        filaRep = filaRep.siguiente

    # Crear una nueva lista para almacenar la suma de valores por columna
    nueva_lista = ListaSimple()
    columna_actual = 1

    while columna_actual <= columnasM:
        suma_columna = 0
        nodo_actual = listaFilasRepetidas.primero
        
        # Sumar los valores de la misma columna
        while nodo_actual:
            if int(nodo_actual.valor.columna) == columna_actual:
                suma_columna += int(nodo_actual.valor.valor)
            nodo_actual = nodo_actual.siguiente
        
        # Insertar la suma en la nueva lista
        nueva_lista.insertar(ValorMatrizPatrones(1, columna_actual, suma_columna))  # Usamos fila = 1 para representar la fila resultante
        
        columna_actual += 1
    
    # Imprimir los resultados de la nueva lista
    actual = nueva_lista.primero
    numeroFilas = 0
    while actual:
        numeroFilas += 1
        actual = actual.siguiente

    # Crear la matriz reducida
    filasMatrizReducida = (filasM - contadorFilas) + 1
    matriz_reducida = ListaCircular()
    listaValoresReducida = ListaSimple()
    filaRep = filas_a_sumar.primero

    # Recorrer los valores restantes de la matriz original
    '''while filaRep:
        fila_actual = int(filaRep.fila.fila)
        nodo_actual = listaValores.primero

        for p in range(1, filasM + 1):
            for c in range(1, columnasM + 1):
                valor = ""
                nodo_actual = listaValores.primero
                while nodo_actual:
                    # Comparar fila y columna para encontrar el valor correcto
                    if int(nodo_actual.valor.fila) == p and int(nodo_actual.valor.columna) == c:
                        if int(nodo_actual.valor.fila) == filaRep.fila.fila:
                            pass
                        else:
                            valorPatron = ValorMatrizPatrones(p+numeroFilas, c, nodo_actual.valor.valor)
                        listaValoresReducida.insertar(valorPatron)
                        break
                    nodo_actual = nodo_actual.siguiente
        filaRep = filaRep.siguiente'''
    #agregar a lista de valores reducida
    nueva_lista_actual = nueva_lista.primero
    while nueva_lista_actual:
        listaValoresReducida.insertar(nueva_lista_actual.valor)
        nueva_lista_actual = nueva_lista_actual.siguiente
    
    contadorFilas = filasM
    validar = True
    while validar:
        
        fila_actual = int(filaRep.fila.fila)
        nodo_actual = listaValores.primero
        
        for p in range(1, filasM + 1):
            for c in range(1, columnasM + 1):
                nodo_actual = listaValores.primero
                while nodo_actual:
                    # Comparar fila y columna para encontrar el valor correcto
                    if int(nodo_actual.valor.fila) == p and int(nodo_actual.valor.columna) == c:
                        if int(nodo_actual.valor.fila) != fila_actual:
                            print("Fila", nodo_actual.valor.fila, "Columna", nodo_actual.valor.columna, "Valor", nodo_actual.valor.valor)
                            valorPatron = ValorMatrizPatrones(p + contadorFilas, c, nodo_actual.valor.valor)
                            listaValoresReducida.insertar(valorPatron)
                        break  # Salir del bucle interno para evitar múltiples inserciones
                    nodo_actual = nodo_actual.siguiente
            contadorFilas =-1
        filaRep = filaRep.siguiente
        if filaRep is None and contadorFilas >  0:
            validar = True
        else:
            validar = False
    
    # Crear la matriz reducida
    matriz_reducida.agregar(MatrizPatrones(
        matriz.nombre + "_Reducida",
        filasMatrizReducida,
        matriz.columnas,
        listaValoresReducida
    ))


    return matriz_reducida