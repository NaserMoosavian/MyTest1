# -*- coding: utf-8 -*-
"""
Created on Tue May 18 12:04:19 2021

@author: Naser
"""
import numpy


class Initialization:
    def __init__(self):
        self.Maxit=1000
        self.nPop=100
        self.NumVariable=2
        self.Varmin=-100*numpy.ones(self.NumVariable)
        self.Varmax=100*numpy.ones(self.NumVariable)
        self.Beta = 0.5 # Mutation rate
        self.Pcr = 0.5 # Crossover rate
        self.FCost=10e10 # A large number
        self.a=numpy.zeros((self.nPop,self.NumVariable)) # Population position
        self.f=numpy.zeros(self.nPop) # Objective function value
        self.trial=numpy.zeros(self.nPop) # Counter
        self.inum=numpy.zeros(self.nPop)    