#Create a function that takes two numbers as arguments and returns their sum.

def sum(num1,num2):
    return num1+num2
a=int(input("enter a numbers "))
b=int(input("enter a numbers "))
result=sum(a,b)
print("the sum of two numbers is",result)


# Write a function that takes an integer minutes and converts it to seconds.

def seconds(min):
    return min*60
min=int(input('enter a number of min'))
if(min>0):
    print("for",min,' minutes the seconds are ',(seconds(min)))
else:
    print("please enter valid number ")


# Create a function that takes a number as an argument, increments the number by +1 and returns the result.


def increment(num):
    return num+1
num=int(input('enter a number'))
print(increment(num))


# Create a function that takes the age in years and returns the age in days.

year=int(input("enter age in years"))
def days(year):
    non_leap=0
    leap=0
    if(year<=0):
        print("enter positive number")
        exit
    for i in range(1,year+1):
        if(i%4):
            non_leap+=1
        else:
            leap+=1
    return ((leap*366)+(non_leap*365))
result=days(year)
print(result)
        
# sbi Create a function that takes voltage and current and returns the calculated power.


def power(v,i):
    print("power is",(v*i))
while(True):
    v=int(input("enter  voltage"))
    i=int(input("enter a current value"))
    if(v>1 and i>1):
        power(v,i)
        break
    else:
        print("enter valid input")


#6.Write a function that returns the string "something" joined with a space " " and the given argument a.

def strjoin(a):
    
    return "something"+" "+str(a)

print(strjoin(12))

'''o/p:  something sanju'''


#7.Create a function that takes two arguments. Both arguments are integers, a and b. Return true if one of them is 10 or if their sum is 10.

def sum_fun(a,b):
    if a==10 or b==10 or a+b==10 :
        return True
a=10
b=20
print(sum_fun(a,b))


#8.Create a function that takes two strings as arguments and returns either true or false depending on whether the total number of characters in the first string is equal to the total number of characters in the second string.
# 
def str_fun(str1,str2):
    if(len(str1)==len(str2)):
        return True
    else:
        return false
str1="sanju"
str2="madhu"
print(str_fun(str1,str2))

def size(str):
    c=0
    for i in str:
        c+=1
    return c
def str_fun(str1,str2):
    if(size(str1)==size(str2)):
        return True
    else:
        return False
str1="sanju"
str2="madhu"
print(str_fun(str1,str2))

# 9.Create a function that takes a name and returns a greeting in the form of a string. Don't use a normal function, use an arrow function.
'''Lambda Function
Lambda functions in Python are used for creating small, anonymous functions in a single line. They can be helpful in situations where you need a simple function for a short period of time, without the need for defining a full function using the def keyword.'''

greet = lambda name: "Hello, " + name + "!"
print(greet("Sanjay"))

#o/p:Hello, Sanjay!


# greet = lambda first_name,last_name: "Hello, " + first_name +" "+ last_name + "!"
# print(greet("Sanjay","Ramaswami"))

'''o/pHello, SanjayRamaswami!'''

#10.Create a function that takes an array of 10 numbers (between 0 and 9) and returns a string of those numbers formatted as a phone number (e.g. (555) 555-5555).

def arr_pn(numbers):
       return f"({numbers[0]}{numbers[1]}{numbers[2]}) {numbers[3]}{numbers[4]}{numbers[5]}-{numbers[6]}{numbers[7]}{numbers[8]}{numbers[9]}"

a = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
phone_number = arr_pn(a)
print(phone_number)

'''
o/p:
(555) 555-5555
'''


#11.Create a function that returns an array of strings sorted by length in ascending order.
# Example:
# sortByLength(["a", "ccc", "dddd", "bb"]) ➞ ["a", "bb", "ccc", "dddd"]

def sort(arr):
    for i in range (len(arr)):
        for j in range (len(arr)):
            if arr[i]<arr[j]:
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
    return arr   
print(sort(["a", "ccc","dddd","bb"]))

'''
['a', 'bb', 'ccc', 'dddd'] '''


