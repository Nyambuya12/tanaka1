n=int(input("Enter the average height of ten people: "))
a=[]
for i in range(0,10):
    height=int(input("Enter height: "))
    a.append(height)
avg=sum(a)/n
print("Average height 0f 10 people is",round(avg,2))
