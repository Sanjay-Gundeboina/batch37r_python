'''1. Write a program to print the sum of the digits in the number.  
Testcase1 : 101  
Output : 2  
Explanation : Sum of the digits in the number 1+0+1 = 2, Answer is 2.  
'''

# num=int(input("enter a number"))
# sum=0
# while num>0:
#     r=num%10
#     sum+=r
#     num=num//10
# print(sum)

'''2. Write a program to print reverse of the given number.  
Testcase1 : 721  
Output : 127  
Explanation : Reverse of the number 721 is 127.
'''

# num=int(input("Enter a number"))
# t=num
# rev=0
# while num!=0:
#     r=num%10
#     rev=rev*10+r
#     num//=10
# print(f"reverse of the number {t} is {rev}")

'''3. Write a program to print factorial of the number.  
Testcase1 : 3  
Output : 6  
Explanation : Factorial of the number 3 is 3*2*1 = 6.  
'''
# num=int(input("enter a number"))
# fact=1
# for i in range(1,num+1):
#     fact*=i
# print(f"factorial of the number {num} is {fact}")

'''4. Write a program to print middle character(s) in the given string or 
number.  
Testcase1 : Wonder  
Output : nd  
Explanation : The middle characters in the given word Wonder is nd.  

'''
# str1=input("enter a string")
# x=len(str1)//2
# print(x)
# if len(str1)%2==0:
#    print(str1[x-1]+str1[x])
# else:
#     print(str1[x])

'''5. Write a program to check whether the sum of digits in the number except  
first digit and digit is equal to the sum of first digit and last digit of that  number. If both the sums are equal then print equal otherwise print not  equal  
Testcase1 : 75547  
Output : equal  
Explanation : In the given number 7557, first digit and last digit sum  that is sum(7,7)=14 is equal to sum of remaining numbers that is  sum(5,5,4) = 14. So both sums are equal.  
Testcase1 : 765  
Output : not equal  
Explanation : Sum(7,5)=12 and Sum(6)=6, both sums are not equal.  
'''
# num = input("Enter a number")
# digit=[]
# first_last_sum=0
# middle_sum=0
# for i in num:
#     digit.append(int(i))
# first_last_sum=digit[0]+digit[-1]
# middle_sum = sum(digit[1:-1]
# if(first_last_sum==middle_sum):
#     print("Equal")
# else:
#     print("not equal")

'''6.Write a program to check whether the digits in-between the first and last   
digit are less than first and last digit, if yes then print true, otherwise print  
false.   
Testcase1 : 1672   
Output : false 
Explanation : The middle digits 6,7 are not less than first digit 1 and  
last digit 7 .   '''

# num=input("enter a number")
# digit=[]
# for i in num:
#     digit.append(i)
# first_dig=digit[0]
# last_dig=digit[-1]
# for x in range(1,len(digit)-1):
#     middle_dig=digit[x]
#     if middle_dig<first_dig or middle_dig<last_dig:
#         print("True")
#         break
#     elif middle_dig>first_dig or middle_dig>last_dig:
#         print("False")
#         break

'''7. Write a program to print the vowels in the given string in reverse order.   
Testcase1 : Helloworld   
Output : ooe   
Explanation : Vowels in the given string Helloworld are e,o,o . The  
reverse order of eoo is ooe'''

# str1=" JackspArrow"
# vowels="aeiouAEIOU"
# v=""
# for i in str1:
#     if i in vowels:
#         v+=i
# print(v)        
# print(v[::-1])

'''8. Write a program to print the vowels in the given string and repeated  
vowel should be printed only single time.   
Testcase1 : Helloworld   
Output : eo   
Explanation : Vowels in the given string Helloworld are e,o,o . The  
single vowels among them are eo .  '''

# str2="Jacksparrow"
# vowels="AEIOUaeiou"
# v=""
# for i in str2:
#     if i in vowels and i not in v:
#         v+=i
# print(v)

'''9.  Write a program to print the string after removing the duplicate characters  
in the string.   
Testcase1 : madam   
Output : d   
Explanation : In the given string madam, the duplicates are m,a. After  
removing m’s and a’s from the given string we formed a new string d. '''

# str3="maduam"
# dup=""
# unq=""
# for i in str3:
#     if i not in unq:
#         unq+=i
# for i in str3:
#     c=0
#     for j in str3:
#         # print(i,j)
#         if i==j:
#             c+=1
#     if c==1:
#         dup+=i        
# print(dup)