# Create a function that takes an array of arrays with numbers. Return a new (single) array with the largest numbers of each.
# Example:
# findLargestNums([[4, 2, 7, 1], [20, 70, 40, 90], [1, 2, 0]]) ➞ [7, 90, 2]

def sort(arr):
    lst=[]
    for i in arr:
        i.sort()
        lst.append(i[-1])
    return lst

print(sort([[4, 2, 7, 1], [20, 70, 40, 90], [1, 2, 0]]))


''' [7, 90, 2] '''



# 13.Create a function that takes an array of numbers and returns the second largest number.
# Example:
# secondLargest([10, 40, 30, 20, 50]) ➞ 40


arr=[10,40,30,20,50]
for i in range(len(arr)):
  for j in range(i+1):
    if arr[i]>arr[j]:
      x=arr[i]
      arr[i]=arr[j]
      arr[j]=x
print(arr[1])

# 14.Create a function that takes an array of items, removes all duplicate items and returns a new array in the same sequential order as the old array (minus duplicates).
# Example:

# removeDups([1, 0, 1, 0]) ➞ [1, 0]

# removeDups(["The", "big", "cat"]) ➞ ["The", "big", "cat"]

def duprem_arr(a):
    x=[]
    for i in a:
        if i not in x:
            x.append(i)
           
    return x
print(duprem_arr((["The", "big", "cat","cat"]) ))
    
'''o/p:
['The', 'big', 'cat']'''

# 15.Create a function that takes an array of integers as an argument and returns a unique number from that array. All numbers except unique ones have the same number of occurrences in the array.

# Example:

# findSingleNumber([2, 2, 2, 3, 4, 4, 4]) ➞ 3

def unique(a):
 
    for i in a:
        c=0
        for j in a:
            if i==j:
                c+=1
        if c==1:
            print(i)
        
unique([2, 2, 2, 3, 4, 4, 4])    



# 16.Create a function that takes two strings as arguments and returns the number of times the first string (the single character) is found in the second string.
# Example:

# charCount("c", "Chamber of secrets") ➞ 1
def charcount(c,s):
    count=0
    for i in s:
        if i in c:
            count+=1
        else:
            pass
    return count
            
print(charcount("e", "Chamber of secrets"))

'''
3

'''
# 17.Create a function that takes a string and returns the number (count) of vowels contained within it.
# Example:

# countVowels("Celebration") ➞ 5

def countvowels(s):
    l=['A','E','I','O','U','a','e','i','o','u']
    c=0
    for i in s:
        if i in l:
            c+=1
    return c
print(countvowels("Celebration"))

''' 5 '''

# 18.Given a string, create a function to reverse the case. All lower-cased letters should be upper-cased, and vice versa.
# Example:
# reverseCase("Happy Birthday") ➞ "hAPPY bIRTHDAY"

def revcase(s):
    str=""
    for i in s:
        if i==i.upper():
            str+=i.lower()
        else:
            str+=i.upper()
    return str
print(revcase("Happy Birthday"))
            
''' o/p:
hAPPY bIRTHDAY'''


# 19.Take one integer n, loop till n and pass each value to a function, create a function that takes one integer parameter, and multiply with 2 in every integer.
			
			# Input:      n=5
			# Output:   2 4 6 8 10

			# Explanation:  Loop start with 1 go till 5 bcoz n=5
			# 		1 x 2 =2, 2 x 2=4, 3 x 2=6 …..etc 



def mul(n):
    for i in range(1,n+1):
        print(i ,'*','2' ,'=', i*2 ,end=" ")
mul(5)


# 20.Create Function that will take one parameter and return types of the data.
			
			# Input:       500
			# Output:     Integer

			# Input:       Coding
			# Output:    String

def typeof(x):
    types = type(x).__name__
    if types=='int':
        print("Integer")
        
    elif types=='str':
        print("String")
        
    elif types=='float':
        print("float")
        
    else:
        print("complex")
        
typeof(7.00)
'''o/p:
float
'''


