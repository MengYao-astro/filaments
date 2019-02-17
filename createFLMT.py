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
from scipy import integrate

#read FLMTS table of IC5146
csvdata=np.genfromtxt('FLMTStable.csv',delimiter=';')
sample=csvdata[11:28,:]
number=sample[:,0]
NH2c=sample[:,1]*10.**21.      # unit: cm-2
p=sample[:,2]
Rflatpc=sample[:,3]   # unit: pc
#count samples
amount=len(number)
#convert Rflat in cm unit
Rflat=Rflatpc*3.0856775814914*10.**18.      # unit: cm
#define Ap coefficienct function
def intApco(indexp):
    f = lambda x : 1/((x**2+1)**(indexp/2.))
    Apco=integrate.quad(f,-float('inf'),float('inf'))[0]
    return Apco
#Filament column density function
def coldsty(vr,vAp,vrhoc,vRflat,vp):                #unit: cm-2
    return vAp*(vrhoc*vRflat)/np.power(1.+(vr/vRflat)**2.,(vp-1.)/2.) # r* means pc-cm
#define pixel size and calculate the physical size of the filaments
#1'' per pixel and take 1024 pixels
datapoints=1024
#set distance to 500pc
physicalLpc=1024/206265.*500. # unit : pc
physicalLcm=physicalLpc*3.0856775814914*10.**18. # unit : cm
#r range
r=np.linspace(-physicalLcm,physicalLcm,datapoints)   # unit: cm
#calculate Ap
Ap=np.array([intApco(x) for x in p])
#calculate rho-center(r=0)
rhoc=2.33*(1.6737236*10.**-24.)*NH2c/Ap/Rflat     # unit: cm-3
#create filament in different distance
#zeros array
NH2=np.zeros((amount,datapoints))
for i in range(amount):
 NH2[i,:]=coldsty(r,Ap[i],rhoc[i],Rflat[i],p[i])/(2.33*1.6737236*10.**-24.)
 plt.plot(r,NH2[i,:])
 #write to fits file
 '''
 hdu=fits.PrimaryHDU(NH2[i,:])
 hdul=fits.HDUList([hdu])
 if not os.path.exists('Cdensityatdiffd/No%d' %number[i]):
  os.mkdir('Cdensityatdiffd/No%d' %number[i])
 hdul.writeto('Cdensityatdiffd/No%d/No%dcoldensityat%dpc.fits' %(number[i],number[i],distance))
 '''
plt.title('column density (cm^-2)')
plt.show()

#Flux of the filaments
def flux(vNH2coldsty,vTem,vwavelen,vopacity,vthetaH):
    return vNH2coldsty/(2.02*10.**20)/(np.exp(1.439/vwavelen/(vTem/10.))-1)/vwavelen**3*(vopacity/0.01)*(vthetaH/10.)**2
    #NH2 in cm-2, Tem in K, wavenlen in mm, opacity in cm2/g, thetaH in arcsec
    #get flux in mJy/beam
#set parameters
Tem=10.        # in K
wavelen=1.     # in mm
opacity=0.01     # in cm2/g
thetaH=16.      # in arcsec
Fflux=flux(NH2,Tem,wavelen,opacity,thetaH)
Fflux=Fflux/1000.                                  # convert unit from mJy to Jy
plt.plot(r,Fflux[0,:])
plt.title('flux density (mJy/beam)')
plt.show()

'''
hdu=fits.PrimaryHDU(Fflux[0,:,:])
hdul=fits.HDUList([hdu])
hdul.writeto('no1flux.fits')
'''
