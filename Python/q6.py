a = int(input('a : '))
b = int(input('b : '))
c = int(input('c : '))
count = 0
for i in range(a,b):
    if i%c == 0:
        count+=1
print(count,' numbers between',a,'and',b,'are divisible by',c)