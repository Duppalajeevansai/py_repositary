#program to check wheather the string is palendrome or not
s=str(input("Enter the string : "))
c=s[::-1]
if(c==s):
    print("{0} is palendrome".format(s))
else:
    print("{0} is not palendrome".format(s))
