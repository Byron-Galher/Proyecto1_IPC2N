def generar_dot(matriz, matrizPatron, archivo_salida):
    filas = int(matriz.filas)
    columnas = int(matriz.columnas)

    filasPatron = int(matrizPatron.filas)
    columnasPatron = int(matrizPatron.columnas)

    with open(archivo_salida, 'w') as f:
        f.write('digraph G {\n')
        f.write('    node [shape=plaintext];\n')
        

        f.write('    tabla_matriz [label=<\n')
        f.write('        <table border="0" cellborder="0" cellspacing="0">\n')


        f.write('            <tr>\n')
        for c in range(1, columnas + 1):
            f.write(f'                <td><b>Columna {c}</b></td>\n')
        f.write('            </tr>\n')

        for p in range(1, filas + 1):
            f.write('<tr>\n')
            for c in range(1, columnas + 1):
                valor = ""
                nodo_actual = matriz.listaValores.primero
                while nodo_actual:
                    if int(nodo_actual.valor.fila) == p and int(nodo_actual.valor.columna) == c:
                        valor = nodo_actual.valor.valor
                        break
                    nodo_actual = nodo_actual.siguiente
                f.write(f'                <td>{valor}</td>\n')
            f.write('            </tr>\n')

        f.write('            <tr>\n')
        f.write(f'                <td colspan="{columnas}"><b>Nombre: {matriz.nombre}</b></td>\n')
        f.write('            </tr>\n')
        f.write('            <tr>\n')
        f.write(f'                <td colspan="{columnas}"><b>Columnas: {columnas}</b></td>\n')
        f.write('            </tr>\n')
        f.write('            <tr>\n')
        f.write(f'                <td colspan="{columnas}"><b>Filas: {filas}</b></td>\n')
        f.write('            </tr>\n')

        f.write('        </table>\n')
        f.write('    >];\n')

        f.write('    tabla_patron [label=<\n')
        f.write('        <table border="0" cellborder="0" cellspacing="0">\n')

        f.write('            <tr>\n')
        for c in range(1, columnasPatron + 1):
            f.write(f'                <td><b>Columna {c}</b></td>\n')
        f.write('            </tr>\n')

        for p in range(1, filasPatron + 1):
            f.write('<tr>\n')
            for c in range(1, columnasPatron + 1):
                valor = ""
                nodo_actual = matrizPatron.listaValores.primero
                while nodo_actual:
                    if int(nodo_actual.valor.fila) == p and int(nodo_actual.valor.columna) == c:
                        valor = nodo_actual.valor.valor
                        break
                    nodo_actual = nodo_actual.siguiente
                f.write(f'                <td>{valor}</td>\n')
            f.write('            </tr>\n')
        f.write('            <tr>\n')
        f.write(f'                <td colspan="{columnasPatron}"><b>Nombre: {matrizPatron.nombre} de Patrones</b></td>\n')
        f.write('            </tr>\n')
        f.write('            <tr>\n')
        f.write(f'                <td colspan="{columnasPatron}"><b>Columnas: {columnasPatron}</b></td>\n')
        f.write('            </tr>\n')
        f.write('            <tr>\n')
        f.write(f'                <td colspan="{columnasPatron}"><b>Filas: {filasPatron}</b></td>\n')
        f.write('            </tr>\n')

        f.write('        </table>\n')
        f.write('    >];\n')
        
        f.write('}\n')