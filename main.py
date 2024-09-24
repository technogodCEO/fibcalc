import fibfuncs as fib

while True:
    x = input("Would you like a list, infinite list, or just one number: enter lst, num, inf, or x to quit: ")
    if x == "lst" or x == "num":
        number = input("Enter the Nth number in the fib sequence you would like to calculate to or up to: ")
    if x == "lst":
        print(fib.fiblist(int(number)))
    elif x == "num":
        print(fib.fib(int(x)))
    elif x == "inf":
        print(fib.inflist())
    elif x == "quit":
        break
