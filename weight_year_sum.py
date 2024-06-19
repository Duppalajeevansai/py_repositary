#two brothers and there weight are a and b a is 3 times in year and b is 2 times at how many years that the a will be greater than b
a=int(input("Enter a's weight : "))
b=int(input("Enter b's weight : "))
count=0
while(a<b):
    a+=3
    b+=2
    count+=1
print(count)
