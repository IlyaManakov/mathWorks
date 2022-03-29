
from random import *
from math import *

#0
a = list(map(int, input().split()))
print(a)
a.append(a[0])
a.remove(a[0])
print(a)

def nearest_value(items, value):
    '''Поиск ближайшего значения до value
в списке items'''
    found = items[0] # найденное значение (первоначально первое)
    for item in items:
        if abs(item - value) < abs(found - value):
            found = item
    return found
#5
x = float(input("Число X: "))#вводим число X
mas = []
masVag2 = []
masVag = []
'''объявляем массивы:
mas - массив, который нужен для нахождения

'''

N = int(input("Число N: ")) #вводим число N
a = [round(random()*100,2) for i in range(N)]
a.sort()
print("массив: ", a)
if len(a)>1:
    for i in range(N):
        for j in range(N):
            if i != j:
                mas.append((a[i]+a[j])/2)
        masVag.append(nearest_value(mas,x))
        mas = []
        for j in range(N):
            if (a[i]+a[j])/2 == masVag[i]:
                masVag2.append([a[i],a[j]])
                break
    print("Наиболее близко к", x, "среднее чисел", masVag2[masVag.index(nearest_value(masVag,x))][0],"и",masVag2[masVag.index(nearest_value(masVag,x))][1])
    print("Оно равно",round(nearest_value(masVag,x),2),"отклонение равно",round(abs(nearest_value(masVag,x)-x),2))
else:
    print("ошибка")

    
    
            
        


#6


#4
N = int(input("кол-во чисел в массиве: ")) 
Z = round(random() *  10,2) 
a = [round(random() *  10,2) for i in range(N)]
print("Число Z: ",Z)
print("Массив:",a)
count = 0 
for i in range(len(a)): 
    if a[i] > Z: 
        a[i] = Z 
        count += 1
print("Массив: ",a)
print("Число замен: ",count)



#3
N = int(input())
mas = []
log = False
for i in range(N):
    a = int(input())
    mas.append(a)
    if i>0:
        if mas[i-1]<mas[i]:
            log = True
        else:
            log = False
if log == True:
    print(mas, " = возрастающая")
else:
    print(mas, " = Не возрастающая")
    
#7
N = int(input())
slovar2 = {}
log = False
for i in range(N):
    a = int(input())
    if a//10 not in slovar2.keys(): 
        slovar2[a//10] = 1
    else:
        slovar2[a//10] += 1
sorted(slovar2.keys())
for key in slovar2:
    if key == 0:
        print("количество лет от 0 до 10 :=", slovar2.get(key))
    else:
        print("количество лет от",key*10,'до',(key+1)*10,':=',slovar2.get(key))
print(slovar2)

#1
N = int(input())
K = int(input())
sum = 0
A = []
masNat = []
for i in range(N):
    A.append(randint(1,100))
    if A[i] % K ==0:
        masNat.append(A[i])
        sum += A[i]
print("Массив", A)
print("Массив кратных элементов: ", masNat)
print("Сумма кратных элементов: ", end = "")

for i in range(len(masNat)):
    if i == 0:

        print(masNat[i], end = " ")
    else:
        print("+",masNat[i], end = " ") 
print(" = ", sum)
