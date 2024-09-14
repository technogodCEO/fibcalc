def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

x = input("Enter the Nth number in the fib sequence you would like to calculate: ")
print(fib(int(x)))