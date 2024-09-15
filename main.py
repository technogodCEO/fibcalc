def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fiblist(n):
    lst = []
    for i in range(n-1):
        curr = fib(i)
        lst.append(curr)
    return lst

while True:
    x = input("Would you like a list or just one number: enter lst, num, or x to quit: ")
    n = input("Enter the Nth number in the fib sequence you would like to calculate to or up to: ")
    if x == "lst":
        print(fiblist(int(n)))
    elif x == "num":
        print(fib(int(x)))
    elif x == "quit":
        break
