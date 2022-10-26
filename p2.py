import random
die_roll = random.randint(1,6)
#find the area of a triangle whose base and hight is given 1/2*bh
#find the area of the triangle whose three sides are given
#s=a+b+c/2
#area=sqrt(s*s-a*s-c)
#find the area of the equilateral triangle
#sqrt(3)/4*(a*a)
import math;
a=int(input("enter side : "))
b=int(input("enter side : "))
c=int(input("enter side : "))
s=a+b+c/2
area=math.sqrt(s*(s-a)*(s-c))
print("area of the triangle is : ",area)