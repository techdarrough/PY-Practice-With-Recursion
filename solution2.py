# Write code for algorithm 2 below
# Write a function that prints the natural numbers from 1 to n.
def naturalNumbers(number):
    for i in range(1, number + 1):
        print(i)

number =int(input("Enter any number: "))
print(" The natural numbers from 1 to {0} are:".format(number))
naturalNumbers(number)
