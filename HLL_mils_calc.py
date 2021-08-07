import numpy as np
from numpy.polynomial import Polynomial as Poly


class Calculator():
    def __init__(self):
        # Fit HLL artillery data
        data = np.loadtxt('HLL_mils_622.csv',delimiter=',')
        self.p_fitted_622 = Poly.fit(data[:,0],data[:,1],deg=1).convert()

        data = np.loadtxt('HLL_mils_800.csv',delimiter=',')
        self.p_fitted_800 = Poly.fit(data[:,0],data[:,1],deg=1).convert()

        self.p_fitted = self.p_fitted_622

    def calc(self,distance):
        return self.p_fitted(distance)

    def change_num(self,num):
        if num == 622:
            self.p_fitted = self.p_fitted_622
        elif num == 800:
            self.p_fitted = self.p_fitted_800
        else:
            pass


def main():
    # init
    calculator = Calculator()

    print('''Usage: 
            1. type number to calculate mils
            2. type 'change xxx' to change mils data
            3. type 'exit' to exit''')

    while(1):
        x_in = input('Distance: ')
        if(x_in.isdigit()):
            print('Mils: ',calculator.calc(int(x_in)))
        elif 'change' in x_in:
            num = int(x_in.removeprefix('change '))
            calculator.change_num(num)
            print('MILs data change to',num)
        elif x_in == 'exit':
            break
        else:
            print('Please input number.')


if __name__ == '__main__':
    main()
