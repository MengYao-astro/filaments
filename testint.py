#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 13:26:34 2019

@author: meng
"""

import numpy as np
from scipy import integrate
f = lambda x : 1/(x**2+1)**2
Ap=integrate.quad(f,-float('inf'),float('inf'))[0]