list1=input().split()
list2=[0]*len(list1)
list3=[]
for i in range(0,len(list1)):
    for j in range(i+1,len(list1)):
        if(list1[i]==list1[j]):
            list2[i]+=1
for i in range(0,len(list2)):
    if(list2[i]==0):
        list3.append(list1[i])
print(list3)