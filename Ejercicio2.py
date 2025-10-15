
import random


def bubbleSort(v1):
    cont=0
    for x in range(len(v1)):
        swapped = False
        for j in range(1,len(v1)-x):
            if v1[j] < v1[j-1]:
                t =v1[j]
                v1[j] = v1[j-1]
                v1[j-1] =t
                swapped = True
                cont+=1
                print(f"{v1}, contador {cont}  ")
    
v = [3,2,5,8,4,1]
print (f"Bubble Sort con el vector {v}")
bubbleSort(v)
v2 = [-1,0,4,5,6,7]
print (f"BubbleSort con el vector: {v2}")
bubbleSort(v2)

v3=[]
for x in range(100000):
    r = random.randint(-200,145)
    v3.append(r)
    
print(f"BubbleSort con el vector: {v3}")
bubbleSort(v3)
print(v3)


    
            