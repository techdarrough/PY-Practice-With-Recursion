# Write code for algorithm 5 below
# Write a function that checks whether a string is a palindrome or not. The program should take in a string and return True if the string is a palindrome and False if not.
def palindromeCheck(s):
    # flipp string and store in var
    rev = ''.join(reversed(s))
    #compare values and return
    if s == rev:
        return True
    return False

print(palindromeCheck('not'))
print(palindromeCheck('madam'))