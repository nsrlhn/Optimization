# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 21:05:05 2019

@author: ensar
"""
Point = 3,4

f = {}
number = 0
def function(variables):
    v = tuple(variables)
    global f
    if v in f:
        return f[v]
    else:
        x = v[0]
        y = v[1]
        func = x**3/3 - 4*x + y**3/3 - 9*y
        f[v] = func
        global number
        number += 1
        return func

def Gradient_Forward(point,i):
    Delta = point[i]*0.001
    Point_Plus_Delta = list(point[:])
    Point_Plus_Delta[i] += Delta
    return (function(Point_Plus_Delta)-function(point))/Delta

G = []
for i in range(len(Point)):
    G.append(Gradient_Forward(Point,i))
    
def Hession_Forward(point,i,j):
    Delta = point[j]*0.001
    Point_j = list(point[:])
    Point_j[j] += Delta
    return (Gradient_Forward(Point_j,i)-Gradient_Forward(point,i))/Delta

H = []
for i in range(len(Point)):
    H.append([])
    for j in range(len(Point)):
        H[i].append(Hession_Forward(Point,i,j))