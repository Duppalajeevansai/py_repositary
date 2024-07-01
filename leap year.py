#program to check wheather the following year is a leap year or not
year=int(input())
if(year%4==0):
    print("{0} is a leap year".format(year))
    if(year%100==0):
        print("{0} is a not leap year".format(year))
        if(year%400==0):
            print("{0} is a leap year".format(year))
        else:
            print("{0} is a leap year".format(year))      
else:
    print("{0} is a not leap year".format(year))
    
        
