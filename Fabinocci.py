#program on fabinocci series
a=0
b=1
temp=0
num=int(input("Enter the number"))
print(a)
print(b)
for i in range(2,num):
    temp=a+b
    a=b
    b=temp
    print(temp)
