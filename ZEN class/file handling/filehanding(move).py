import os
#moving files from one dir to another
source=r'C:\Users\Abhinaya\Desktop\source'
destination=r'C:\Users\Abhinaya\Desktop\destination'
files=os.listdir(source)
for f in files:
	print(f)
	file=open(source+'\\'+f,'rb')
	var1=file.read()
	file.close()
	file=os.remove(source+'\\'+f)
	
	