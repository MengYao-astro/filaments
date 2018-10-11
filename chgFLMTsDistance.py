#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 11 oct 2018 14:00

@author: meng
"""

import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits

#fits_image_filename = fits.util.get_testdata_filepath('/home/yao/work/filaments/FLMTex.fits')
hdul = fits.open('FLMTex.fits')
hdul.info()
