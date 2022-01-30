#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 22:04:26 2022

@author: yassine
"""
from PIL import Image
import numpy as np
import numpy.linalg as alg
import matplotlib.pyplot as plt
def compression(M, k):
    U,S,VT = alg.svd(M,full_matrices=False)
    S = np.diag(S)
    Xapprox = U[:,:k] @ S[0:k,:k] @ VT[:k,:]
    plt.figure(1)
    img = plt.imshow(Xapprox)
    img.set_cmap('gray')
    plt.axis('off')
    plt.title('k = ' + str(k))
    plt.show()
    plt.figure(2)
    plt.semilogy(np.diag(S))
    plt.title('Singular Values')
    plt.show()
    
    plt.figure(3)
    plt.plot(np.cumsum(np.diag(S))/np.sum(np.diag(S)))
    plt.title('Singular Values: Cumulative Sum')
    plt.show()
        
im=Image.open("lena_gris.png")
T=np.array(im)
h,l=T.shape 
compression(T,30)
for r in (10,20,30,40,50,60):
    compression(T, r)