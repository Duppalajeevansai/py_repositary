#code to get the grades of the students
marks=int(input("Enter the marks :"))
if(marks>84):
    print("Scored A+ Grade")
elif(marks>60 and marks<84):
    print("Scored B Grade")
else:
    if(marks<60 and marks>30):
        print("Scored C Grade")
    else:
        print("Fail")
