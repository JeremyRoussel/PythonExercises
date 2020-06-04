import fire
import matplotlib.pyplot as plt
import numpy as np

class Functions(object):
    ### A simple function class ###

    def hello(self, entry):
        return ("Hello, "+entry+"!")

        # To run, use the following
        # python3 Functions.py hello 'Jeremy'

    def f(self, x):
        xs = np.array(x)
        ys = xs +1
        plt.plot(xs,ys)
        plt.show()

        # To run, use the following
        # python3 Functions.py f '[-3,-2,-1,0,1,2,3]'

    def squares(self, strt, end):
        x = np.arange(strt, end, step=1)
        y = x**2
        plt.plot(x,y)
        plt.show()

        # To run, use the following
        # python3 Functions.py squares -100 100
    
    def odd_even(self, xs):
        x = np.array(xs)
        y = np.empty_like(x)
        for i, v in enumerate(x):
            if v % 2 == 0:
                y[i] = -1
            else:
                y[i] = 1
        plt.bar(x,y)
        plt.show()

        # To run, use the following
        # python3 Functions.py odd_even '[-5,-4,-3,-2,-1,0,1,2,3,4,5]'

    def sinwave(self, xs, xe):
        x = np.arange(xs, xe, step=1)
        y = np.sin(x)
        plt.plot(x,y)
        plt.show()

        # To run, use the following
        # python3 Functions.py sinwave -5 5

    def sinwave2(self, xs, xe):
        x = np.arange(xs, xe, step=.1)
        y = np.sin(x)
        plt.plot(x,y)
        plt.show()

        # To run, use the following
        # python3 Functions.py sinwave2 -5 5

    def degree_conv(self, xs, xe):
        x = np.arange(xs, xe, step=1)
        y = x*1.8 + 32
        plt.plot(x,y)
        plt.show()

        # To run, use the following
        # python3 Functions.py degree_conv -20 100

    def play_again(self):
        resp = input('Do you want to play again? (Y/N) ')
        if resp == 'Y':
            return True
        else:
            return False

        # To run, use the following
        # python3 Functions.py play_again

    def play_again_again(self):
        resp = ""
        accepted = {"Y":True, "N":False}
        while resp not in accepted:
            resp = input('Do you want to play again? (Y/N) ')    
        return accepted[resp]

        # To run, use the following
        # python3 Functions.py play_again_again

    def smallest(self, numList):
        nums = np.array(numList)
        return np.min(nums)
    
    def largest(self, numList):
        nums = np.array(numList)
        return np.max(nums)
    
    def shortest(self, strList):
        shrt = len(strList[0])
        strValue = strList[0]
        for i in strList:
            if len(i) < shrt:
                shrt = len(i)
                strValue = i
        return strValue

    def longest(self, strList):
        lngst = len(strList[0])
        strValue = strList[0]
        for i in strList:
            if len(i) > lngst:
                lngst = len(i)
                strValue = i
        return strValue


if __name__ == "__main__":
    fire.Fire(Functions)