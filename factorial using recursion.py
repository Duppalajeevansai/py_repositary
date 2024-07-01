def cal(x):
    global factorial
    if x == 0:
        print("{0} has no factorial".format(x))
    else:
        factorial *= x
        cal(x - 1)

n = int(input("Enter a number: "))
factorial = 1
cal(n)
print("Factorial of {0} is {1}".format(n, factorial))
