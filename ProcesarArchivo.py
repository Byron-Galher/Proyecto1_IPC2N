class MatrizPatrones:
    def __init__(self,nombre, filas, columnas, listaValores=None):
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas
        self.listaValores = listaValores

class ValorMatrizPatrones:
    def __init__(self, fila, columna, valor):
        self.fila = fila
        self.columna = columna
        self.valor = valor

class NodoPatrones:
    def __init__(self, matriz=None, siguiente=None):
        self.matriz = matriz
        self.siguiente = siguiente

class NodoValorPatrones:
    def __init__(self, valor=None, siguiente=None):
        self.valor = valor
        self.siguiente = siguiente

class ListaCircular:
    def __init__(self,):
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
        'actual.matriz.listaValores.recorrer()'
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

    def recorrer(self):
        actual = self.primero

        while actual != None:
            fila = 1
            columna = 1
            while fila <= int(actual.valor.fila) and columna <= int(actual.valor.columna):
                if int(actual.valor.fila) == fila:
                    print(actual.valor.valor," ")
                    columna += 1
                if int(actual.valor.fila) == fila and int(actual.valor.columna) == columna:
                    print(actual.valor.valor,"\n")
                    columna += 1
                    fila += 1
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
                '''while nodo_actual:
                    if int(nodo_actual.valor.valor) == 0:
                        valorP = nodo_actual.valor.valor
                        valorPatron = ValorMatrizPatrones(p, c, "0")
                        ListaSimplePatron.insertar(valorPatron)
                        nodo_actual = nodo_actual.siguiente
                    elif int(nodo_actual.valor.valor) >= 1:
                        valor = nodo_actual.valor.valor
                        valorPatron = ValorMatrizPatrones(p, c, "1")
                        ListaSimplePatron.insertar(valorPatron)
                        nodo_actual = nodo_actual.siguiente
                    nodo_actual = nodo_actual.siguiente'''
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

