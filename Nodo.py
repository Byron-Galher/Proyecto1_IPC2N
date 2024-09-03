class Matriz:
    def __init__(self,nombre, filas, columnas, listaValores=None):
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas
        self.listaValores = listaValores

class ValorMatriz:
    def __init__(self, fila, columna, valor):
        self.fila = fila
        self.columna = columna
        self.valor = valor

class Nodo:
    def __init__(self, matriz=None, siguiente=None):
        self.matriz = matriz
        self.siguiente = siguiente

class NodoValor:
    def __init__(self, valor=None, siguiente=None):
        self.valor = valor
        self.siguiente = siguiente
        

class ListaCircular:
    def __init__(self,):
        self.primero = None

    def agregar(self,nodo):
        if self.primero is None:
            self.primero = Nodo(matriz=nodo)
            self.primero.siguiente = self.primero
        else:
            actual = Nodo(matriz=nodo, siguiente=self.primero.siguiente)
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
        
        while listaVal != None:
            while fila <= int(actual.matriz.filas) and columna <= int(actual.matriz.columnas):
                    if int(actual.valor.fila) == fila:
                        print(actual.valor.valor," ")
                        columna += 1
                    if int(actual.valor.fila) == fila and int(actual.valor.columna) == columna:
                        print(actual.valor.valor,"\n")
                        columna += 1
                        fila += 1
        while actual.siguiente != self.primero:
            actual = actual.siguiente
            print("Matriz: ", actual.matriz.nombre, "Filas: ", actual.matriz.filas, "Columnas: ", actual.matriz.columnas)
            'actual.matriz.listaValores.recorrer()'


class ListaSimple:
    def __init__(self):
       self.primero = None
    
    def insertar(self,valor):
        if self.primero is None:
            self.primero = NodoValor(valor=valor)
            return
        
        actual = self.primero

        while actual.siguiente:
            actual = actual.siguiente
            
        actual.siguiente = NodoValor(valor=valor)

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

            '''for i in range(1,int(actual.valor.fila)):
                if int(actual.valor.fila) == i:
                    print(actual.valor.valor," ")
                for j in range(1,int(actual.valor.columna)):
                    if int(actual.valor.columna) == j:
                        print(actual.valor.valor," ")'''
            'print("Fila: ", actual.valor.fila, "Columna: ", actual.valor.columna, "Valor: ", actual.valor.valor)'
            
            actual = actual.siguiente