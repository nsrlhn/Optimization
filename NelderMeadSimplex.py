# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 15:19:55 2019

@author: ensar
"""

def NMS(function,initialPoints,epsilon,r,c,e,s):
    dimension = len(initialPoints[0])
    if dimension != len(initialPoints)-1:
        return None
    points = initialPoints
    while True:
        #Step1
        f = []
        for x in points:
            f.append(function(x))
        #Step2
        f_sorted = f[:]
        f_sorted.sort()
        fl = f_sorted[0]
        fs = f_sorted[-2]
        fh = f_sorted[-1]
        index_l = f.index(fl)
        index_s = f.index(fs)
        index_h = f.index(fh)
        xl=points[index_l]
        xs=points[index_s]
        xh=points[index_h]
        #Step3
        n = len(points)-1
        x0 = []
        for i in range(dimension):
            total = 0
            for x in points:
                total += x[i]
            total = (total-xh[i])/n
            x0.append(total)
        #Step4
        xr = []
        for i in range(dimension):
            xr.append(x0[i]+r*(x0[i]-xh[i]))
        #Step5
        fr = function(xr)
        if fr < fl:
            xe = []
            for i in range(dimension):
                xe.append(xr[i]+e*(xr[i]-x0[i]))
            fe = function(xe)
            if fe < fr:
                xh = xe[:]
            else:
                xh = xr[:]
        elif fr > fh:
            xc = []
            for i in range(dimension):
                xc.append(x0[i]-c*(x0[i]-xh[i]))
            fc = function(xc)
            #Step6
            if fc < fh:
                xh = xc[:]
            else:
                for i in range(dimension):
                    xh[i] = xl[i] + s*(xh[i]-xl[i])
                    xs[i] = xl[i] + s*(xs[i]-xl[i])
        elif fs < fr and fr < fh:
            xc = []
            for i in range(dimension):
                xc.append(xr[i]-c*(xr[i]-x0[i]))
            fc = function(xc)
            #Step6
            if fc < fh:
                xh = xc[:]
            else:
                for x in points:
                    for i in range(dimension):
                        x[i] = xl[i] + s*(x[i]-xl[i])
        elif fl < fr and fr < fs:
            xh = xr[:]
        #Step7
        points[index_l] = xl
        points[index_s] = xs
        points[index_h] = xh
        f0 = function(x0)
        if (((fh-f0)**2+(fs-f0)**2+(fl-f0)**2)/(dimension+1))**0.5 < epsilon:
            return x0
