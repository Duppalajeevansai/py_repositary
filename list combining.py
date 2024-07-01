l1=[10,"Jeevan"]
l2=["sai",20,"Hasini"]
print(l1+l2)

#3d method iterible operation
result=*l1,*l2
print(result)

#4th method
fourth=l1+l2
print(fourth)

#2nd opeartion
l1.extend(l2)
print(l1)
