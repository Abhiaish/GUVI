n=int(input())
count=0
lastdigit=n%10
while(n>=10):
	firstdigit=n//10
	n=n//10
	print(lastdigit)
	print(firstdigit)
	
