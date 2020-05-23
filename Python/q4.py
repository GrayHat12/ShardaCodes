from dateutil import parser
date = input('Input your DOB in month-date format : ')
datetime = None
try :
    datetime = parser.parse(date)
except:
    print('Invalid Input')
    exit(1)
day = datetime.day
month = datetime.month
if month == 1:
    if day <= 20:
        print('Capricon')
    elif day >= 21:
        print('Aquarius')
elif month == 2:
    if day <= 18:
        print('Aquarius')
    elif day >= 19:
        print('Pisces')
elif month == 3:
    if day <= 20:
        print('Pisces')
    elif day >= 21:
        print('Aries')
elif month == 4:
    if day <= 20:
        print('Aries')
    elif day >= 21:
        print('Taurus')
elif month == 5:
    if day <= 21:
        print('Taurus')
    elif day >= 22:
        print('Gemini')
elif month == 6:
    if day <= 21:
        print('Gemini')
    elif day >= 22:
        print('Cancer')
elif month == 7:
    if day <= 22:
        print('Cancer')
    elif day >= 23:
        print('Leo')
elif month == 8:
    if day <= 23:
        print('Leo')
    elif day >= 24:
        print('Virgo')
elif month == 9:
    if day <= 22:
        print('Virgo')
    elif day >= 23:
        print('Libra')
elif month == 10:
    if day <= 23:
        print('Libra')
    elif day >= 24:
        print('Scorpio')
elif month == 11:
    if day <= 22:
        print('Scorpio')
    elif day >= 23:
        print('Sagittarius')
elif month == 12:
    if day >= 22:
        print('Capricon')
    elif day <= 21:
        print('Sagittarius')