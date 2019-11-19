print("Enter the values:")
a=int(input())
b=int(input())
c=int(input())
if(a>=b):
	if(a>=c):
		print("a is greatest")
	else:
		print("c is greatest")
else:
	if(b>=a):
		if(b>=c):
			print("b is greatest")
		else:
			print("c is greatest")