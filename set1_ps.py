# Set 2 - Easy-Level Python Problem-Solving Questions
#  1. Multiply all elements in a list
#  Input: [2, 3, 4]
#  Output: 24

l=[2, 3, 4]
mul=1
for i in l:
    mul*=i
print(mul)

#  2. Find minimum value in a list
#  Input: [8, 3, 5]
#  Output: 3

l1=[8,3,5]
l1.sort()
print(l1[0])

#  3. Find count of odd numbers in a list
#  Input: [2, 5, 7, 8]
#  Output: 2

l1=[2, 5, 7, 8]
odd_count=0
for i in l1:
    if i%2 != 0:
        odd_count+=1
print(odd_count)

# 4. Find difference between max and min
#  Input: [4, 7, 2, 9]
#  Output: 7

l3=[4, 7, 2, 9]
l3.sort()
print(l3[-1] - l3[0])

#  5. Sum of only positive numbers
#  Input: [-1, 3, 5, -2]
#  Output: 8
 
l4=[-1, 3, 5, -2]
s=0
for i in l4:
    if i>=0:
        s+=i
print(s)

#  6. Get keys with even values from dict
#  Input: {'a': 2, 'b': 3, 'c': 4}
#  Output: ['a', 'c']

dict1= {'a': 2, 'b': 3, 'c': 4}
l=[]
for keys in dict1:
    if dict1[keys] % 2==0:
        l.append(keys)
print(l)

#  7. Update value of a key in a dictionary
# Input: {'a': 1, 'b': 2}, change 'a' to 10
#  Output: {'a': 10, 'b': 2}

dict2={'a': 1, 'b': 2}
dict2['a']=10
print(dict2)

# 8. Check if a key exists in a dictionary
#  Input: {'x': 5}, check key 'x'
#  Output: True

dict4={'x': 5}
for key in dict4:
    if key=='x':
        print("True")
    else:
        print("False")

#  9. Print only dictionary keys
#  Input: {'name': 'Ava', 'age': 21}
#  Output: ['name', 'age']
 
dict5={'name': 'Ava', 'age': 21}
l=[]
for key in dict5:
    l.append(key)
print(l)
 

#  10. Add new key-value if key doesn't exist
#  Input: {'x': 1}, add 'y': 2
#  Output: {'x': 1, 'y': 2}

dict6={'x': 1}
for key in list(dict6):
    if key != 'y':
        dict6['y']=2
   
print(dict6)


# 11. Check if a number is even or odd
#  Input: 9
#  Output: Odd

n=9
if n%2 !=0:
    print("odd")
else:
    print("even")
    
#  12. Find factorial of a number
#  Input: 5
#  Output: 120

n=5
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)

#  13. Check if a number is prime
#  Input: 7
#  Output: Prime

n=7
c=0
for i in range(2,n):
    if n%i==0:
        c+=1
        break
if c==0:
    print("prime")
else:
    print("not prime")

# 14. Reverse digits of a number
#  Input: 1234
#  Output: 4321

n=1234
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
print(rev)

#  15. Count digits in a number
#  Input: 789
#  Output: 3

n=789
c=0
while n>0:
    r=n%10
    c+=1
    n=n//10
print(c)
