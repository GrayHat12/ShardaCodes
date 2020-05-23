def is_prime(number):
    if number <= 1:
        return False
    for x in range(2, number):
        if not number % x:
            return False
    return True

count = 0
print('Prime numbers till 100 are : ')
for i in range(1,101):
    if is_prime(i):
        print(i)
        count+=1
print ('Number of primes encountered :',count)