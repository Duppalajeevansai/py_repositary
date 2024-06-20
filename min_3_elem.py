#sum of min three elements in the list
l1=list(map(int,input("Enter the Elements : ").split()))
l2=0
for i in range(l1[0],l1[-1]):
    min_value=min(l1)
    container=min_value
    l3=l2-min_value
con1=l1[0:3]
print(sum(con1))
