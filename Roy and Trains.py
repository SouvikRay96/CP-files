import math
"""ROY AND TRAINS"""

test_cases = int(input()) # Enter the test cases
result = list() # A list created to store the result/output of all the test cases
for i in range(test_cases):
    details = list(map(int,input().split())) # Taking the details
    count = 0
    t0,t1,t2,v1,v2,d = details[0],details[1],details[2],details[3],details[4],details[5]
    # t0 = Time taken by Roy to reach the station of city A
    # Train 1 will depart in time t1 from city A
    # Train 2 will depart in time t2 from city A
    # v1 = Velocity/Speed of train 1
    # v2 = Velocity/Speed of train 2
    # d = Distance between the two cities A and B
    train_1 = t1 + int(math.ceil((d/v1)*60)) 
    # train_1 = Total Time taken by Roy to reach city B if he catches the first train from city A
    train_2 = t2 + int(math.ceil((d/v2)*60))
    # train_2 = Total Time taken by Roy to reach city B if he catches the second train from city A
    if t0 > t1 and t0 > t2:
        # if Roy fails to reach the station of city A before the time the two trains will depart
        # then he fails to catch both the trains and it's impossible for him to reach city B
        # So append -1 as given in the problem statement
        result.append(-1)
    else:
        if t0 > t2:
            # if Roy fails to recah the station in time the train 2 departs then he has the only option
            # i.e. To catch train 1
            result.append(train_1)
        elif t0 > t1:
            # if Roy fails to raech the station in time the train 1 departs then he has only one option
            # i.e. to catch train 2
            result.append(train_2)
        else:
            # If Roy reaches the station in time and two trains have not been departed yet
            # then he can choose the train which will take less time to reach city B
            result.append(min(train_1,train_2))
    
# Printing the results of the entered test cases
for i in result:
    print(i)