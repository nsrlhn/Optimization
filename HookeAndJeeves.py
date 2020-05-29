# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 13:10:01 2019

@author: ensar
"""
def exploratoryMove(function,xc,stepSize):
    xc = list(xc)
    s = stepSize
    for i in range(len(xc)):
        xc_minus = xc[:]
        xc_minus[i] -= s[i]
        xc_plus = xc[:]
        xc_plus[i] += s[i]
        if function(xc_minus) <= function(xc):
            xc = xc_minus[:]
        elif function(xc_plus) <= function(xc):
            xc = xc_plus[:]
    return xc[:]

def patternMove(function,xc,xe):
    xc = list(xc)
    xe = list(xe)
    result = []
    for i in range(len(xc)):
        result.append(2*xe[i]-xc[i])
    return result    
    
def HJ(function,initialPoint,stepSize,epsilon):
    f = function
    xc = initialPoint
    s = stepSize
    e = epsilon
    while True:
        #Step2
        xe = exploratoryMove(f,xc,s)
        #Step3
        if xe != xc and f(xe) < f(xc):
            #Step5
            while True:
                xp = patternMove(f,xc,xe)
                #Step6
                xp_prime = exploratoryMove(f,xp,s)
                #Step7
                if f(xp_prime) < f(xe):
                    xc = xe[:]
                    xe = xp_prime[:]
                else:
                    xc = xe[:]
                    break
        #Step4
        if max(s) < e:
            break
        else:
            s = [x / 2 for x in s]
    return xc
    