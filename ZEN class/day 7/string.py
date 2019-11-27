#name="GuviGeek"
#list=[name]
#list=name.upper()
#print(list)


names=["Arun","Aksara","Devi","Ajay"]
sex=["M","F","F","M"]
status=["M","S","M","S"]
for i in range(0,len(sex)):
	if sex[i] == "M":
		print("Mr."+names[i])
	else:
		if(status[i] == "M"):
			print("Mrs."+names[i])
		else:
			print("Ms."+names[i])
print(names[:])