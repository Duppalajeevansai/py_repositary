#solve the quadratic equations:
import cmath
a=1
b=2
c=3
d=(b**2)-(4*a*c)
#substituting the d into the quadratic equation
sum1= (-b-cmath.sqrt(d))/(2*a)
sum2= (-b+cmath.sqrt(d))/(2*a)
print("Quadratic equation is {0} and {1}".format(sum1,sum2))
