#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 11 oct 2018 10:00

@author: meng
"""

import os
import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits
#read FLMTS table of IC5146
csvdata=np.genfromtxt('FLMTStable.csv',delimiter=';')
sample=csvdata[11:28,:]
number=sample[:,0]
rho=sample[:,1]
p=sample[:,2]
Rflat=sample[:,3]
#count
amount=len(number)

#Filament function
def coldsty(r,Ap,rho,Rflat,p):
    return Ap*(rho*Rflat)*1./np.power(1.+(r/Rflat)*(r/Rflat),(p-1.)/2.)
#create filament in different distance
distance=float(input('distance in pc:'))
initialD=460.
#r range
times=distance/initialD
r=np.linspace(-1.5,1.5,1345)*times
Ap=np.pi/2.
diffdF=np.zeros((amount,1345,1345))
for i in range(amount):
 for j in range(1345):
  diffdF[i,j,:]=coldsty(r,Ap,rho[i],Rflat[i],p[i])
 plt.plot(r,diffdF[i,0,:])
 #write to fits file

 hdu=fits.PrimaryHDU(diffdF[i,:,:])
 hdul=fits.HDUList([hdu])
 if not os.path.exists('FLMTSatdiffd/No%d' %number[i]):
  os.mkdir('FLMTSatdiffd/No%d' %number[i])
 hdul.writeto('FLMTSatdiffd/No%d/No%dFLMTat%dpc.fits' %(number[i],number[i],distance))

plt.show()
