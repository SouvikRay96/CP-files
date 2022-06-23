"""CRICKET RATINGS"""

n = int(input()) # Enter number of cricket matches
if n == 0: # If n = 0 then the maximum consistent sum of rating will be 0
    print("0")
else:
    # Else enter the ratings of the batsman/bowler in those n matches
    ratings = list(map(int,input().split()))
    # considering two variables 
    rating_sum1 = 0
    rating_sum2 = 0
    for i in range(n):
        rating_sum1 += ratings[i]
        if rating_sum2 < rating_sum1:
            rating_sum2 = rating_sum1
        if rating_sum1 < 0:
            rating_sum1 = 0
    # Printing the maximum consistent and continuos sum of the ratings of the cricketer
    print(rating_sum2)