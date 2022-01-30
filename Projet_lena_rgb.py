#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 23:12:59 2022

@author: yassine
"""


import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import svd
from PIL import Image


def compress_image(img, k):
    
    r = img[:,:,0]  # Matrice pour r
    g = img[:,:,1]  # Matrice pour g
    b = img[:,:,2] # Matrice pour b

    ur,sr,vr = svd(r, full_matrices=False)
    ug,sg,vg = svd(g, full_matrices=False)
    ub,sb,vb = svd(b, full_matrices=False)
    
    rr = np.dot(ur[:,:k],np.dot(np.diag(sr[:k]), vr[:k,:]))
    rg = np.dot(ug[:,:k],np.dot(np.diag(sg[:k]), vg[:k,:]))
    rb = np.dot(ub[:,:k],np.dot(np.diag(sb[:k]), vb[:k,:]))
    
    rimg = np.zeros(img.shape)
    
    rimg[:,:,0] = rr
    rimg[:,:,1] = rg
    rimg[:,:,2] = rb
    
    for ind1, row in enumerate(rimg):
        for ind2, col in enumerate(row):
            for ind3, value in enumerate(col):
                if value < 0:
                    rimg[ind1,ind2,ind3] = abs(value)
                if value > 255:
                    rimg[ind1,ind2,ind3] = 255

    compressed_image = rimg.astype(np.uint8)
    
    plt.title('k = ' + str(k))
    plt.imshow(compressed_image)
    plt.axis('off')
    plt.show()
    
im=Image.open("lena.png")
T=np.array(im)
for r in (10,20,30,40,50,60):
    compress_image(T,r)