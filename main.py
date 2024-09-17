#imports a series of keyboard functions that allow various code to run
import keyboard


#This function prints one number from the fibonacci sequence
def fib(n,prime):
    if n == 1:
        var = 1
    elif n == 2:
        var = 1
    else:
        var = fib(n-1) + fib(n-2)

    if prime == True:
        if isprime(var) == True:
            return var
        else:
            return False
    else:
        return var



#This function prints a list of all the numbers of the fibonacci sequence up to a certain number
def fiblist(n,prime):
    lst = []
    for i in range(n-1):
        curr = fib(i, prime)
        if not curr:
            continue
        lst.append(curr)
    return lst

#This function prints and infinite sequence of the fib sequence unless x is pressed
def inflist(prime):
    counter = 1
    while True:
        x = fib(counter,prime)
        counter += 1
        if keyboard.is_pressed("q"):
            break
        if not x:
            continue
        print(x)

# can check if a number is prime
def isprime(n):
    for i in range(2, (n//2)+1):
        if n%i == 0:
            return False
    return True

# Allows users to select if they want prime numbers or not
def primestateselect():
    while True:
        y = input("Would you like only prime numbers: y or n: ")

        if y == "y":
            return True
        elif y == "n":
            return False

# Sets up an option for users to select the peramiters they want
print("you will now need to select parameters")

# runs primestateselect() that allows users to select if they want prime numbers or not
y = primestateselect()

# Main Loop
while True:
    x = input("Would you like a list, an infinite number or just one number: enter lst, inf, num, or x to quit: ")
    if x == "num" or "lst":
        n = input("Enter the Nth number in the fib sequence you would like to calculate to or up to: ")

    if x == "lst":
        print(str(fiblist(int(n,y))))
    elif x == "num":
        print(str(fib(int(n,y))))
    elif x == "inf":
        inflist(y)
    elif x == "quit":
        break