# 21.Program to find greatest of three numbers(using ternary operator).

			# Input:  4 8 2
			# Output: 8 is greatest
   
a,b,c=4,8,2
print(a) if (a>b and b>c) else print(b) if(b>c) else print(c)

'''p/p:
8
'''

# 22 . C Program to find factorial of number.
		
# 			Input: n=5
# 			Output: 120

# 			Explanation: 5 x 4 x 3 x 2 x 1 = 120
	
#  23. C Program to arrange numbers in ascending order
# 			Input: [2,3,1,5,4]
# 			Output: [1,2,3,4,5]

# 		        Sort the Array using loop only(you can not use predefined function).


# 24. Print Patter using loop.

# 			1
# 			1 2
# 			1 2 3
# 			1 2 3 4
#   		1 2 3 4 5


for i in range(6):
    for j in range(1,i+1):
        print(j ,end=" ")
    print()

'''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 '''

# 25. C Program to Calculate the Power of a Number(using loop only).

# 			Input: n=5, p=3
# 			Output: 5 ^ 3 = 125
# 			Explanation: 5 x 5 x 5 = 125


def power(n,p):
    product=n
    for i in range(1,p):
        product*=n
    return product
print(power(5,3))
  
'''
125''' 

# 26.Program to Check Whether a Number is Prime or Not

			# Input: 9
			# Output: 9 is not a prime no

			# Input: 7
			# Output : 7 is a prime no

num = 4
c=0
if num>2:
    for i in range(2,num):
        if num % i==0:            
            print(num,"is not prime")
            c=c+1
            break
    if c==0:   
        print(num,"is prime")
        

#  27. Program to find LCM of two numbers using while loop

# 			Input: 15 50
# 			Output: Lcm of 15 and 50 is 150.

ip1=15
ip2=12
max=ip1 if (ip1>ip2) else ip2

while True:
    if(max%ip1==0 and max%ip2==0):
        print("lcm is:",max)
        break
    max+=1

'''o/p:
lcm is: 60

'''

#  28.Program to Display Characters from A to Z Using Loop with count.

# 			Output: A1 B2 C3 D4 E5 F6 ……. Z26 

alphabet = "abcdefghijklmnopqrstuvwxyz"
c=1
for letter in alphabet:
    print(letter.upper(),c ,end=" ")
    c+=1
	

for i in range(1,27):
    print(chr(64+i),i,end=" ")

'''
A 1 B 2 C 3 D 4 E 5 F 6 G 7 H 8 I 9 J 10 K 11 L 12 M 13 N 14 O 15 P 16 Q 17 R 18 S 19 T 20 U 21 V 22 W 23 X 24 Y 25 Z 26 
'''

#29. Program to find a missing number

# 			Input:  n=5(length of array), arr= [5,3,1,4]
# 			Output: 2 is missing

n=[]
for i in range(1,6):
    n.append(i)

arr=[5,3,1,4]
arr.sort()
for num in n:    
    if num not in arr:
      print(num,"is missing")
'''
o/p:
2 is missing'''

# 30.Program to count vowels and consonants in a given String.

			# Input: i am ram
            # Output: 3 vowels 3 consonants.
            
lst=['a','e','i','o','u','A','E','I','O','U']
lst1=[" "]
str="i am ramii"
vc=0
cc=0
for i in str:
    if i in lst:
        vc+=1
    elif i not in lst1:
        cc+=1
print(vc ,"vowels",cc,"cononants")

''' 
o/p:
5 vowels 3 cononants'''

#  31.program to insert  the elements of an array for specific index.

# 			Input: [1,2,3,4,5,7,8,9,10] , index=5
# 			Output: [1,2,3,4,5,6,78,9,10]

x=[1,2,3,4,5,7,8,9,10]
index=5
x[index]=6
print(x)

'''
[1,2,3,4,5,6,78,9,10]'''

# 32.Reverse a number using while Loop

# 			Input: 123
# 			Output: 321

n=123
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
print(rev)

'''o/p:
321
'''

# 33 Count occurrence of number:

