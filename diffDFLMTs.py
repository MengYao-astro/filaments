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
#create filament in different distance
d=float(input('distance in pc:'))
#r range
times=d/460.
r=np.linspace(-3,3,101)*times
Ap=np.pi/2.
rho=1.8
Rflat=0.05
p=2.1
tFLMT=np.zeros((101,101))
for i in range(101):
 tFLMT[i,:]=coldsty(r,Ap,rho,Rflat,p)
plt.plot(r,tFLMT[0,:])
plt.show()
#write to fits

hdu=fits.PrimaryHDU(tFLMT)

hdul=fits.HDUList([hdu])
hdul.writeto('FLMTin%dpc.fits' %d)

