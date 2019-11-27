string = input(" enter  String : ")
char = input("enter  Character : ")
i = 0


while(i < len(string)):
    if(string[i] == char):
        break
    i = i + 1
a=string.replace("char","*")
print(a)