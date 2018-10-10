#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 19:00:43 2018

@author: meng
"""

import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits

fits_image_filename = fits.util.get_testdata_filepath('test0.fits')
hdul = fits.open(fits_image_filename)
#hdul.info()
#print(hdul[0].header['DATE'])
hdr = hdul[0].header
#print(list(hdr.keys()))
hdr.set('observer', 'Meng Yao')
print(hdr['observer'])
