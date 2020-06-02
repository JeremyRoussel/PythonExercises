try: 
    tempc = int(input('Enter the degrees in Celcius! '))
    if tempc >= -273.15:
        print(tempc*1.8 + 32)
    else:
        print('Please only enter a temperature above absolute zero!')
except:
    print('Please only enter a numerical value!')
