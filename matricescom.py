def mostrar_menu():
    print("\n\033[1;34m=== MENÚ PRINCIPAL ===\033[0m")
    print("1. \033[1;32mCrear una matriz\033[0m")
    print("2. \033[1;32mMostrar matrices\033[0m")
    print("3. \033[1;32mSumar dos matrices\033[0m")
    print("4. \033[1;32mRestar dos matrices\033[0m")
    print("5. \033[1;32mMultiplicar dos matrices\033[0m")
    print("6. \033[1;31mSalir\033[0m")

def crear_matriz():
    try:
        filas = int(input("\033[1;33mNúmero de filas: \033[0m"))
        columnas = int(input("\033[1;33mNúmero de columnas: \033[0m"))
        print(f"\033[1;36mIngrese los elementos de la matriz ({filas}x{columnas}), fila por fila:\033[0m")
        matriz = []
        for i in range(filas):
            fila = list(map(int, input(f"\033[1;35mFila {i+1}: \033[0m").split()))
            if len(fila) != columnas:
                print("\033[1;31mError: Debes ingresar exactamente\033[0m", columnas, "\033[1;31mvalores.\033[0m")
                return None
            matriz.append(fila)
        return matriz
    except ValueError:
        print("\033[1;31mError: Debes ingresar valores numéricos.\033[0m")
        return None

def mostrar_matrices(matrices):
    if not matrices:
        print("\033[1;31mNo hay matrices almacenadas.\033[0m")
        return
    for i, matriz in enumerate(matrices):
        print(f"\n\033[1;34mMatriz {i+1}:\033[0m")
        for fila in matriz:
            print(" ".join(map(str, fila)))

def seleccionar_matrices(matrices):
    if len(matrices) < 2:
        print("\033[1;31mError: Se necesitan al menos dos matrices almacenadas.\033[0m")
        return None, None
    mostrar_matrices(matrices)
    try:
        i1 = int(input("\033[1;33mSeleccione el número de la primera matriz: \033[0m")) - 1
        i2 = int(input("\033[1;33mSeleccione el número de la segunda matriz: \033[0m")) - 1
        if 0 <= i1 < len(matrices) and 0 <= i2 < len(matrices):
            return matrices[i1], matrices[i2]
        else:
            print("\033[1;31mError: Selección inválida.\033[0m")
            return None, None
    except ValueError:
        print("\033[1;31mError: Debes ingresar números válidos.\033[0m")
        return None, None

def sumar_matrices(matriz1, matriz2):
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        print("\033[1;31mError: Las matrices deben tener las mismas dimensiones para sumar.\033[0m")
        return None
    resultado = []
    for i in range(len(matriz1)):
        fila = [matriz1[i][j] + matriz2[i][j] for j in range(len(matriz1[0]))]
        resultado.append(fila)
    return resultado

def restar_matrices(matriz1, matriz2):
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        print("\033[1;31mError: Las matrices deben tener las mismas dimensiones para restar.\033[0m")
        return None
    resultado = []
    for i in range(len(matriz1)):
        fila = [matriz1[i][j] - matriz2[i][j] for j in range(len(matriz1[0]))]
        resultado.append(fila)
    return resultado

def multiplicar_matrices(matriz1, matriz2):
    if len(matriz1[0]) != len(matriz2):
        print("\033[1;31mError: El número de columnas de la primera matriz debe coincidir con el número de filas de la segunda.\033[0m")
        return None
    resultado = []
    for i in range(len(matriz1)):
        fila_resultado = []
        for j in range(len(matriz2[0])):
            suma_producto = sum(matriz1[i][k] * matriz2[k][j] for k in range(len(matriz2)))
            fila_resultado.append(suma_producto)
        resultado.append(fila_resultado)
    return resultado

# Programa principal
def main():
    matrices = []
    while True:
        mostrar_menu()
        try:
            opcion = int(input("\033[1;33mSeleccione una opción: \033[0m"))
        except ValueError:
            print("\033[1;31mError: Debes ingresar un número válido.\033[0m")
            continue

        if opcion == 1:
            nueva_matriz = crear_matriz()
            if nueva_matriz is not None:
                matrices.append(nueva_matriz)
                print("\033[1;32mMatriz creada exitosamente.\033[0m")
        elif opcion == 2:
            mostrar_matrices(matrices)
        elif opcion == 3:
            matriz1, matriz2 = seleccionar_matrices(matrices)
            if matriz1 and matriz2:
                resultado = sumar_matrices(matriz1, matriz2)
                if resultado is not None:
                    print("\n\033[1;32mResultado de la suma:\033[0m")
                    for fila in resultado:
                        print(" ".join(map(str, fila)))
        elif opcion == 4:
            matriz1, matriz2 = seleccionar_matrices(matrices)
            if matriz1 and matriz2:
                resultado = restar_matrices(matriz1, matriz2)
                if resultado is not None:
                    print("\n\033[1;32mResultado de la resta:\033[0m")
                    for fila in resultado:
                        print(" ".join(map(str, fila)))
        elif opcion == 5:
            matriz1, matriz2 = seleccionar_matrices(matrices)
            if matriz1 and matriz2:
                resultado = multiplicar_matrices(matriz1, matriz2)
                if resultado is not None:
                    print("\n\033[1;32mResultado de la multiplicación:\033[0m")
                    for fila in resultado:
                        print(" ".join(map(str, fila)))
        elif opcion == 6:
            print("\033[1;34mSaliendo del programa. ¡Hasta luego!\033[0m")
            break
        else:
            print("\033[1;31mOpción inválida, intente de nuevo.\033[0m")

if __name__ == "__main__":
    main()