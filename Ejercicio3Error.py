import math

def fibonacci(n):
    if n == 0:
        return 0
    x = 0
    y = 1
    for i in range(1, n):
        z = x + y
        x = y
        y = z
    return y

numReal = (1 + math.sqrt(5)) / 2 

for x in range(2, 100):
    numerador = fibonacci(x)
    denominador = fibonacci(x - 1)
    numAprox = numerador/denominador
    error_abs =abs(numReal-numAprox)/numReal

    if error_abs <= 10**-5:
        print(f"LLego en {x} intentos")
        break