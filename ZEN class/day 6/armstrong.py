#printing armstrong numbers
num = int(input())
for num in range(1, 500):
   order = len(str(num))
    
   sum = 0
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10
   if num == sum:
       print(num)
	   
	  
#checking armstrong or notq
num = int(input("Enter a number: "))

sum = 0

temp = num

while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")