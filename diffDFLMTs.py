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
NH2=sample[:,1]*10**21      # unit: cm-2
p=sample[:,2]
Rflatpc=sample[:,3]   # unit: pc
#prepare parameters
Ap=np.pi/2.
Rflat=Rflatpc*3.09*10**18      # unit: cm
rho=NH2/Ap/Rflat     # unit: cm-3
p=p
#count
amount=len(number)
#Filament column density function
def coldsty(r,Ap,rho,Rflat,p):                #in cm-2
    return Ap*(rho*Rflat)*1./np.power(1.+(r*3.09*10.**18/Rflat)**2.,(p-1.)/2.) # r* means pc-cm
#create filament in different distance
distance=float(input('distance in pc:'))
initialD=460.
#r range
times=distance/initialD
r=np.linspace(-1.5,1.5,1345)*times   # unit: pc
#zeros array
diffdcoldsty=np.zeros((amount,1345,1345))
for i in range(amount):
 for j in range(1345):
  diffdcoldsty[i,j,:]=coldsty(r,Ap,rho[i],Rflat[i],p[i])
 plt.plot(r,diffdcoldsty[i,0,:])
 #write to fits file
 '''
 hdu=fits.PrimaryHDU(diffdcoldsty[i,:,:])
 hdul=fits.HDUList([hdu])
 if not os.path.exists('Cdensityatdiffd/No%d' %number[i]):
  os.mkdir('Cdensityatdiffd/No%d' %number[i])
 hdul.writeto('Cdensityatdiffd/No%d/No%dcoldensityat%dpc.fits' %(number[i],number[i],distance))
 '''
plt.show()

#Flux of the filaments
def flux(NH2coldsty,Tem,wavelen,opacity,thetaH):
<<<<<<< HEAD
    return NH2coldsty/(2.2*10.**20)/(np.exp(1.439*(wavelen*Tem/10.)**(-1)-1))/wavelen**3/(opacity/0.01)/(thetaH/10.)
=======
    return NH2coldsty/(2.2*10.**20)/(np.exp(1.439*wavelen*Tem)-1)/wavelen/(opacity/0.01)/(thetaH/10.)
>>>>>>> f243978e2c6bd73074ad9eb7c9cb3f5dd5674c9b
    #NH2 in cm-2, Tem in K, wavenlen in mm, opacity in cm2/g, thetaH in arcsec
    #get flux in mJy/beam
NH2coldsty=diffdcoldsty
<<<<<<< HEAD
Tem=10.        # in K
wavelen=1.     # in mm
opacity=1.     # in cm2/g
thetaH=3.      # in arcsec
Fflux=flux(NH2coldsty,Tem,wavelen,opacity,thetaH)
plt.plot(r,Fflux[0,0,:])
plt.show()

=======
Tem=10.
wavelen=1.
opacity=1.
thetaH=3.
Fflux=flux(NH2coldsty,Tem,wavelen,opacity,thetaH)
>>>>>>> f243978e2c6bd73074ad9eb7c9cb3f5dd5674c9b
'''
hdu=fits.PrimaryHDU(Fflux[0,:,:])
hdul=fits.HDUList([hdu])
hdul.writeto('no1Fflux.fits')
'''
<<<<<<< HEAD

=======
>>>>>>> f243978e2c6bd73074ad9eb7c9cb3f5dd5674c9b
