#deleting the duplicate elements in the list
l1=list(map(int,input("Enter the elements : ").split()))
print("Before removing the duplicates : ",l1)
l2=set(l1)
print("After removing the duplicates : ",l2)
