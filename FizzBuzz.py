def Fizzle(x):
    
    if x % 3 == 0 and x % 5 == 0:
        print("Pop")
    elif x % 5 == 0:
        print("Buzz")
    elif x % 3 == 0:
        print("Fizz")
    else: print("That number is flat")

Fizzle(1)