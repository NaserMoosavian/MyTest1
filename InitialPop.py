# -*- coding: utf-8 -*-
"""
Created on Tue May 18 12:02:49 2021

@author: Naser
"""
import numpy
from Initialization import  Initialization
from BestSol import  BestSol
from ObjectiveFunc import ObjectiveFunc


class InitialPop:
    BestSol.Cost=10e10
    nPop = Initialization().nPop
    NumVariable = Initialization().NumVariable
    Varmin = Initialization().Varmin
    Varmax = Initialization().Varmax 
    a = Initialization().a
    f = Initialization().f
    trial = Initialization().trial
    Costfunction = ObjectiveFunc.Costfunction
    nEval=0
    # Create inital population
    for i in range (0,nPop): 
        a[i,:] = numpy.random.uniform(Varmin,Varmax,NumVariable)
        f[i]=Costfunction(a[i,:])
        trial[i]=0
        nEval=nEval+1
        if f[i]<BestSol.Cost:
            BestSol.Position=a[i,:]
            BestSol.Cost=f[i]
            BestSol.Trial=trial[i]
    nPop1=nPop
    