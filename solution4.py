# Write code for algorithm 4 below
# Write a function that calculates the value of 'a' to the power of 'b'.
import math


# def power(a,b):
#     if b == 0:
#         return 1
#     elif b == 1:
#         return a
#     else:
#         return(a*power(a, b-1))

# n = 6 
# p = 10
# print(power(n, p))

# def power(a,b):
#     res=0
#     for i in range(b):
#         res*=a
#     return res
# print(pow(4,2))

def power(a,b):
    print(math.pow(a,b))

power(4,2)



