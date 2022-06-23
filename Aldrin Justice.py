import math
"""ALDRIN JUSTICE"""
test_cases = int(input()) # Inserting the test cases
result = list() # Creating a list of results
while test_cases != 0: # Running a Loop for t test cases
    bt1,bt2,mt1,mt2 = map(int,input().split())
    # bt1 and bt2 are the two points to draw a line representing the given time slot of Barney
    # mt1 and mt2 are the two points to draw a line representing the given time slot of Marshall
    # Since it is given that It is NOT necessary that bt1 <= bt2 and mt1 <= mt2
    # So the below two if else blocks are executed
    if bt1 <= bt2:
        # if the condition is satisfied then create a list of numbers barney in the interval bt1-bt2 inclusive
        barney = [i for i in range(bt1,bt2 + 1)]
    else:
        # Else swap the values of bt1 and bt2 ,
        # Swapping done so as to orient the values of upper and lower limit to bt2 and bt1 respectively
        # Then create the list barney in the interval bt1-bt2 inclusive
        bt1,bt2 = bt2,bt1
        barney = [i for i in range(bt1,bt2 + 1)]
    if mt1 <= mt2:
        # if the condition is satisfied then create a list of numbers marshall in the interval bt1-bt2 inclusive
        marshall = [i for i in range(mt1,mt2 + 1)]
    else:
        # Else swap the values of mt1 and mt2 ,
        # Swapping done so as to orient the values of upper and lower limit to mt2 and mt1 respectively
        # Then create the list marshall in the interval mt1-mt2 inclusive
        mt1,mt2 = mt2,mt1
        marshall = [i for i in range(mt1,mt2 + 1)]
    # Condition to check if the given lines are indistinguishable or not
    if (bt1 in marshall or bt2 in marshall) or (mt1 in barney or mt2 in barney):
        if bt2 == mt1:
            # If the lines are indistinguishable then check they intersect each other at one point or not
            # If it is then append Point to the result list that means,,,,
            # The two lines representing the time slots of Barney and Marshall intersect at only one point
            result.append("Point")
        else:
            # Else append Nothing to the result list that means,,,,
            # The two lines representing the time slots of Barney and Marshall are indistinguishable
            result.append("Nothing")
    # If the lines are not indistinguishable then check 
    # If there exists a timeline (more than one day) in which none of them have the opportunity to slap
    elif math.fabs(bt2-mt1) >= 1:
        # If it is then append Line to the result list
        result.append("Line")
    test_cases -= 1 # Decrementing the test cases by one to run the loop

# Printing the result of the test cases entered
for i in result:
    print(i)

