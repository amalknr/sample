import random
die_roll = random.randint(1,6)
#find the area of a triangle whose base and hight is given 1/2*bh
#find the area of the triangle whose three sides are given
#s=a+b+c/2
#area=sq(s*s-a*s-c)
#find the area of the equilateral triangle
#sqrt(3)/2*a*a
import math;
a=int(input("enter side : "))
area = math.sqrt(3)/4 * (a*a)
print("area of the triangle is : ",area)