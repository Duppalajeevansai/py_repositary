#longest substring without repeatation need the sting and the count
n=str(input("Enter the string : "))
b=[]
for i in n:
    if i in b:
        pass
    else:
        b.append(i)
print("{0} and count is {1}".format(b,len(b)))
