# -*- coding: utf-8 -*-
"""
Created on Tue May 18 12:09:21 2021

@author: Naser
"""
import numpy

class ObjectiveFunc:
    def Costfunction(x):
        a0= numpy.array(x)
        y0 = sum(a0*a0) # Sphere function
        return y0
