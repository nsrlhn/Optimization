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

def getalfa(point,s,function):
    f = function
    a = 0
    b = 1
    l = 1
    while(l > 1e-5):
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

def get_min_point(function,start_point,max_iteration,epsilon):
    point = np.array(start_point)
    for k in range(max_iteration):
        s = -np.array(Gradient(function,point))*1000
        if np.linalg.norm(s) < epsilon:
            break
        alfa = getalfa(point,s,function)
        p = point + alfa*s
        if np.linalg.norm(p-point)/np.linalg.norm(point) <= epsilon:
            break
        point = p
    return point
        
        
