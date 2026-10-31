from matrices import es_matriz, suma_matrices, suma_filas, suma_diagonal,suma_diagonal_secundaria, transponer, multiplicar


def test_es_matriz():
    assert es_matriz([]) is True
    assert es_matriz([[1, 2], [3, 4]]) is True
    assert es_matriz([[], []]) is True
    assert es_matriz([[1, 2], [3]]) is False
    assert es_matriz([[1], [2, 3]]) is False


def test_suma_matrices():
    assert suma_matrices(
        [[1, 2], [3, 4]],
        [[5, 6], [7, 8]],
    ) == [[6, 8], [10, 12]]

    assert suma_matrices(
        [[1, 2, 3], [4, 5, 6]],
        [[9, 8, 7], [6, 5, 4]],
    ) == [[10, 10, 10], [10, 10, 10]]

    assert suma_matrices([[1, 2], [3, 4]], [[5, 6, 7], [8, 9, 10]]) is None
    assert suma_matrices([[1, 2], [3]], [[4, 5], [6, 7]]) is None
    assert suma_matrices([[1], [2]], [[3]]) is None
    assert suma_matrices([], []) == []
    assert suma_matrices([[], []], [[], []]) == [[], []]


def test_suma_filas():
    assert suma_filas([[1, 2, 3], [4, 5, 6]]) == [6, 15]
    assert suma_filas([[1], [2, 3]]) is None
    assert suma_filas([]) == []
    assert suma_filas([[], []]) == [0, 0]


def test_suma_diagonal():
    assert suma_diagonal([[1, 2], [3, 4]]) == 5
    assert suma_diagonal([[1, 2, 3], [4, 5, 6]]) is None
    assert suma_diagonal([[1, 2], [3]]) is None
    assert suma_diagonal([]) == 0
    
def test_suma_diagonal_secundaria():

    # Caso 1: Matriz vacía
    assert suma_diagonal_secundaria([]) == 0

    # Caso 2: Matriz de 1x1
    assert suma_diagonal_secundaria([[5]]) == 5

    # Caso 3: Matriz cuadrada de 2x2
    assert suma_diagonal_secundaria([[1, 2], [3, 4]]) == 5

    # Caso 4: Matriz cuadrada de 3x3
    assert suma_diagonal_secundaria([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]) == 15

    # Caso 5: Matriz cuadrada de 4x4
    assert suma_diagonal_secundaria([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]) == 34

    # Caso 6: Matriz con números negativos
    assert suma_diagonal_secundaria([
        [-1, -2, -3],
        [-4, -5, -6],
        [-7, -8, -9]
    ]) == -15

    # Caso 7: Matriz con números decimales
    assert suma_diagonal_secundaria([
        [1.5, 2.5],
        [3.5, 4.5]
    ]) == 6.0

    # Caso 8: Matriz rectangular
    assert suma_diagonal_secundaria([
        [1, 2, 3],
        [4, 5, 6]
    ]) is None

    # Caso 9: Matriz con filas de distinta longitud
    assert suma_diagonal_secundaria([
        [1, 2],
        [3]
    ]) is None

    # Caso 10: Matriz con filas vacías
    assert suma_diagonal_secundaria([[], []]) is None

def test_transponer():
    assert transponer([[1, 2, 3], [4, 5, 6]]) == [
        [1, 4],
        [2, 5],
        [3, 6],
    ]
    assert transponer([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]
    assert transponer([[1, 2], [3]]) is None
    assert transponer([]) == []
    assert transponer([[], []]) == []

def test_multiplicar():

    # Caso 1: Multiplicación de matrices 1x1
    assert multiplicar([[2]], [[3]]) == [[6]]

    # Caso 2: Multiplicación de matrices 2x2
    assert multiplicar(
        [[1, 2], [3, 4]],
        [[5, 6], [7, 8]]
    ) == [[19, 22], [43, 50]]

    # Caso 3: Multiplicación de matrices 3x3
    assert multiplicar(
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    ) == [[30, 24, 18], [84, 69, 54], [138, 114, 90]]

    # Caso 4: Multiplicación con números decimales
    assert multiplicar(
        [[1.5, 2], [3, 4]],
        [[2, 1], [0.5, 3]]
    ) == [[4.0, 7.5], [8.0, 15]]

    # Caso 5: Matriz con números negativos
    assert multiplicar(
        [[-1, 2], [3, -4]],
        [[2, -3], [-1, 5]]
    ) == [[-4, 13], [10, -29]]

    # Caso 6: Multiplicación por matriz identidad
    assert multiplicar(
        [[1, 2], [3, 4]],
        [[1, 0], [0, 1]]
    ) == [[1, 2], [3, 4]]

    # Caso 7: Multiplicación por matriz de ceros
    assert multiplicar(
        [[1, 2], [3, 4]],
        [[0, 0], [0, 0]]
    ) == [[0, 0], [0, 0]]

    # Caso 8: Matrices incompatibles
    assert multiplicar(
        [[1, 2], [3, 4]],
        [[1, 2, 3], [4, 5, 6]]
    ) is None

    # Caso 9: Primera matriz no válida
    assert multiplicar([[1, 2], [3]], [[1], [2]]) is None

    # Caso 10: Segunda matriz no válida
    assert multiplicar([[1, 2], [3, 4]], [[1, 2], [3]]) is None

    # Caso 11: Ambas matrices vacías
    assert multiplicar([], []) == []

    # Caso 12: Una matriz vacía y otra no
    assert multiplicar([], [[1, 2], [3, 4]]) == []

    # Caso 13: Matrices con filas vacías
    assert multiplicar([[], []], [[], []]) == [[], []]

test_es_matriz()
test_suma_matrices()
test_suma_filas()
test_suma_diagonal()
test_suma_diagonal_secundaria()
test_transponer()
test_multiplicar()
print("Todos los casos de prueba pasaron correctamente.")
