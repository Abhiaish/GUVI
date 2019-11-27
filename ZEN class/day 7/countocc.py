string = input(" enter  String : ")
char = input("enter  Character : ")
i = 0
count=0

while(i < len(string)):
 if(string[i] == char):
  count=count+1
 i=i+1
print("The count of ", char, "is" , count)