#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 15:31:04 2018

@author: meng
"""

import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits
'''
#gaussian function
def gaussian(x,mu,sig):
    return (1./(np.sqrt(2.*np.pi)*sig))*np.exp(-(x-mu)*(x-mu)/2.*(sig*sig))
mu=0
sig=2
plt.plot(gaussian(np.linspace(-3,3,120),mu,sig))
plt.show()
'''

#Filament function
def coldsty(r,Ap,rho,Rflat,p):
    return Ap*(rho*Rflat)*1./np.power(1.+(r/Rflat)*(r/Rflat),(p-1.)/2.)
#create a filament
#fits data
#r range
r=np.arange(-50,51,1)
#diff Ap
ApFLMTs=np.zeros((3,101,101))
for Ap in np.pi/4., np.pi/2., np.pi:
 for i in range(101):
  rho=1.
  Rflat=10.
  p=4.
  j=int(np.log2(Ap*4./np.pi))    #count from 0
  ApFLMTs[j,i,:]=coldsty(r,Ap,rho,Rflat,p)   #write column density to 3 arrays
 plt.subplot(2,2,1)
 plt.plot(r,ApFLMTs[j,0,:])    #plot with r and each column desity
 plt.title('diff Ap')
 plt.legend(['pi/4','pi/2','pi'],loc='best')
 '''
 #write to fits
 hdu=fits.PrimaryHDU(ApFLMTs[j,:,:])
 hdul=fits.HDUList([hdu])
 hdul.writeto('diffAp2D%d.fits' %j)
 '''
#diff rho
rhoFLMTs=np.zeros((3,101,101))
for rho in 1.,2.,3.:
 for i in range(101):
  Ap=np.pi/2.
  Rflat=10.
  p=2.
  j=int(rho-1)     #count from 0
  rhoFLMTs[j,i,:]=coldsty(r,Ap,rho,Rflat,p)   #write column density to 3 arrays
 plt.subplot(2,2,2)
 plt.plot(r,rhoFLMTs[j,0,:])    #plot with r and each column desity
 plt.title('diff rho')
 plt.legend(['1','2','3'],loc='best')
 '''
 #write to fits
 hdu=fits.PrimaryHDU(rhoFLMTs[j,:,:])
 hdul=fits.HDUList([hdu])
 hdul.writeto('diffrho2D%d.fits' %j)
 '''
#diff Rflat
RflatFLMTs=np.zeros((3,101,101))
for Rflat in 10.,20.,30.:
 for i in range(101):
  Ap=np.pi/2.
  rho=1.
  p=2.
  j=int(Rflat/10.-1)    #count from 0
  RflatFLMTs[j,i,:]=coldsty(r,Ap,rho,Rflat,p)   #write column density to 3 arrays
 plt.subplot(2,2,3)
 plt.plot(r,RflatFLMTs[j,0,:])    #plot with r and each column desity
 plt.title('diff Rflat')
 plt.legend(['10','20','30'],loc='best')
 '''
 #write to fits
 hdu=fits.PrimaryHDU(RflatFLMTs[j,:,:])
 hdul=fits.HDUList([hdu])
 hdul.writeto('diffRflat2D%d.fits' %j)
 '''
#diff p
pFLMTs=np.zeros((3,101,101))
for p in np.arange(2,5,1):
 for i in range(101):
  Ap=np.pi/2.
  rho=1.
  Rflat=10.
  j=int(p-2.)     #count from 0
  pFLMTs[j,i,:]=coldsty(r,Ap,rho,Rflat,p)     #write column density to 3 arrays
 plt.subplot(2,2,4)    
 plt.plot(r,pFLMTs[j,0,:])     #plot with r and each column desity
 plt.title('diff p')
 plt.legend(['2','3','4'],loc='best')
 '''
 #write to fits
 hdu=fits.PrimaryHDU(pFLMTs[j,:,:])
 hdul=fits.HDUList([hdu])
 hdul.writeto('diffp2D%d.fits' %j)
 '''
plt.subplots_adjust(wspace =0.5, hspace =0.5)
plt.savefig('ColumnDensity')
plt.show()
