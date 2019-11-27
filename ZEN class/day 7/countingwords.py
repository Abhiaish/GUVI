
## Program to count number of word 

string = "python of guvi is very interesting.so we are going to learn python immediately as python is a very important language"
word = input("Enter the word to be counted: ")
a = string.split()
count = 0
for i in range(0,len(a)):
 if(word==a[i]):
  count += 1
print("The number of times, the word",word,"has occured is: ",count)

## Program to capitalize the alphabet after '.'

b = string.split('.')
for i in range(len(b)):
 b[i]=b[i].capitalize()
print(b)
Position:	Ln 17, Ch 9	Total:	Ln 17, Ch 479	
