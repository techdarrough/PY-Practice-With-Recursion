# Write code for algorithm 2 below
# Write a function that prints the natural numbers from 1 to n.
def natural_numbers(x,i=1):
	#base case
  if i > x:
    return
  #recursive case
  else:
    print(i)
    natural_numbers(x,i+1)




def naturalNumbers(number):
    for i in range(1, number + 1):
        print(i)

number =int(input("Enter any number: "))
print(" The natural numbers from 1 to {0} are:".format(number))
naturalNumbers(number)
natural_numbers(number)
