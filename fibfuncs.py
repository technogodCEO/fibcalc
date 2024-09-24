import keyboard

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
        if keyboard.is_pressed("q"):
            break

