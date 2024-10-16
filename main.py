import fibfuncs as fib

mem = []

while True:
    x = input("Would you like a list, infinite list, or just one number: enter lst, num, inf, or x to quit: ")
    while True:
        if x == "lst" or x == "num":
            number = input("Enter the Nth number in the fib sequence you would like to calculate to or up to: ")
            # noinspection PyBroadException
            try:
                number = int(number)
            except:
                print("an error occurred")
            else:
                break


    if x == "lst":
        print(fib.fiblist(int(number), mem))
    elif x == "num":
        print(fib.fib(int(number), mem))
    elif x == "inf":
        print(fib.inflist(mem))
    elif x == "quit":
        break

    print(""" 
    Calculation Successful
    Thank You
    """)