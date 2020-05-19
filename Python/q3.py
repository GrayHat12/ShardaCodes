current = int(input('Current time in hours : '))
travel = int(input('How many hours ahead ? '))
newtime = (current + travel) % 12
print('New hour',str(newtime)+'\'o clock')