'''10. Write a program to convert all the upper case letters in the given string to  
lower case letter and vice versa.   
Testcase1 : JohnWick   
Output : jOHNwICK   
Explanation : All the upper case letters changed to lower case and vise  
versa.   '''

# str3=input("enter a string:")
# str4=""
# for i in str3:
#     if i==i.upper():
#        str4+=i.lower()
#     else:
#         str4+=i.upper()
# print(str4)

'''11. Write a program to print all the Upper case letters in the string in reverse  
order and then followed by the lower case letters .   
Testcase1 : NumberOne   
Output : ONumberne   
Explanation : In the given string NumberOne, Uppercase letters are N,O.  
The reverse order of them are ON next it is followed by lowe case letters  
(umberne). So final string is ONumberne.'''

# ip_str=input("enter a string")
# up_str=""
# lp_str=""
# op_str=""
# for i in ip_str:
#     if i== i.upper():
#         up_str+=i
#     else:
#         lp_str+=i
# op_str=up_str[::-1]+lp_str
# print(op_str.strip())

'''12.Find the Largest Element in an Array  
Problem: Write a function to return the largest number in an array.  
Testcase 1:  
Input: [3, 1, 4, 1, 5, 9]  
Output: 9  
Explanation:  
In the array [3, 1, 4, 1, 5, 9], the largest number is 9. '''

lst1 = [3, 1, 4,11, 1, 5, 9]
# lst1.sort()
# print(lst1[-1])

 # or
 
# max=lst1[0]
# for i in lst1:
#     if i>max:
#         max=i
# print(max)

'''13. Find the Second Largest Element  
Problem: Write a function to return the second largest number in an array.  
Testcase 1:  
Input: [3, 1, 4, 1, 5, 9]  
Output: 5  
Explanation:  
In the array [3, 1, 4, 1, 5, 9], the second largest number after 9 is 5. '''

# list2=[3, 1, 4, 1, 5, 9]
# list2.sort()
# print(list2[-2])

# or

# first_max=list2[0]
# second_max=list2[1]
# for i in list2:
#     if i> first_max and second_max:
#         second_max=first_max
#         first_max=i
        
#     elif i<first_max and i>second_max:
#         second_max=i
# print(second_max)

'''13.  Sum of All Elements  
Problem: Write a function that returns the sum of all elements in an array.  
Testcase 1:  
Input: [1, 2, 3, 4]  
Output: 10 
Explanation:  
The sum of the elements 1 + 2 + 3 + 4 = 10. '''

# list3 = [1, 2, 3, 4] 
# sum=0
# for i in list3:
#     sum+=i
# print(sum)

'''14.Remove Duplicates from an Array  
Problem: Write a function to remove duplicate values from an array.  
Testcase 1:  
Input: [1, 2, 2, 3, 4, 4, 5]  
Output: [1, 2, 3, 4, 5]  '''

# list4 = [1, 2, 2, 3, 4, 4, 5]  
# unq_list=[]
# for i in list4:
#     if i not in unq_list:
#         unq_list.append(i)
# print(unq_list)

'''15. Check if Array is Sorted  
Problem: Write a function to check if an array is sorted in ascending  
order.   
Testcase 1:  
Input: [1, 2, 3, 4, 5]  
Output: true  
Explanation:  
The array [8,7,1, ,2, 3, 4, 5] is sorted in ascending order. '''
    
# def is_sorted(lst):
#     for i in range(len(lst) - 1):
#         if lst[i] > lst[i + 1]:
#             return False
#     return True

# input_arr = [2,3,4,5]
# output = is_sorted(input_arr)
# print(output)

'''16.  Reverse an Array  
Problem: Write a function to reverse the elements in an array.  
Testcase 1:  
Input: [1, 2, 3, 4, 5]  
Output: [5, 4, 3, 2, 1]  
Explanation:  
The array [1, 2, 3, 4, 5] is reversed to [5, 4, 3, 2, 1]. 
'''
# lst4= [1, 2, 3, 4, 5]  
# print(lst4[::-1])


'''17. Remove Falsy Values  
Problem: Write a function that removes all falsy values from an array.  
Falsy values include false, 0, "", null, undefined, and NaN.  
Testcase 1:  
Input: [0, 1, false, 2, ', 3]  
Output: [1, 2, 3]  
Explanation:  
The falsy values 0, false, and "" are removed from the array, leaving  [1, 
2, 3]. '''

