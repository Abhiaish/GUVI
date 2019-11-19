print("student 1 marks:")
a=int(input())
b=int(input())
c=int(input())

average=((a+b+c)/3)
print("average",float(average))
if average<60:
	print("sorry,got rejected!")
if average>60:
	print("the grade is A")
if average>=80 and average<100:
	print("your clg is IIT")
if average>=70 and average<80:
	print("your clg is PSG")
if average>=60 and average<70:
	print("your clg is SRM")
