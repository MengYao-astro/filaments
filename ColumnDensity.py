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
'''
#plot profile with vary parameters
for Ap in np.pi/4, np.pi/2, np.pi:
 rho=1
 Rflat=10
 p=4
 plt.subplot(2,2,1)
 plt.plot(coldsty(np.linspace(-50,50,100),Ap,rho,Rflat,p))
 plt.title('dif Ap')
 plt.legend(['pi/4','pi/2','pi'],loc='best')
for rho in 1,2,3:
 Ap=np.pi/2
 Rflat=10
 p=4
 plt.subplot(2,2,2)
 plt.plot(coldsty(np.linspace(-50,50,100),Ap,rho,Rflat,p))
 plt.title('dif rho')
 plt.legend(['1','2','3'],loc='best')
for Rflat in 10,20,30:
 Ap=np.pi/2
 rho=1
 p=4
 plt.subplot(2,2,3)
 plt.plot(coldsty(np.linspace(-50,50,100),Ap,rho,Rflat,p))
 plt.title('dif Rflat')
 plt.legend(['10','20','30'],loc='best')
for p in 2,3,4:
 Ap=np.pi/2
 rho=1
 Rflat=10
 plt.subplot(2,2,4)
 plt.plot(coldsty(np.linspace(-50,50,100),Ap,rho,Rflat,p))
 plt.title('dif p')
 plt.legend(['2','3','4'],loc='best')
plt.subplots_adjust(wspace =0.5, hspace =0.5)
plt.savefig('ColumnDensity')
plt.show()
'''
#create a filament
#fits data
Ap=np.pi/2
rho=1
Rflat=10
p=2
r=np.arange(-50,51,1)
n=np.zeros((101,101))
for i in range(101):
    n[i,:]=coldsty(r,Ap,rho,Rflat,p)
plt.plot(r,n[0,:])
plt.show()

#write to fits
hdu=fits.PrimaryHDU(n)
hdul=fits.HDUList([hdu])
hdul.writeto('2Ddensity.fits')