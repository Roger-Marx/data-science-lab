def meow(n: int) -> str:    
    """"
    Repeat "meow" n times, one per line
    
    """
    return "meows\n" * n

number: int  = int(input("Number: "))
#number: int  = input("Number: ")

meows:str = meow(number)
#meow(number)

print(meows)