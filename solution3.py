# Write code for algorithm 3 below
# Write a function that returns the nth elements in the Fibonacci Sequence.


# def fib(n):

#     if n <= 1:
#         return n
#     return fib(n -1) + fib(n-2)

def fib(n, lookup):
    if n <= 1:
        return n
    #First time subproblem is seen
    if n not in lookup:
        lookup[n] = fib(n-1, lookup) + fib(n-2, lookup)
    return lookup[n]    

if __name__ == '__main__':
    # n = 8
    # print('Fibonacci nth element is: F(n)=', fib(n))
    n = 8 
    lookup = {}

    print("F(n)=", fib(n, lookup))

    # credit to https://www.techiedelight.com/program-to-find-nth-fibonacci-number/