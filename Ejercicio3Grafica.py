import matplotlib.pyplot as plt

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

def numero_aureo(a):
    if a <= 1:
        return 1
    return fibonacci(a) / fibonacci(a-1)


num_aureos=[]
for x in range (2,9):
    num_aureos.append(numero_aureo(x))

n=[2,3,4,5,6,7,8]

num_Aureo_Real=(1 + 5 ** 0.5) / 2  



fig, (ax_tabla, ax_graf) = plt.subplots(1, 2, figsize=(10, 4), gridspec_kw={'width_ratios': [1, 2]})


ax_tabla.axis('off')  

tabla_datos = list(zip(n, num_aureos))
nombres_columna = ["N", "Número Áureo"]

tabla = ax_tabla.table(cellText=tabla_datos,
                       colLabels=nombres_columna,
                       loc='center',
                       colColours=["#FF00FF"]*len(nombres_columna),
                       cellLoc='center',
                       bbox=[-0.7, 0, 1.7, 1] )

tabla.auto_set_font_size(False)
tabla.set_fontsize(12)
tabla.scale(1, 1.5)


ax_graf.plot(n, num_aureos, marker='o', linestyle='-', color='#FF00FF')
ax_graf.set_xlabel('N')
ax_graf.set_ylabel('Número Áureo')
ax_graf.grid(True)
ax_graf.axhline(y=num_Aureo_Real, color='red', linestyle='--', linewidth=1)
ax_graf.text(8.1, num_Aureo_Real, 'φ ≈ 1.618', color='red', va='center')

plt.tight_layout()
plt.show()

