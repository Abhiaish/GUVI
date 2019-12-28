import os
#copying files from one dir to another
source=r'C:\Users\Abhinaya\Desktop\source'
destination=r'C:\Users\Abhinaya\Desktop\destination'
files=os.listdir(source)
for f in files:
	print(f)
	file=open(source+'\\'+f,'rb')
	var1=file.read()
	file.close()
	Newfile=open(destination+'\\'+f,'wb')
	Newfile.write(var1)
	Newfile.close()
)
	