
string = input(" enter  String : ")
char = input("enter  Character : ")
i = 0
flag = 0
list=[]

while(i < len(string)):
 if(string[i] == char):
  list.append(i)
 i = i + 1
print("The all occurrence of ", char, " is at Position " , list)