import matplotlib.pyplot as plt
suma=1
n=[]
resultados=[]
for x in range (1,20):    
    suma+=1/x
    n.append(x)
    resultados.append(suma)

fig, ax_graf=plt.subplots(figsize=(8, 5))
ax_graf.plot(n, resultados, marker='o', linestyle='-', color='#FF00FF')
ax_graf.set_xlabel('N')
ax_graf.set_ylabel('Suma de la serie')
ax_graf.grid(True)
plt.show()