# 			Input: [1,6,3,1,5,9,7,2,1,9,3,7,8,9,10] , no find=7
# 			Output: 7 present 2 times.

arr = [2, 3, 2, 4, 5, 3, 3] 
a = []  
for i in arr:
    if i not in a:
        a.append(i)
for num in a:
    count = 0  
    for val in arr:
        if num == val:
            count += 1
            
    if count > 1 or count==1: 
        print(num, "appears", count, "times")

'''
o/p:
2 appears 2 times
3 appears 3 times

'''



'''Level:Mediummmm'''




#1. Write a function that converts an object into an array, where each element represents a key-value pair in the form of an array.

# Examples :

# toArray({ a: 1, b: 2 }) ➞ [["a", 1], ["b", 2]]

# toArray({ shrimp: 15, tots: 12 }) ➞ [["shrimp", 15], ["tots",12]]

# toArray({}) ➞ []


def toArray(obj):
    result = []
    for i in obj:
        result.append([i, obj[i]])  
    return result


print(toArray({ "a": 1, "b": 2 }))  
print(toArray({ "shrimps": 15, "tots": 12 }))  
print(toArray({}))  


'''
[['a', 1], ['b', 2]]
[['shrimps', 15], ['tots', 12]]
[]
'''

#2. Create a function that takes two numbers as arguments (num, length) and returns an array of multiples of num until the array length reaches length.
# Examples :

# arrayOfMultiples(7, 5) ➞ [7, 14, 21, 28, 35]

# arrayOfMultiples(12, 10) ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]

# arrayOfMultiples(17, 6) ➞ [17, 34, 51, 68, 85, 102]


def arrayOfMultiples(num,length):
    l=[]
    for i in range(1,length+1):
        l.append(num*i)
    print(l)

arrayOfMultiples(7, 5) 
arrayOfMultiples(12, 10)


'''
7, 14, 21, 28, 35]
[12, 24, 36, 48, 60, 72, 84, 96, 108, 120]

'''


# 3.create the function that takes an array with objects and returns the sum of people's budgets.

# Examples :

# getBudgets([
#   { name: "John", age: 21, budget: 23000 },
#   { name: "Steve",  age: 32, budget: 40000 },
#   { name: "Martin",  age: 16, budget: 2700 }
# ]) ➞ 65700

# getBudgets([
#   { name: "John",  age: 21, budget: 29000 },
#   { name: "Steve",  age: 32, budget: 32000 },
#   { name: "Martin",  age: 16, budget: 1600 }
# ]) ➞ 62600


def getBudgets(x):
    s=0
    for i in x:
  	  s+=i["budget"]
     
    print(s)
   
getBudgets([
  { "name": "John", "age": 21, "budget": 29000 },
  { "name": "Steve",  "age": 32, "budget": 32000 },
  { "name": "Martin",  "age": 16, "budget": 1600 }
])
'''
62600
'''


# 4.Create a function that takes an array of objects like { name: "John", notes: [3, 5, 4]} and returns an array of objects like { name: "John", avgNote: 4 }. If a student has no notes (an empty array) then let's assume avgNote: 0.
# 	Example :

# [
#   { name: "John", notes: [3, 5, 4]}
# ] ➞ [
#   { name: "John", avgNote: 4 }
# ]


def arrobj(students):
    result = [] 

    for student in students:
        notes = student["notes"]
        sum = 0
        count = 0
        for num in notes:
            sum += num
            count += 1  
        if count > 0:
            avg_note = sum // count
        else:
            avg_note = 0
        
        new_student = { "name": student["name"], "avgNote": avg_note }
        result.append(new_student) 
    return result  

students_data = [
    { "name": "John", "notes": [3, 5, 4] }
]

print(arrobj(students_data))


'''

[{'name': 'John', 'avgNote': 4}]

'''


# 5.Create a function that moves all capital letters to the front of a word.
# 	Examples :

# capToFront("hApPy") ➞ "HAPpy"

# capToFront("moveMENT") ➞ "MENTmove"

# capToFront("shOrtCAKE") ➞ "OCAKEshrt"


