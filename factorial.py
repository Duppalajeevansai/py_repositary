#program for the factorial
n=int(input())
factorial=1
if(n==0):
    print("{0} cannot be factored".format(n))
else:
    for i in range(1,n+1):
        factorial*=i
print(factorial)
