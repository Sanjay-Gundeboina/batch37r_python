# list1=[1,2,3,4,5,6,7,8]
# even=[]
# for i in list1:
#     if i%2==0:
#         even.append(i)
# print(even)


# list1=[1,2,3,4,5,6,7,8]
# odd=[]
# for i in range(len(list1)):
#     if list1[i] % 2 != 0:
#         odd.append(list1[i])
# print(odd)

# list1=[1,2,3,4,5,6,7,8]
# even2=[ele for ele in list1 if ele%2==0]
# print(even2)
 
list2=[[1,2,3],[4,5,6],[7,8,9]]
# max_val=[]
# for i in list2:
#     # print(i)
#     max=i[0]
#     for j in i:        
#         if j>max:
#             max=j
#     max_val.append(max)
# print(max_val)


# list2=[[1,2,3],[4,5,6],[7,8,9]]
# max_list=[ele for sub in list2  for ele in sub if ele == max(sub)]
# print(max_list)


'''DICTIONARIES'''

# details={"p1":"sanjay","p2":"Madhu","p3":"Hemanth"}
# # new={}
# # for person in details:
# #     # print(details[i])
# #     if details[person].lower().startswith("m"):
# #         new[person]=details[person]
# # print(new)
# n2={key:details[key] for key in details if details[key][0].lower()=="m"}
# print(n2)