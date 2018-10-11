#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 11 oct 2018 10:00

@author: meng
"""


import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits
#Filament function
def coldsty(r,Ap,rho,Rflat,p):
    return Ap*(rho*Rflat)*1./np.power(1.+(r/Rflat)*(r/Rflat),(p-1.)/2.)
#create a typical filament
#r range

r=np.arange(-50,51,2)
Ap=np.pi/2.
rho=2.
Rflat=10.
p=2.
tFLMT=np.zeros((51,51))
for i in range(51):
 tFLMT[i,:]=coldsty(r,Ap,rho,Rflat,p)
plt.plot(r,tFLMT[0,:])
plt.show()
#write to fits
hdu=fits.PrimaryHDU(tFLMT)
hdul=fits.HDUList([hdu])
hdul.writeto('tFLMT.fits')
