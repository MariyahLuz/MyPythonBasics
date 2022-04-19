#This program checks to see if the city entered belongs to a certain country and returns that country, else returns unknown

usa=['atlanta', 'new york', 'chicago', 'baltimore']
uk=['london', 'bristo', 'cambridge']
ug=['kampala', 'wakiso', 'jinja', 'mbarara']

name= input('Enter the name of your city: ')

if name in usa:
    print('Your in USA...')

elif name in uk:
    print('Your in UK...')

elif name in ug:
    print('Your in UG...')

else:
    print('Unknown city name')
