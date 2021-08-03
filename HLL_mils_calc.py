import numpy as np
from numpy.polynomial import Polynomial as Poly

# Fit HLL artillery data
data = np.loadtxt('HLL_artillery_data.csv',delimiter=',')
x = data[:,0]
y = data[:,1]
p_fitted = Poly.fit(x,y,deg=1).convert()

# Calculate
while(1):
    x_in = input('Distance: ')
    if(x_in.isdigit()):
        print('Mils: ',p_fitted(int(x_in)))
    elif x_in == 'exit':
        break
    else:
        print('Please input number.')
