# -*- coding: utf-8 -*-
"""
Created on Tue May 18 12:00:21 2021

@author: Naser
"""
import numpy
import matplotlib.pyplot as plt
from InitialPop import InitialPop
from Initialization import Initialization
from BestSol import  BestSol
from ObjectiveFunc import ObjectiveFunc

class FDE(BestSol):
        # Start FDE
        trial = InitialPop().trial
        inum = Initialization().inum
        nPop = Initialization().nPop
        nPop1 = InitialPop().nPop1
        Beta = Initialization().Beta
        FCost = Initialization().FCost
        Costfunction = ObjectiveFunc.Costfunction
        a = InitialPop().a
        f = InitialPop().f
        nEval = InitialPop().nEval
        
        
        for it in range (0,Initialization().Maxit): 
            k=0
            for i in range (0,nPop): 
                if trial[i] > 30:           
                    inum[k]=i
                    k=k+1 
            if k>0 and nPop>0.1*nPop1:
                for ii in range (0,k-1):
                    tt=int(inum[ii])
                    a= numpy.delete(a, (tt), axis=0)
                    f=numpy.delete(f, (tt), axis=0)
                    trial=numpy.delete(trial, (tt), axis=0)
                    nPop=nPop-1
                    if nPop<=0.1*nPop1:
                        break
            inum=numpy.zeros(nPop)
            if nPop<=int(0.1*nPop1): # Restart
                nPop1=int(1.1*nPop1)
                nPop=nPop1
                a=numpy.zeros((nPop,Initialization().NumVariable))
                f=numpy.zeros(nPop)
                trial=numpy.zeros(nPop)  
                BestSol.Cost=10e10
                for i in range (0,nPop1):
                    a[i,:] = numpy.random.uniform(Initialization().Varmin,Initialization().Varmax,Initialization().NumVariable)
                    f[i]=Costfunction(a[i,:])
                    trial[i]=0
                    nEval=nEval+1
                    if f[i]<BestSol.Cost:
                        BestSol.Position=a[i,:]
                        BestSol.Cost=f[i]
                        BestSol.Trial=trial[i]
            for i in range (0,nPop): # Mutation and Crossover 
                A = numpy.random.permutation(range(nPop))
                A=numpy.delete(A, (i), axis=0)
                A1=A[1]
                A2=A[2]
                A3=A[3]
                x=a[A1,:] 
                TTT=sum(abs(BestSol.Position-a[A1,:]))>0 and sum(abs(BestSol.Position-a[A2,:]))>0 and sum(abs(BestSol.Position-a[A3,:]))>0
                if TTT == True:
                    Y=a[A1,:]+Beta*(BestSol.Position-a[A2,:])
                    Y=numpy.minimum(Y,Initialization().Varmax)
                    Y=numpy.maximum(Y,Initialization().Varmin)
                    Z=numpy.zeros(Initialization().NumVariable)
                    for j in range (0,Initialization().NumVariable):
                        t=numpy.random.uniform(0,1,[1])
                        if t<=Initialization().Pcr:
                            Z[j]=Y[j]
                        else:
                            Z[j]=x[j]
                    NewSol=Z
                    NewCost=Costfunction(NewSol)
                    nEval=nEval+1
                    if NewCost<f[i]: # Selection
                        a[i,:]=NewSol
                        f[i]=NewCost
                        trial[i]=0
                        if f[i]<BestSol.Cost:
                            BestSol.Position=a[i,:]
                            BestSol.Cost=f[i]
                            BestSol.Trial=trial[i]
                        else:
                            BestSol.Trial=BestSol.Trial+1
                    else:
                        trial[i]=trial[i]+1
                    if BestSol.Cost<FCost:
                        FCost=BestSol.Cost
            print('iteration',it,'Cost Function',FCost,)
            #Create the plots
            fig = plt.figure(figsize=(8,8))  
            ax = plt.subplot(111)
            nn=ax.scatter(8,8, s=0.1, alpha=1)
            mm=ax.scatter(0,0, s=150, alpha=1)
            colors = numpy.random.rand(len(a[:,0]))
            area = (3 * numpy.random.rand(len(a[:,0])))**2  # 0 to 15 point radii
            bb=ax.scatter(a[:,0],a[:,1], s=area, c=colors, alpha=0.5)
            plt.pause(0.35)
            plt.show()


