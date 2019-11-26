l1=[10,20,10,30,20,10,60,70]
countlist=[]
valuelist=[]

for i in range(0,len(l1)):
 count=1
 for j in range(i+1,len(l1)):
  if(l1[i]==l1[j]):
   count+=1
 countlist.append(count)
 if(count>1):
   valuelist.append(l1[i])
print(countlist)
print(valuelist)
print(valuelist[2])



