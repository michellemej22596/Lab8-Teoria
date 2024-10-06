def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Retorna el índice donde se encuentra el elemento
    return -1  # Retorna -1 si no se encuentra el elemento

# Ejemplo de uso:
arr = [10, 20, 30, 40, 50, 60]
target = 40

resultado = linear_search(arr, target)
if resultado != -1:
    print(f"Elemento encontrado en la posición {resultado}")
else:
    print("Elemento no encontrado")
