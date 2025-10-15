def fibonacci (n):
    if n==0:
        return 0

    x=0
    y=1
    for i in range(1,n):
        z= x+y
        x=y
        y=z
    return y

y11=fibonacci(11)
print(f"Prueba con n:11 y es: {y11}")

y84=fibonacci(84)
print(f"Prueba con n:84, y es {y84}")

y1531=fibonacci(1531)
print(f"Prueba con n:1531 y es {y1531}")




