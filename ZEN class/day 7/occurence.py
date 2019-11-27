
string = input(" enter  String : ")
char = input("enter  Character : ")
i = 0
list=[]

while(i < len(string)):
 if(string[i] == char):
  a=i+1
  list.append(a)
 i = i + 1
print("The all occurrence of ", char, " is at Position " , list)