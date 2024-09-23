
def fib(number):
    if number == 1:
        return 1
    elif number == 2:
        return 1
    else:
        return fib(number - 1) + fib(number - 2)

def fiblist(number):
    lst = []
    for i in range(number - 1):
        curr = fib(i)
        lst.append(curr)
    return lst

def inflist():
    counter = 1
    while True:
        currFibVal = fib(counter)
        counter += 1
        print(currFibVal)



while True:
    x = input("Would you like a list, infinite list, or just one number: enter lst, num, inf, or x to quit: ")
    if x == "lst" or x == "num":
        number = input("Enter the Nth number in the fib sequence you would like to calculate to or up to: ")
    if x == "lst":
        print(fiblist(int(number)))
    elif x == "num":
        print(fib(int(x)))
    elif x == "inf":
        print(inflist())
    elif x == "quit":
        break
