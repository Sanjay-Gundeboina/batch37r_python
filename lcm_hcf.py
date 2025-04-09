'''LCM'''

# n1=int(input("enter a number"))
# n2=int(input("enter a number"))
# big=max(n1,n2)
# small=min(n1,n2)
# if big%small==0:
#     print(f"{big} is LCM")
# else:
#     temp=big
#     while True:
#         if temp%big==0 and temp%small==0:
#             print(f"{temp }is the LCM")
#             break
#         temp+=big


'''HCF'''

# n1=int(input("enter a number"))
# n2=int(input("enter a number"))
# big=max(n1,n2)
# small=min(n1,n2)
# hcf=0
# if big%small==0:
#     print(f"{small} is the hcf")  
  
# else:  
#  for i in range(1,small+1):
#     if big%i==0 and small%i==0:
#         hcf=i
#         break
# print(f"{hcf} is the hcf")


'''TASK'''
'''LCM OF 3 NUMBERS'''

n1=int(input("enter a number"))
n2=int(input("enter a number"))
n3=int(input("enter a number"))
lst=[]
lst.append(n1)
lst.append(n2)
lst.append(n3)
lst.sort()
small=lst[0]
mid=lst[1]
big=lst[2]
if big%small and big%mid ==0:
    print(f"{big} is LCM")
else:
    temp=big
    while True:
        if temp%big==0 and temp%small==0 and temp%mid==0:
            print(f"{temp }is the LCM")
            break
        temp+=big

