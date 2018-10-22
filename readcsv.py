'''
test read csv files
Meng, 22 oct 2018
'''
import numpy as np
a=np.genfromtxt('FLMTStable.csv',delimiter=';')
table=a[11:28,:]
print(table)
