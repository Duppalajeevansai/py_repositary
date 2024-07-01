n=int(input())
sum=0
temp=n
while temp>0:
    stote=temp%10
    sum+=stote**3
    temp//=10
if n==sum:
    print(n," is a Armstrong number")
else:
    print(n," is not a Armstrong number")
