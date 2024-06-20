#input a list sort the list according to its length
l1=input("enter the list : ").split()    
l1.sort(key=len)
print(l1)
