def fib(number, mem):
    if number == 1:
        return 1
    elif number == 2:
        return 1
    else:
        return fib(number - 1, mem) + fib(number - 2, mem)

def fiblist(number, mem):
    lst = []
    for i in range(number - 1):
        curr = fib(i, mem)
        lst.append(curr)
    return lst

def inflist(mem):
    counter = 1
    while True:
        currFibVal = fib(counter, mem)
        counter += 1
        print(currFibVal)


