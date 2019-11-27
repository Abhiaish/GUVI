
string = input(" enter  String : ")
char = input("enter  Character : ")
i = 0
flag = 0

while(i < len(string)):
    if(string[i] == char):
        flag = 1
        break
    i = i + 1

if(flag == 0):
    print("Sorry!")
else:
    print("The first Occurrence of ", char, " is at Position " , i + 1)