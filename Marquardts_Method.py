# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 00:04:23 2019

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

def IsPositiveDefinite(Hession_Matrix):
    for i in range(len(Hession_Matrix)):
        if np.linalg.det(Hession_Matrix) < 0:
            return False
        Hession_Matrix = np.delete(Hession_Matrix,0,0)
        Hession_Matrix = np.delete(Hession_Matrix,0,1)
    return True

def get_min_point(function,start_point,max_iteration,epsilon):
    point = np.array(start_point)
    lamda = 1e3
    for k in range(max_iteration):
        G = np.array(Gradient(function,point))
        if np.linalg.norm(G) < epsilon:
            break
        H = np.array(Hession(function,point))
        s = -np.matmul(np.linalg.inv(H+lamda*np.identity(len(H))),G)
        p = point + s
        if function(p) < function(point):
            lamda = lamda/2
        else:
            lamda = lamda*2
        point = p
    return point