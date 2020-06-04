party = int(input('How many people? '))

try: 
    check = float(input('Enter the amount of the bill! '))
    if check >= 0:
        tips = {'good':.2, 'fair':.15, 'poor':.1}
        service = ""
        while service not in tips:
            service = input('Was the service good, fair, or bad? ')
        print('Each Person pays ${:.2f}'.format(check*(1+tips[service])/party))
    else:
        print('Please only enter a positive number!')
except:
    print('Please only enter numerical values!')
