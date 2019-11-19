distance=int(input("enter the distance"))
peaktime=int(input("enter the peaktime"))
if(distance>5):
	distance=distance-5
else:
	print("fare is 100")
fare=int(distance*8+100)

if(peaktime==1):
	fare=fare+0.25*fare
print(fare)
