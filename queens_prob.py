n = 43

def main():
    board = []
    for i in range(n):
        row = [numerate(i,j,n) for j in range(n)]
        board += [row]


    for r in board:
        print(r)


    auto_check(board)

def auto_check(b):
    if tiene_repetidos_en_diagonales(b):
        print("hay repeticion en diagonales")

    elif tiene_repetidos_en_fila_o_columna(b):
        print("Hay repetidos en filas o columnas")
    else:
        print("todo gudw")
    return


def tiene_repetidos_en_fila_o_columna(tablero):
    n = len(tablero)
    # Verificar filas
    for fila in tablero:
        if len(fila) != len(set(fila)):
            return True  # Hay un número repetido en esta fila

    # Verificar columnas
    for columna in range(n):
        columna_vals = [tablero[fila][columna] for fila in range(n)]
        if len(columna_vals) != len(set(columna_vals)):
            return True  # Hay un número repetido en esta columna
    
    return False  # No se encontraron números repetidos en filas o columnas

def tiene_repetidos_en_diagonales(tablero):
    n = len(tablero)
    diagonal_principal = [tablero[i][i] for i in range(n)]
    diagonal_secundaria = [tablero[i][n-1-i] for i in range(n)]

    if len(set(diagonal_principal)) != len(diagonal_principal):
        return True  # Hay un número repetido en la diagonal principal
    
    if len(set(diagonal_secundaria)) != len(diagonal_secundaria):
        return True  # Hay un número repetido en la diagonal secundaria

    return False  # No se encontraron números repetidos en las diagonales


def numerate(i, j, n):
    result = (j + 2 * i) % n
    return result


if __name__ == "__main__":
    main()
