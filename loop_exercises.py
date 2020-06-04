import numpy as np
question = int(input("Enter number 1-12: "))

if question == 1:
    for i in range(1,11):
        print(i)

if question == 2:
    n = int(input('Start from: '))
    m = int(input('End on: '))
    for i in range(n,(m+1)):
        print(i)

if question == 3:
    for i in np.arange(1,10,2):
        print(i)

if question == 4:
    for i in range(1,6):
        stars = ""
        for t in range(1,6):
            stars += "*"
        print("".join(stars))

if question == 5:
    length = int(input('How many stars? ')) + 1
    for i in range(1,length):
        stars = ""
        for t in range(1,length):
            stars += "*"
        print("".join(stars))

if question == 6:
    height = int(input('Height? '))
    width = int(input('Width? '))
    for i in range(1,height+1):
        stars = ""
        for t in range(1,width+1):
            if (i == 1) or (i == height):
                stars += "*"
            elif (t == 1) or (t == width):
                stars += "*"
            else:
                stars += " "
        print("".join(stars))

if question == 7:
    height = 4
    for i in range(1,(height +1 )):
        stars = ""
        for j in range(1,(2*height)):
            if (j<(height+1-i)) or (j>(height-1+i)):
                stars += " "
            else:
                stars += "*"
        print("".join(stars))

if question == 8:
    height = int(input("How many rows? "))
    for i in range(1,(height +1 )):
        stars = ""
        for j in range(1,(2*height)):
            if (j<(height+1-i)) or (j>(height-1+i)):
                stars += " "
            else:
                stars += "*"
        print("".join(stars))

if question == 9:
    for i in range(1,11):
        for j in range(1,11):
            print(f'{i} X {j} = '+str(i*j))

if question == 10:
    text = input('Text to Bannerize? ')
    for i in range(3):
        stars = ""
        if i != 1:
            for i in range(len(text)+4):
                stars += "*"
        else:
            stars = "* " + text + " *"
        print("".join(stars))

if question == 11:
    for i in range(1,101):
        print(i*(i+1)/2)

if question == 12:
    print('Please don\'t actually use naive facorization...')
    base = abs(int(input("Fine, what do you want to factor? ")))
    current = base/1

    factors = []
    i = 2
    while i < current:
        if current % i == 0:
            factors.append(i)
            current /= i
            i = 2
        else:
            i += 1
    factors.append(int(current))
    print(factors) 
