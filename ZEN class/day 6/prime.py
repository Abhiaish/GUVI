num = int(input("enter the number:"))
 
if num > 1: 
   for i in range(2, num//2):   
       if (num % i) == 0: 
           print(num, "is not a prime number") 
           break
   else: 
       print(num, "is a prime number") 
  
else: 
   print(num, "is not a prime number")

x=num
print("The factors of ",x,"are:")
for i in range(1,x+1):
	if(x%i == 0):
		print(i)

print(num)