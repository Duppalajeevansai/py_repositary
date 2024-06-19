#codde of a elephant to his friend house for 1 step 1,2,3,4 and 5 are the steps
n=int(input("enter the friend's house : "))
if(n<=5):
    print(int(1))
elif(n%5==0):
    print(int(n/5))
else:
    print(int((n/5)+1))
      
