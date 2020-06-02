days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
try: 
    day = int(input('Enter the day of the week! (0-6) '))
    if day == 0 or day == 6:
        print('Sleep In!')
    elif day >=1 and day <= 5:
        print('Work!')
    else:
        print('Please only enter a number from 0-6!')
except:
    print('Please only enter a number from 0-6!')
