import math
import numpy as np

### FizzBuzz

for n in range(1,101):  #Loop through numbers from 1 to 100
    state = ""  #Reset print statement
    if n%3 == 0:   #If divisible by three, add Fizz to the print
        state += "Fizz"
    if n%5 == 0:  #If divisible by five, add Buzz to the print
        state += "Buzz"
    if state != "":  #Print number and statement if it's a factor
        print(f"{n} = {state}")

### Sum all 3 or 5 below 1000

total = 0  #Set total to zero
for n in range(1,1000):  #Go through 1 to 999
    if (n%3 == 0) or (n%5 == 0): #If number can be divisible by 3 or 5
        total += n #add to total

print()
print(f'Sum of all numbers with 3 and 5 as a factor = {total}')

### Fibonacci Sequence

n = [1, 2]  #Initialization of Fib
while n[-1] < 4E6:  # Add numbers to sequence while last is less than 4 million
    n.append(n[-1]+n[-2])  # Append new Fibonacci term
n.pop() # Remove last term, since it will be more than 4 million

fib_sum = 0  # Init for sum
for i in n:  # Loop over all numbers in the sequence
    if i%2 == 0:  #If number is divisble by 2
        fib_sum += i #Add to the sum


print()
print(f'Fibonacci Sum of all even numbers in the sequence less than 4,000,000 = {fib_sum}')

### Largest Prime

## Define function for evaluating if prime or not

def isprime(x):
    for n in range(2,int(x**.5)+1):  #Loop over sequence from 2 to the square root of the number, rounded up
        if x%n == 0:  # If there is a factor in the sequence,
            return False  #Return that it is not a prime
    return True #Return is prime since it was not divisible


base = 600851475143  #starting number
current = base/1  #Current iterable number

factors = []  #init of factors
i = 2  #start of loop
while i < current:  #While loop for finding factors
    if current % i == 0: #If a factor is found..
        factors.append(i) #Add it to the factor list
        current /= i  #Reduce the current iterable
        i = 2  #Reset the iteration variable
    else:
        i += 1
factors.append(int(current))

print()
print(f'Prime factors of {base} are {factors}') 

largest = -1
for n in factors:
    if isprime(n) == True:
        largest = n


print(f'The largest of these is {largest}')

### 10,001 Prime

which_prime = 10001

def prime_n(x):
    n_primes = 1
    i = 2
    while n_primes < x:
        i += 1
        if isprime(i) == True:
            n_primes += 1
    return i

print()
print(f'The {which_prime}st prime number is {prime_n(which_prime)}')