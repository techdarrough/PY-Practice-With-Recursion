# Write code for algorithm 1 below
# 1.  Write a program that takes a positive number as an argument and prints the numbers from n to zero.
def count_down(n):
    if n==0:
        return 1
    else:
        print(n)
        count_down(n-1)


def countDown(t):

    while t > 0:
        print(t)
        t -= 1
count_down(3)
countDown(5)
