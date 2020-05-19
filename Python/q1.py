import datetime

current_year = datetime.datetime.now()
current_year = current_year.year

name = input('Enter Name : ')
age = int(input('Enter age : '))

print('Hello',name)
print('You\'ll turn 100 in the year',current_year-age+100)