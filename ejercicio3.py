#Ejercicio 3
# Inciso b)

import time

def function(n):
    for i in range(1, n//3 + 1):
        for j in range(1, n + 1, 4):
            print("Sequence")

# Método de profiling y medición del tiempo
input_sizes = [1, 10, 100, 1000, 10000, 100000]
execution_times = []

for n in input_sizes:
    start_time = time.time()
    function(n)
    end_time = time.time()
    execution_time = end_time - start_time
    execution_times.append(execution_time)
    print(f"n = {n}, tiempo de ejecución = {execution_time:.5f} segundos")

# Mostrar los resultados en una tabla
print("\nTamaño de input (n) | Tiempo de ejecución (segundos)")
for i, n in enumerate(input_sizes):
    print(f"{n:<20} | {execution_times[i]:.5f}")
