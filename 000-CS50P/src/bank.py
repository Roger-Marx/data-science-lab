balance = 0  #declaring variable outside of the function so that it can be accessed by all functions GLOBAL

def main():
    global balance #balance is a global variable, but is now accessible and modifieable from inside the function
    print("Balance:", balance)
    deposit(100)
    print("Balance:", balance)
    withdraw(50)
    print("Balance:", balance)




def deposit(n):
    global balance #balance is a global variable, but is now accessible and modifieable from inside the function
    balance += n

def withdraw(n):
    global balance #balance is a global variable, but is now accessible and modifieable from inside the function
    balance -= n


if __name__ == "__main__":
    main()
    