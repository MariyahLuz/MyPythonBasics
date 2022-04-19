#This program checks to see if the cities entered belong to the same country or not

usa=['atlanta', 'new york', 'chicago', 'baltimore']
uk=['london', 'bristo', 'cambridge']
ug=['kampala', 'wakiso', 'jinja', 'mbarara']

name1= input('Enter your favorite city 1: ')
name2= input('Enter your favorite city 2: ')

if name1 in usa and name2 in usa:
    print('Both of these cities are in USA')

elif name1 in uk  and name2 in uk:
    print('Both of these cities are in UK')

elif name1 in ug and name2 in ug:
    print('Both of these cities are in UG')

else:
    print('Both of the cities do not belong to the same country')

