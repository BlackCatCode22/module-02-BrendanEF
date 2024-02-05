# User input
def largest_integer(integer1, integer2, integer3):
    if integer1 > integer2 and integer1 > integer3:
        largest = integer1
    elif integer2 > integer1 and integer2 > integer3:
        largest = integer2
    else:
        largest = integer3
    return largest

# User input error
try:
    integer1 = int(input("First integer: "))
    integer2 = int(input("Second integer: "))
    integer3 = int(input("Third integer: "))
except:
    print("Error, please enter numeric input without a decimal")
    quit()

largest = largest_integer(integer1, integer2, integer3)

# Output
print("The largest of the three integers is", largest)