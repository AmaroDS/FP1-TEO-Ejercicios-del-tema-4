def es_matriz(matriz: list[list[int | float]]) -> bool:
    """
    Comprueba si una lista de listas representa una matriz válida.

    Parámetros:
    matriz (list[list[int | float]]): Lista de listas que se quiere comprobar.

    Devuelve:
    bool: True si todas las filas tienen el mismo número de elementos.
    """
    if len(matriz) == 0:
        return True
    # TODO: Ejecutar con el depurador
    # Esto es un esquema de para todo
    num_columnas = len(matriz[0])

    es_rectangular = True
    for fila in matriz[1:]:
        # Si NO se cumple la condicion
        if len(fila) != num_columnas:
            es_rectangular = False
            break
    return es_rectangular


    

def suma_matrices(
    m1: list[list[int | float]], m2: list[list[int | float]]
) -> list[list[int | float]] | None:
    """
    Suma dos matrices de las mismas dimensiones.

    Parámetros:
    m1 (list[list[int | float]]): Primera matriz.
    m2 (list[list[int | float]]): Segunda matriz.

    Devuelve:
    list[list[int | float]] | None: Matriz resultante, o None si las matrices
    no son válidas o tienen dimensiones distintas.
    """

    if not es_matriz(m1) or not es_matriz(m2):
        return None

    if len(m1) != len(m2):
        return None

    res = []

    for i in range(len(m1)):
        captura_filas = []
        j = 0
        if len(m1[i]) != len(m2[i]):
            return None
        while j < len(m1[i]):
            captura_filas.append(m1[i][j] + m2[i][j])
            j +=1
        res.append(captura_filas)
    return res

def suma_filas(
    matriz: list[list[int | float]],
) -> list[int | float] | None:
    """
    Suma los elementos de cada fila de una matriz.

    Parámetros:
    matriz (list[list[int | float]]): Matriz cuyos elementos se sumarán.

    Devuelve:
    list[int | float] | None: Lista con la suma de cada fila, o None si la
    matriz no es válida.
    """
    if not es_matriz(matriz):
        return None

    res = []
    for i in range(len(matriz)):
        j = 0
        suma = 0
        while j < len(matriz[i]):
            suma += matriz[i][j]
            j += 1
        res.append(suma)
    return res


def suma_diagonal(matriz: list[list[int | float]]) -> int | float | None:
    """
    Suma los elementos de la diagonal principal de una matriz cuadrada.

    Parámetros:
    matriz (list[list[int | float]]): Matriz cuadrada de números.

    Devuelve:
    int | float | None: Suma de la diagonal, o None si la matriz no es válida
    o no es cuadrada.
    """
    if not es_matriz(matriz):
        return None

    if matriz == []:
        return 0

    if len(matriz) != len(matriz[0]):
        return None

    res = 0
    for i in range(len(matriz)):
        res += matriz[i][i]
    return res


def suma_diagonal_secundaria(matriz: list[list[int | float]]) -> int | float | None:
    '''
    Devuelve la suma de la diagonal secundaria
    '''
    if not es_matriz(matriz):
        return None

    if matriz == []:
        return 0

    if len(matriz) != len(matriz[0]):
        return None

    suma = 0
    numero_elementos = len(matriz)
    for i in range(numero_elementos):
        if i == numero_elementos:
            break
        suma += matriz[i][numero_elementos-1-i]
    return suma

def transponer(
    matriz: list[list[int | float]],
) -> list[list[int | float]] | None:
    """
    Devuelve la matriz transpuesta.

    Parámetros:
    matriz (list[list[int | float]]): Matriz que se quiere transponer.

    Devuelve:
    list[list[int | float]] | None: Matriz transpuesta, o None si la matriz
    no es válida.
    """
    if not es_matriz(matriz):
        return None

    if matriz == []:
        return []

    res = []

    num_filas = len(matriz)
    num_columnas = len(matriz[0])

    for i in range(num_columnas):
        j=0
        captura = []
        for j in range(num_filas):
            captura.append(matriz[j][i])
        res.append(captura)
    
    return res

def multiplicar(m1: list[list[int | float]], m2: list[list[int | float]]
) -> list[list[int | float]] | None:
    '''
    Devuelve la matriz multiplicación m1xm2.
    '''
    if not es_matriz(m1) or not es_matriz(m2):
        return None
    
    num_filas= len(m1)
    num_columnas = len(m2[0])
    if num_filas != num_columnas:
        return None

    if m1 == []:
        return[]

    res = []
    captura = []
    while i < len(num_filas):
        j=0
        suma=0
        for j in range(num_columnas):
            suma += m1[i][j]*m2[j][i]
        captura.append(suma)
    res.append(captura)

    return res
    

    # TODO: Para casa