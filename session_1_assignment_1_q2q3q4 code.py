# -*- coding: utf-8 -*-
"""
-Session 1
-Assignment ONE
"""

##assignmnet 1 question 2
print("*/ assignment 1 output 2/*")
#defining function for finding elements divisible by 7 but not by 5
def divby7notby5(x,y):
    print("values divisible by 7 not by 5 between %d and %d are \n" %(x,y))
    for i in range(x,y+1):
        if i%7==0:
            if i%5!=0:
                print(i,end=",")
divby7notby5(2000,3200)
print('\n')
print("-"*100)


"""
-Session 1
-Assignment ONE
"""
                
#assignmnet 1 question 3
print("*/ assignment 1 output 3/*")
#asking user for inputs
f_name=input("your first name please: ")
l_name=input("your last name please: ")
print("in reverse order:",l_name," ",f_name)
print("-"*100)
print('\n')
"""
-Session 1
-Assignment ONE
"""

#assignmnet 1 question 4
print("*/ assignment 1 output 4/*")
import math
#defining function for caluculation of volume of sphere
def volofsphere(D):
    print("diameter of sphere: %d" %D)
    Volume=(4/3)*math.pi*(D/2)*(D/2)*(D/2)
    return round(Volume,2)
volofsphere(12)
print("Volume of sphere is %f --rounded off to two digits" %(volofsphere(12)))
print("-"*100)
print('\n')
print("End of assignment")

