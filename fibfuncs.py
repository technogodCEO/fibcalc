def fib(number, mem):
    for i in range(2, number + 1):
        mem.append(mem[-1] + mem[-2])
    return mem[number]

def fiblist(number, mem):
    for i in range(2, number + 1):
        mem.append(mem[-1] + mem[-2])
    return mem

def inflist(mem):
    counter = 0
    while True:
        mem.append(mem[-1] + mem[-2])
        counter += 1
        print(mem[counter])