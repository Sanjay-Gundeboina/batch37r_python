# list1=[[1,2,3],[4,6,7],[8,2,9]]
# list2=[]
# for i in range(len(list1)):
#     # print(list1[i])
#     for j in range(len(list1[i])):
#         list2.append(list1[i][j])
# print(list2)


# list1=[[1,2,3],[4,6,7],[8,2,9]]
# list2=[]
# for i in list1:
#     for j in i:
#         list2.append(j)
# print(list2)


'''TASK --> minimum and maximum values in a sub list'''

list1=[[1,2,3],[4,6,7],[8,2,9]]
max_v=[]
min_v=[]
for i in list1:
    x = max(i)
    y = min(i)
    max_v.append(x)
    min_v.append(y)
    
print("max values in a list : ", max_v)
print("min values in a list : " ,min_v)


'''Method-2'''
list1=[[1,2,3],[4,6,7],[8,2,9]]
max_v=[]
min_v=[]
for i in list1:
    i.sort()
    max_v.append(i[-1])
    min_v.append(i[0])
print(max_v,min_v)
