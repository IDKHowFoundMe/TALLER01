
num=1
suma=0
cont=1
for x in range(1,20):
    suma+=1/num
    num=num*2
    if(abs(suma-2)<10**-1):
        print (x)
        break