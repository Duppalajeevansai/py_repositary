l1=list(map(int,input("Enter the elements : ").split()))
dum=l1[-1]
l1[-1]=l1[0]
l1[0]=dum
print(l1)
