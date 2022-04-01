import numpy as np
import statistics
from math import *
from prettytable import PrettyTable

def LagAab(L,w):
    sum = 0
    for i in range(w):
        for j in range(len(L[i])):
            sum += 1*L[i][j]
    return sum

def Lsum(w):
    sumL = 0
    for i in range(w):
        sumL += sum(L[i])
    return sumL
th = ["K",'A',"Pab(K)","H(a,b)"]
table = PrettyTable(th)       
print("введите W")
w = int(input())
print(w,' систем(a/ы)')
L = []
for i in range(w):
    print('Введите ',i+1,' систему')
    L.append( list(map(float,input().split())))

Q,M = 0,0
p,pAB,hAB,mAB = [],[],[],[]
for i in range(w):
    pAB.append(sum(L[i])/Lsum(w))
    hAB.append(-np.sum(pAB[i]*np.log10(pAB[i])))
    for j in range(len(L[i])):
        Q += exp(-1*LagAab(L,w))
for i in range(w):
    p.append([])
    for j in range(len(L[i])):
        p[i].append(1/Q*exp(L[i][j]))
        M = M + (p[i][j]*L[i][j])

for i in range(w):
    table.add_row([i,L[i],pAB[i],hAB[i]])
#MAab = np.log10(Q) +
print('Q=',Q)
print(table)
print('M(a,b)=',M)
