string = input(" enter  String : ")
char = input("enter  Character : ")
i = 0

while(i < len(string)):
    if(string[i] == char):
	 string.replace(i,"")
        break
    i = i + 1
print(string)

