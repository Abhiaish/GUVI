num=int(input("Enter the number:"))
rev=0
while(num>0):
	a=num%10
	rev=rev*10+a
	num=num//10
print("The reversed number:",rev)