# ip_lst=[0, 1, False, 2,'',3] 
# falsy_lst=[False,0,'','null', 'undefined','NaN']
# op_lst=[]
# for i in ip_lst:
#     if i not in falsy_lst:
#         op_lst.append(i)
# print(op_lst)

'''18. Find Unique Elements  
Problem: Write a function to find the unique elements in an array  
(elements that appear only once).  
Testcase 1:  
Input: [1, 2, 2, 3, 4, 4, 5]  
Output: [1, 3, 5]  
Explanation:  
The unique elements that appear only once in the array are 1, 3, and 5. '''

# lst=[1, 2, 2, 3, 4, 4, 5]  
# unq_list=[]
# for i in lst:
#     c=0
#     for j in lst:
#         if i==j:
#             c+=1
#     if c==1:
#         unq_list.append(i)
# print(unq_list)

'''19. Sum of Even Numbers  
Problem: Write a function that returns the sum of all even numbers in an  
array.  
Testcase 1:  
Input: [1, 2, 3, 4, 5]  
Output: 6  
Explanation: 
The even numbers in the array are 2 and 4. Their sum is 2  '''

# l=[1, 2, 3, 4, 5]
# even_sum=0
# for i in l:
#     if i%2==0:
#         even_sum+=i  
# print(even_sum)

'''20.  Reverse a String :  
Question: Write a function to reverse a given string. 
Testcase: "hello" 
Output: "olleh" 
Explanation: The reverse of the string "hello" is "olleh". Each character's 
order is reversed. 
'''
# str1="sanju"
# print(str1[::-1])
 
# 0r

# str1="hello"
# rev=""
# for i in str1:
#     rev=i+rev
# print(rev)


'''
21. Check if a String is a Palindrome 
Question: Write a function to check if a given string is a palindrome. 
Testcase: "racecar" 
Output: true 
Explanation: A palindrome is a string that reads the same forward and 
backward. Since "racecar" is the same in both directions, the output is 
true.'''

# def is_pallin(str1):
#     x=str1
#     rev=str1[::-1]
#     if x==rev:
#         return True    
#     else:
#         return False
# print(is_pallin("racear"))

'''22. Count Vowels in a String 
Question: Write a function to count the number of vowels in a given 
string. 
Testcase: "hello world" 
Output: 3 
Explanation: The vowels in "hello world" are 'e', 'o', and 'o'. Thus, the total 
count of vowels is 3. 
'''
# str1="hello world"
# v_c=0
# vowels="AEIOUaeiou"
# for i in str1:
#     if i in vowels:
#         v_c+=1
# print(v_c)


'''
23. Remove Vowels from a String 
Question: Write a function to remove all vowels from a given string. 
Testcase: "hello world" 
Output: "hll wrld" 
Explanation: After removing the vowels 'e', 'o', and 'o' from "hello world", 
we are left with "hll wrld".'''

# str1="hello world"
# str2=""
# vowels="AEIOUaeiou"
# for i in str1:
#     if i not in vowels:
#         str2+=i
# print(str2)

'''24. Convert String to Title Case 
Question: Write a function that converts a string to title case (capitalize 
the first letter of each word). 
Testcase: "hello world" 
Output: "Hello World" 
Explanation: The first letter of each word is capitalized, resulting in "Hello 
World". '''

# str2 = "hello world" 
# str3=""
# x = str2.split(" ")
# for i in x:
#     for j in range(len(i)):
#         print(j)
#         if j==0:
#             str3+=i[0].upper()
#         else:
#             str3+=j
# print(str3)


'''
25. Convert String to Number 
Question: Write a function to convert a string to a number (without using 
parseInt or Number). 
Testcase: "123" 
Output: 123 
Explanation: The string "123" is converted to the number 123.'''

'''
26. Check if String Contains Only Digits 
Question: Write a function to check if a string contains only numeric 
digits. 
Testcase: "12345" 
Output: true 
Explanation: The string "12345" consists only of digits, so the result is 
true. '''

# def id_str_dig(str1):
#     for i in str1:
#         if i<'0' or i>'9':
#             return False
#     return True

# print(id_str_dig("12345"))

'''27. Count Occurrences of a Character 
Question: Write a function that counts the occurrences of a specific 
character in a string. 
Testcase: "hello world", "l" 
Output: 3 
Explanation: The character 'l' appears 3 times in the string "hello world".'''

# s1="hello world"
# print(s1.count("l"))

# s1="hello world"
# chr=input("enter char")
# c=0
# for i in s1:
#     if i==chr:
#         c+=1
# print(c)
