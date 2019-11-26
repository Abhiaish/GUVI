num=int(input("Enter the number:"))
mul=1
while(num>0):
	a=num%10
	mul=mul*a
	num=num//10
print(" mul number:",mul)