def capToFront(s):
    caps = ""  
    lowers = ""  
    for char in s:
        if 'A' <= char <= 'Z':  
            caps += char  
        else:
            lowers += char  

    return '"'+caps + lowers+'"'

print(capToFront("hApPy"))       
print(capToFront("moveMENT"))    
print(capToFront("shOrtCAKE"))   

'''
"APhpy"
"MENTmove"
"OCAKEshrt"
'''

#6.Count each occurrence of number(can not use predefined function).

# 			Input: [1,6,3,1,5,9,7,2,1,9,3,7,8,9,10] , no find=7
# 			Output: 1 present 2 times.
# 				   2 present 1 times.
# 				   3 present 2 times.
# 				   5 present 1 times …….  Etc

l= [1,6,3,1,5,9,7,2,1,9,3,7,8,9,10]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
        
for num in l1:
    c=0
    for x in l:
        if num==x:
            c += 1
          
    if c==1 or c>1:
        print(num,"present",c,"times" )




'''
1 present 3 times
6 present 1 times
3 present 2 times
5 present 1 times
9 present 3 times
7 present 2 times
2 present 1 times
8 present 1 times
10 present 1 times



'''
# # 			Input: [1,6,3,1,5,9,7,2,1,9,3,7,8,9,10] , no find=7
# # 			Output: 7 present 2 times.

arr = [1,6,3,1,5,9,7,2,1,9,3,7,8,9,10]
x=7
count = 0  
for num in arr:
    if x == num:
        count += 1               
print(x, "appears", count, "times")

''' 
7  appears 2 times'''


#7. Write a function that accepts an array of strings. Return the longest string(can not use predefined function).

# 		Input: [‘nik’, ’mikhil’, ’Cow’,’Elephant’] 							Output: Elephant


def arrBig(s):
    max=' '
    for i in s:
        if len(max)<len(i):
            max=i
    print(max)
arrBig(['nik', 'mikhil', 'Cow','Elephant'] )
            
'''
Elephant
'''

# Most Commonly Used two Character in String(can not use predefined function)

# 				Input: ‘Hii i am ram’
# Output; i, a 

def most_common_chars(s):
    s = s.replace(" ", "")  
    max1 = max2 = 0
    char1 = char2 = ''

    for char in s:
        count = s.count(char) 
        if count > max1:  
            max2, char2 = max1, char1  
            max1, char1 = count, char  
        elif count > max2 and char != char1:  
            max2, char2 = count, char  
    return char1, char2

print(most_common_chars('Hii i am ram'))





def most_common_chars(s):
    s = s.replace(" ", "")  # Remove spaces
    unique_chars = ""  # To store unique characters
    counts = []  # To store frequency of characters

    # Count occurrences of each character
    for char in s:
        if char not in unique_chars:
            unique_chars += char
            counts.append(s.count(char))

    # Find the two highest occurring characters
    first_max = second_max = 0
    first_char = second_char = ''

    for i in range(len(counts)):
        if counts[i] > first_max:  
            second_max, second_char = first_max, first_char
            first_max, first_char = counts[i], unique_chars[i]
        elif counts[i] > second_max:  
            second_max, second_char = counts[i], unique_chars[i]

    return first_char, second_char

# Example usage
s = "Hii i am ram"
result = most_common_chars(s)
print(result[0], result[1])

'''i a
'''
# 9.Write Program to remove duplicate elements in an array and sort it in descending order(can not use predefined function).

# 			Input: [5,3,5,2,1,1,7,3,5,6]
# 			Output: [7,6,5,3,2,1]

x=[5,3,5,2,1,1,7,3,5,6]
arr=[]
for i in x:
    if i not in arr:
        arr.append(i)
for i in range (len(arr)):
    for j in range (len(arr)):
        if arr[i]>arr[j]:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
      
print(arr)
            
'''
[7, 6, 5, 3, 2, 1]'''

# 10.Write a Program to Remove brackets from an algebraic expression(can not use predefined function).

