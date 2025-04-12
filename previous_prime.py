num= 20
prev=num
prev_prime_not_found=True
while prev_prime_not_found:
    prev-=1
    count=0
    for i in range(2,prev):
       if prev%i==0:
        count+=1
        break
    if count==0:
        print(f"{prev} is the previous prime")
        prev_prime_not_found=False
        
'''
Enter a number:5
3 is the previoud prime
'''
        

nxt=num
nxt_prime_not_found=True
while nxt_prime_not_found:
    nxt+=1
    count=0
    for i in range(2,nxt):
       if nxt%i==0:
        count+=1
        break
    if count==0:
        print(f"{nxt} is the next prime")
        nxt_prime_not_found=False
if (num - prev) <= (nxt - num):
    print(f"{prev} is the nearest prime to {num}")
else:
    print(f"{nxt} is the nearest prime to {num}")

'''
Enter a number:6
7 is the next prime
'''

'''Nearest prime'''

num= 20
prev=num
prev_prime_not_found=True
while prev_prime_not_found:
    prev-=1
    count=0
    for i in range(2,prev):
       if prev%i==0:
        count+=1
        break
    if count==0:
        # print(f"{prev} is the previous prime")
        prev_prime_not_found=False
nxt=num
nxt_prime_not_found=True
while nxt_prime_not_found:
    nxt+=1
    count=0
    for i in range(2,nxt):
       if nxt%i==0:
        count+=1
        break
    if count==0:
        # print(f"{nxt} is the next prime")
        nxt_prime_not_found=False
nearest = prev if (num - prev) <= (nxt - num) else nxt
print(f"{nearest} is the nearest prime to {num}")

'''19 is the nearest prime to 20'''

        