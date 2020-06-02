days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
try: 
    day = int(input('Enter the day of the week! (0-6) '))
    if day >= 0 and day <= 6:
        print(days[day])
    else:
        print('Please only enter a number from 0-6!')
except:
    print('Please only enter a number from 0-6!')
