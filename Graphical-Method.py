# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 16:49:59 2019

@author: ensar
"""

import numpy as np
import matplotlib.pyplot as plt
import math

B = 120 #cm
E = 75e5 #N/cm2
s_all = 15000 #N/cm2
W = 60000 #N
density = 2.8e-3 #kg/cm3

n = 100
D=np.array(range(n))/10
H=np.array(range(n))*2
y2=np.zeros(n)
g1=np.zeros(n)
g3=np.zeros(n)
g4=np.zeros(n)
g5=np.zeros(n)
g6=np.zeros(n)
Df=np.zeros(n)
Lagrange=np.zeros(n)
g2=[1e10]*n

for i in range(n):
    A = D[i]**2*math.pi/4
    l = (H[i]**2+B**2/3)**0.5
    I = math.pi/64*D[i]**4
    P = W*l/3/H[i]
    Pcr = math.pi**2*E*I/l**2
    
    g3[i] = 200
    g4[i] = 50
    g5[i] = 10
    g6[i] = 0.5
    
    g1[i] = (4*P/s_all/math.pi)**0.5
    
    f = 7.05 #kg
    Df[i] = (f*4/math.pi/3/l/density)**0.5
    for i2 in range(n):
        l = (H[i2]**2+B**2/3)**0.5
        I = math.pi/64*D[i]**4
        P = W*l/3/H[i2]
        Pcr = math.pi**2*E*I/l**2
        g2_temp = abs(P-Pcr/2)
        if g2[i] > g2_temp and P-Pcr/2 < 0:
            g2[i] = g2_temp
            y2[i] = H[i2]

plt.plot(g1,H)
plt.plot(D,y2)
plt.plot(D,g3)
plt.plot(D,g4)
plt.plot(g5,H)
plt.plot(g6,H)
plt.plot(Df,H)
plt.xlabel('D')
plt.ylabel('H')
plt.title('Graphical Optimization')
plt.legend(('g1','g2','g3','g4','g5','g6','f='+str(f)),loc='upper right')
plt.savefig('Q1.png',dpi=720)

Result =[]
for d in range(n):
    for h in range(n):
        if H[h] > y2[d] and y2[d]!= 0 and D[d] < Df[h] and H[h] > 50:
            Result.append([D[d],H[h]])