# # 			Input: a + b-(9+c)=3
# # 			Output: a + b- 9+c=3

def removebrace(s):
    x=''
    for i in s:
        if i!='(' and i!=')':
            x += i
    return x

print(removebrace("a + b-(9+c)=3"))

'''
a + b-9+c=3

'''
# 11.Write Program to remove duplicate elements in an array and sort it in Accending order(can not use predefined function).

# 			Input: [Z, A, P, C, A, Z , K, N, C]
# 			Output: [A, C, K,N, P, Z]
x=['Z', 'A', 'P', 'C', 'A', 'Z' ,'K', 'N', 'C']
s=set(x)
arr=[]
# for i in x:
#     if i not in arr:
#         arr.append(i)
print(arr)
for i in range (len(arr)):
    for j in range (len(arr)):
        if ord(arr[i])< ord(arr[j]):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
   
print(arr)

'''
['A', 'C', 'K', 'N', 'P', 'Z']
'''
    
def arr_pallindrome(a):
    for i in a:
        x =""
        for j in range(len(i)-1,-1,-1):
            x+=i[j]
        
        if i==x:
            print(i)
       
       
a=["mom","madam","sir","pen"]
res=arr_pallindrome(a)



def arr_pallin(a):
    for i in a:
        if i == i[::-1]:
            print(i)

a=["mom","madam","sir","pen"]
res=arr_pallin(a)

'''
mom
madam
'''

# 13.,Find sum of the Unique numbers: 
# Example : Let arr = [1, 2, 2, 1, 3, 5, 1];
#  The unique numbers are 1,2, 3, 5 so the sum should be 11.

arr=[1, 2, 2, 1, 3, 5, 1]
unique=set(arr)
x=list(unique)
s=0
for i in x:
    s += i
print("sum:",s)

'''
sum: 11
'''
    
    
# 12.If subseq's  array  sequence is present in the array, returns true or else returns false.                                                    
# Let arr = [5, 7, 3, 2, 2, 7,-1, 5, -3, 13, 4]
# Example: 
#            Input : Subseq1 = [7, -1, 5, -3] Output:  true
#            Subseq2 = [7, -1, 4, -3]            : false
#            Subseq3 = [ -1]                        : true
#            Subseq4 = [13, -3, 4, 1]           : false


arr=[5, 7, 3, 2, 2, 7,-1, 5, -3, 13, 4]
subseq =[-1] 
def subseq_arr(x,subseq):
    c=0
    for i in range(len(subseq)):    
        if arr[x]==subseq[i]:      
            c+=1
        if x!=len(arr)-1:
            x+=1      
    return c

for i in range(len(arr)): 
    c=0
    if arr[i] == subseq[0]:
        res = subseq_arr(i,subseq)
        if (res == len(subseq)):
            c=1
            break
    
if(c):
    print("True")
else:
    print("false")
    
'''
 True
'''   





'''

LEVEL:DIFFICULTY

'''

# 1.Create a function that converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized.

# Examples :

# toCamelCase("A-B-C") ➞ "ABC"

# toCamelCase("the-stealth-warrior") ➞ "theStealthWarrior"

# toCamelCase("The_Stealth_Warrior") ➞ "TheStealthWarrior"



def toCamelCase(s):
    str=''  
    for i in s:
        if i != '-' and i!='_':
            str += i
    return('''"'''+ str+ '''"''')
print(toCamelCase("the-Stealth-Warrior"))

'''theStealthWarrior '''


#2. Create a function that takes an array of strings and returns an array with only the strings that have numbers in them. If there are no strings containing numbers, return an empty array.	

# Examples :

# numInStr(["1a", "a", "2b", "b"]) ➞ ["1a", "2b"]

# numInStr(["abc", "abc10"]) ➞ ["abc10"]

# numInStr(["abc", "ab10c", "a10bc", "bcd"]) ➞ ["ab10c", "a10bc"]

# numInStr(["this is a test", "test1"]) ➞ ["test1"]


l=[]
def numInStr(a):
    for y in a:
        i=y.replace(" ","")
        if i.isalpha():
            pass
        else:
            l.append(i)
    print(l)
    

