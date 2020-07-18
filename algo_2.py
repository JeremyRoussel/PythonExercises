import fire
import numpy as np

class Functions(object):

    def Collatz(self, num):
        test = 1
        print(num)
        while num != test:
            if num%2 == 0:
                num = num/2
                print(num)
            else:
                num = num*3 +1
                print(num)
        print('Done!')

# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

    def isPalindrome(self, string): 
        return string == string[::-1] 

    def Palindrome(self):
        expression_list = np.arange(999,900, -1)
        start = 999
        max_palin = 0

        while start > 950:
            
            for counter, value in enumerate(expression_list):
                num_check = start*value
                stringcheck = str(num_check)
                
                if self.isPalindrome(stringcheck) == True:
                    if num_check > max_palin:
                        max_palin = num_check
            
            start -= 1

        print(max_palin)

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

    def findNum(self):
        i = 2520
        notfound = True

        while (notfound):
            i += 2520
            isDividable = True
            j = np.arange(11,20,1)
            for n in j:
                if (i % n != 0):
                    isDividable = False
                    break
            if (isDividable):
                notfound = False
        return i

    def findNum2(self):
        i = 2520
        notfound = True

        while (notfound):
            i += 2520
            isDividable = False
            j = np.arange(11,20,1)
            
            k = np.divide(i, j)
            l= np.floor_divide(i,j)
            if (k == l).all():
                isDividable = True
                break
            if (isDividable):
                notfound = False
        return i

if __name__ == "__main__":
    fire.Fire(Functions)


# Collatz(17)
# Collatz(20)
# Collatz(109)
