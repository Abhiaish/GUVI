#Removing leading spaces without using in-built function
n="hi   "
n=list(n)
print(n)
for i in range(len(n)-1,-1,-1):
	if(n[i]==' '):
		n.pop(i)
		
print(n)