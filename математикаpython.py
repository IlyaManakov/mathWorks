import numpy as np
import statistics
from math import *
from prettytable import PrettyTable



def NewObject():
    th = ["K",'A',"Pab(K)","H(a,b)","Максимизация","H'(a,b)"]
    table = PrettyTable(th)
    print("Введите ансамбль большого числа L идентичных электротехнических систем")
    L = list(map(float,input().split()))
    pAB = L/ np.sum(L)
    print(pAB)
    hAB = -np.sum(pAB* np.log10(pAB))
    mAB = statistics.mean(L)

    for i in range(len(L)):
        max = -(hAB)+np.sum(pAB[i])+np.sum(pAB[i] + L[i])
        Hab2 = abs(-np.sum(L[i] - max) * abs(np.log2(L[i] - max)))+(-np.sum(L[i] +max) * abs(np.log2(L[i] + max)))
        table.add_row([i+1, L[i],(round(L[i]/np.sum(L),3)),(round(-np.sum(pAB[i] * np.log10(pAB)),3)),round(max),Hab2])
    print(table)

    th1 = ['M(Aab)']
    table1 = PrettyTable(th1)
    table1.add_row([mAB])
    print(table1)
NewObject()


#Функция Лагранжа
def LagAab(A,w):
    sum = 0
    for i in range(w):
        sum += 1*A[i]
    return sum
print("введите W")
w = int(input())
print('Введите ',w,' значение')
A = list(map(float,input().split()))
Q = 0
for i in range(w):
    Q += exp(-1*LagAab(A,w))
H = 0
H = np.log10(Q) + LagAab(A,w)
print('H=',H)
print('Q=',Q)
p = []
for i in range(w):
    p.append(1/Q*exp(A[i]))
    print('p[',i+1,']=',p[i])
M = 0
for i in range(w):
    M= M + (p[i]*A[i])
print('M=',M)
