import time

def function(n):
    counter = 0
    for i in range(n//2, n+1):
        for j in range(1, n//2 + 1):
            num_k_iterations = int(n).bit_length()  # Optimiza el bucle de k
            counter += num_k_iterations

# Tamaños de input (los originales)
input_sizes = [1, 10, 100, 1000, 10000, 100000, 1000000]
execution_times = []

for size in input_sizes:
    print(f"Ejecutando función para tamaño de entrada: {size}")
    start_time = time.time()  # Inicia el temporizador
    function(size)            # Ejecuta la función con el tamaño actual
    end_time = time.time()    # Termina el temporizador
    exec_time = end_time - start_time
    execution_times.append(exec_time)  # Calcula el tiempo de ejecución
    print(f"Tamaño {size} completado en {exec_time:.6f} segundos")

# Mostrar resultados en tabla
print("Tamaño de input | Tiempo de ejecución (s)")
for size, exec_time in zip(input_sizes, execution_times):
    print(f"{size:<15} | {exec_time:.6f}")
