# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 08:55:03 2019

@author: ensar
"""
import numpy as np

def Gradient(function,point):
    def Gradient_Central(point,i):
        Delta = point[i]*0.001
        Point_Plus_Delta = list(point[:])
        Point_Plus_Delta[i] += Delta/2
        Point_Minus_Delta = list(point[:])
        Point_Minus_Delta[i] -= Delta/2
        return (function(Point_Plus_Delta)-function(Point_Minus_Delta))/Delta
    G = []
    for i in range(len(point)):
        G.append(Gradient_Central(point,i))
    return G

def Hession(function,point):
    def Gradient_Central(point,i):
        Delta = point[i]*0.001
        Point_Plus_Delta = list(point[:])
        Point_Plus_Delta[i] += Delta/2
        Point_Minus_Delta = list(point[:])
        Point_Minus_Delta[i] -= Delta/2
        return (function(Point_Plus_Delta)-function(Point_Minus_Delta))/Delta
        
    def Hession_Central(point,i,j):
        Delta = point[j]*0.001
        Point_pj = list(point[:])
        Point_pj[j] += Delta/2
        Point_nj = list(point[:])
        Point_nj[j] -= Delta/2
        return (Gradient_Central(Point_pj,i)-Gradient_Central(Point_nj,i))/Delta
    
    H = []
    for i in range(len(point)):
        H.append([])
        for j in range(len(point)):
            H[i].append(Hession_Central(point,i,j))
    return H
        
def getalfa(point,s,function):
    f = function
    a = 0
    b = 1
    l = 1
    while( l > 1e-5):
        l = b-a
        p1 = point + s*l/4+s*a
        pm = point + s*l/2+s*a
        p2 = point + s*l*3/4+s*a
        if f(p1) < f(pm):
            b = (l)/2+a
        else:
            a = (l)/4+a
            if f(pm) < f(p2):
                b = (l)*3/4+a
            else:
                a = (l)/2+a
        #print("alfa : "+str(a)+','+str(b))
    return (b-a)/2

def IsPositiveDefinite(Hession_Matrix):
    for i in range(len(Hession_Matrix)):
        if np.linalg.det(Hession_Matrix) < 0:
            return False
        Hession_Matrix = np.delete(Hession_Matrix,0,0)
        Hession_Matrix = np.delete(Hession_Matrix,0,1)
    return True

def get_min_point(function,start_point,max_iteration,epsilon):
    point = np.array(start_point)
    for k in range(max_iteration):
        G = np.array(Gradient(function,point))
        H = np.array(Hession(function,point))
        if IsPositiveDefinite(H):
            s = -np.array(Gradient(function,point))
        elif np.matmul(np.matmul(np.transpose(G),np.linalg.inv(H)),G) >= 0:
            s = -np.array(Gradient(function,point))
        else:
            print("Netons Method : Change Initial Point")
            break
        if np.linalg.norm(s) < epsilon:
            break
        alfa = getalfa(point,s,function)
        p = point + alfa*s
        if np.linalg.norm(p-point)/np.linalg.norm(point) <= epsilon:
            break
        point = p
    return point
        
        
