n=int(input())
temp=n
temp2=n
count=0
lastdigit=n%10
while(temp!=0):
 temp=temp//10
 count+=1 
while(temp2>=10):
 firstdigit=temp2//10
 temp2=temp2//10
digits=count-1
swap=lastdigit*10**digits
print(swap)
swap=swap+ n%10**digits
swap=swap-lastdigit
swap=swap+firstdigit
print(swap)