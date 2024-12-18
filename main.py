import sys
import fibfuncs as fib

# noinspection SpellCheckingInspection
fibmem = [0,1]
sys.set_int_max_str_digits(1000000000)

while True:
    while True:
        x = input("Would you like a list, infinite list, or just one number: enter lst, num, inf, or x to quit: ")
        if x == "lst" or x == "num" or x == "inf":
            break
        else:
            print("an error occurred, please try again")
    if x == "lst" or x == "num":
        while True:
            number = input("Enter the Nth number in the fib sequence you would like to calculate to or up to: ")
            # noinspection PyBroadException
            try:
                number = int(number)
            except:
                print("an error occurred, please try again")
            else:
                break


    if x == "lst":
        print(fib.fiblist(int(number), fibmem))
    elif x == "num":
        print(fib.fib(int(number), fibmem))
    elif x == "inf":
        print("works")
        print(fib.inflist(fibmem))
    elif x == "quit":
        break

    print(""" 
    Calculation Successful
    Thank You
    """)

    # noinspection SpellCheckingInspection
    fibmem = [0,1]
