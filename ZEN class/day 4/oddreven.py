a=[]
odd=[]
even=[]
a=input().split()
for i in a:
	if(int(i)%2==0):
		even.append(i)
	else:
		odd.append(i)
print(odd)
print(even)
	