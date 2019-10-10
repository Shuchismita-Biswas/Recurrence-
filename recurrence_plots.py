# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 15:07:35 2019

@author: shuch
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#unthresholded recurrence plot
def r_plot(data,delay=1):
    transformed=np.zeros([2,len(data)-delay])
    transformed[0,:]=data[0:len(data)-delay]
    transformed[1,:]=data[delay:len(data)]
    rp=np.zeros([len(data)-delay,len(data)-delay])
    for i in range(len(rp)):
        for j in range(len(rp)):
            rp[i,j]=np.linalg.norm(transformed[:,i]-transformed[:,j])
    return(rp)
    
def cr_plot(data1,data2,delay=1):
     transformed=np.zeros([2,len(data1)-delay])
     transformed[0,:]=data1[0:len(data1)-delay]
     transformed[1,:]=data2[delay:len(data2)]
     crp=np.zeros([len(data1)-delay,len(data2)-delay])
     for i in range(len(crp)):
        for j in range(len(crp)):
            crp[i,j]=np.linalg.norm(transformed[:,i]-transformed[:,j])
     return(crp)

def threshold(mat,thresh=0.2):
    mini=mat.min()
    maxi=mat.max()
    trans=(mat-mini)/(maxi-mini)
    for i in range(len(trans)):
        for j in range(len(trans)):
            if trans[i,j]>0.2:
                trans[i,j]=1
            else:
                trans[i,j]=0
    return(trans)