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
pixelsize=1.   # unit : arcsec
#set distance to 500pc
physicalLpc=datapoints*pixelsize/206265.*500. # unit : pc
physicalLcm=physicalLpc*3.0856775814914*10.**18. # unit : cm
#r range
r=np.linspace(-physicalLcm,physicalLcm,datapoints)   # unit: cm
#calculate Ap
Ap=np.array([intApco(x) for x in p])
#calculate rho-center(r=0)
rhoc=2.8*(1.6737236*10.**-24.)*NH2c/Ap/Rflat     # unit: cm-3
#create filament in different distance
#zeros array
NH2=np.zeros((amount,datapoints))
for i in range(amount):
 NH2[i,:]=coldsty(r,Ap[i],rhoc[i],Rflat[i],p[i])/(2.8*1.6737236*10.**-24.)
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

#Flux per beam of the filaments
def fluxperbeam(vNH2,vT,vlambda,vkv,vthetaHPBW):
    return 4.396*10**-24*vNH2/(np.exp(1.439/vlambda/(vT/10.))-1)*vlambda**-3*vkv*vthetaHPBW**2
    #NH2 in cm-2, Tem in K, wavenlen-lambda in mm, opacity-kv in cm2/g, thetaHPBW in arcsec
    #get flux in Jy/beam
#Flux per pixel
def fluxperpixel(vNH2,vT,vlambda,vkv,vthetap):
    return 4.377*10**-24*vNH2/(np.exp(1.439*vlambda**-1*(vT/10.)**-1)-1)*vlambda**-3*vkv*vthetap**2
    #NH2 in cm-2, Tem in K, wavelength-lambda in mm, opacity-kv in cm2/g, theta in arcsec
    #get flux in Jy/beam
#set parameters
Tem=10.        # in K
wavelen=0.85     # in mm
opacity=0.01     # in cm2/g
fluxp=fluxperpixel(NH2,Tem,wavelen,opacity,pixelsize)
fluxb=fluxperbeam(NH2,Tem,wavelen,opacity,16.795)
plt.plot(r,fluxp[0,:])
no1flux=np.array([fluxp[0,:]]*datapoints)

plt.title('flux density (Jy/pixel)')
plt.show()


hdu=fits.PrimaryHDU(no1flux)
hdul=fits.HDUList([hdu])
hdul.writeto('no1flux.fits')