numInStr(["this is a test", "test1"])
numInStr(["abc", "abc10"])        
numInStr(["1a", "a", "2b", "b"])
numInStr(["abc", "ab10c", "a10bc", "bcd"])        
        
'''
['ab10c', 'a10bc']
'''

# 3.Write a function that takes a list of hours and returns the total weekly salary.
# The input list hours is listed sequentially, ordered from Monday to Sunday.
# A worker earns $10 an hour for the first 8 hours.
# For every overtime hour, he earns $15.
# On weekends, the employer pays double the usual rate, regardless how many hours were worked previously that week. For instance, 10 hours worked on a weekday would pay 80+30 = $110, but on a weekend it would pay 160+60 = $220.

# Examples :
# weeklySalary([8, 8, 8, 8, 8, 0, 0]) ➞ 400
# weeklySalary([10, 10, 10, 0, 8, 0, 0]) ➞ 410
# weeklySalary([0, 0, 0, 0, 0, 12, 0]) ➞ 280

def weeklySalary(lst):
   total_sal=0
   days=0
   for hrs in lst:
       if days<5:
           if hrs>8:
               total_sal+= 8*10+(hrs-8)*15
           else:
               total_sal+=hrs*10
       else:
           if hrs>8:
                total_sal+=2*(8*10+(hrs-8)*15)
                
           else:
                total_sal+=2*(hrs*10)
       days+=1
   return total_sal

weeklySalary([8, 8, 8, 8, 8, 0, 0])
weeklySalary([10, 10, 10, 0, 8, 0, 0])
x=weeklySalary([0, 0, 0, 0, 0, 12, 0])

print(x)

'''
400
410
280
'''

# 4.Create a function which takes in an encoded string and returns an object according to the following example:
# Examples :
# parseCode("John000Doe000123") ➞ {
# firstName: "John",
# lastName: "Doe",
# id: "123"
# }
# parseCode("michael0smith004331") ➞ {
# firstName: "michael",
# lastName: "smith",
# id: "4331"
# }

# parseCode("Thomas00LEE0000043") ➞ {
# firstName: "Thomas",
# lastName: "LEE",
# id: "43"
# }

def parseCode(s):
    x=""
    x=s.split('0')
    
    lst2=[]
    for i in x:
        if i !=" " and i != '':
            lst2.append(i)
   
    print( "{firstname:",lst2[0] ,"\n" ,"lastname:",lst2[1] ,"\n","ID:",lst2[2],"}")


parseCode("John000Doe000123")
parseCode("Thomas00LEE0000043")
    
class Car:
    def __init__(self, brand):
        self.brand = brand
    def drive(self):
        print(f"{self.brand} is driving")
my_car = Car("Toyota")
my_car.drive()

    
'''automorphic number'''
n=12

def is_automorphic(n):
    s=n*n
    temp=n
    while temp>0:
        if s%10 != temp%10:
            print(n, "is not an Automorphic number")
            return 
        else:
            print(n, "is an Automorphic number")
            return 
    s //=10
    temp //=10

res=is_automorphic(n)  
        

'''automorphic in a range:'''
n=120
def is_automorphic(n):
    s=n*n
    temp=n
    while temp>0:
        if s%10 != temp%10:
           
            return False
      
        s //=10
        temp //=10
    return True


for i in range(1,n+1):
    if (is_automorphic(i)):
        print(i)


n = 1000

def is_automorphic(n):
    s = n * n
    temp = n
    while temp > 0:
        if s % 10 != temp % 10:
            return False
        s //= 10
        temp //= 10
    return True

for i in range(1, n + 1):
    if is_automorphic(i):
        print(i)

   
l=[7,51,3,4,77,84,52,43,23]
x=[]
for i in l:
    rev=int(str(i)[::-1])
    x.append(rev)
for i in range(len(x)):
    for j in range(len(x)):
        if(x[i]<x[j]):
            t=x[i]
            x[i]=x[j]
            x[j]=t
print(x)