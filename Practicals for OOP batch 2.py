#Prog01: Create a program that ask user to input 2 numbers. Print the smaller number.
#Prog02: Create a program that ask user to input 2 numbers. Print "Not Equal" when the numbers are not the same.
#Prog03: Create a program that ask user to input 2 numbers. Print the difference of the two numbers.
#Prog04: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers without the decimal point
#Prog05: Create a program that ask user to input 2 numbers. Print the remainder when the first number is divided by the second number.
#Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.
#Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.
#Prog08: Create a program that print all the odd numbers starting from 0 to 100. (Use while loop)
#Prog09: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five.
#Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.

def prog01():
    while True:
        try:
            num_1 = float(input("Please enter the first number here: "))
            num_2 = float(input("Please input the second number here: "))
            break
        except ValueError:
            print("Invalid input! Please only input numbers")
    if num_1 > num_2:
        print(f'{num_2} is the smaller number')
    elif num_1 < num_2:
        print(f'{num_1} is the smaller number')
    else:
        print('There is no bigger number')

def prog02():
    while True:
        try:
            num_1 = float(input("Please enter the first number here: "))
            num_2 = float(input("Please input the second number here: "))
            break
        except ValueError:
            print("Invalid input! Please only input numbers")
    if num_1 != num_2:
        print('Not Equal')
    elif num_1 == num_2:
        print('Equal')
    else:
        print('Something went wrong')

def prog03():
    while True:
        try:
            num_1 = float(input("Please enter the minuend here: "))
            num_2 = float(input("Please input the subtrahend here: "))
            break
        except ValueError:
            print("Invalid input! Please only input numbers")
    print(f'The difference between your two numbers is {num_1 - num_2}')

def prog04():
    while True:
        try:
            num_1 = float(input("Please enter the dividend here: "))
            num_2 = float(input("Please input the divisor here: "))
            if num_2 == 0:
                print("You cannot divide by zero, please change the divisor")
                continue
            break
        except ValueError:
            print("Invalid input! Please only input numbers")
    print(f'Your quotient is {int(num_1 / num_2)} (without the decimal)')


def prog05():
    while True:
        try:
            num_1 = float(input("Please enter the dividend here: "))
            num_2 = float(input("Please input the divisor here: "))
            if num_2 == 0:
                print("You cannot divide by zero, please change the divisor")
                continue
            break
        except ValueError:
            print("Invalid input! Please only input numbers")
    print(f'The remainder is {int(num_1 % num_2)}')
 
def prog06():
    while True:
        try:
            num_1 = float(input("Please enter the number 1 here: "))
            for rep in range(9):
                num2_10 = float(input(f'Please enter the number {rep + 2} here: '))
                num_1 -= num2_10
            break
        except ValueError:
            print("Invalid input! Please only input numbers")
    print(f'The first number when subtracted to the rest of the numbers is {num_1}')

def prog07():
    even_count = 0
    for rep in range(10):
        while True:
            try:
                num = int(input(f'Please input the number {rep + 1} here: '))
                break
            except ValueError:
                print("Invalid input! Please only input numbers")
        if num % 2 == 0:
            even_count += 1
    print(f'You have inputted {even_count} even number/s')        

def prog08():
    num = 0
    while num < 101:
        if num % 2 == 1:
            print(num)
        num += 1    

def prog09():
    for rep in range(101):
        if rep % 5 != 0:
            print(rep)

def prog10():
    while True:
        try:
            num_1 = int(input("Please enter the first number here: "))
            num_2 = int(input("Please input the second number here: "))
            break
        except ValueError:
            print("Invalid input! Please only input numbers")
    
    if num_1 > num_2:
        print(f'The numbers between {num_2} and {num_1} are the following: ')
        for num in range(num_1 - 1, num_2, -1):
                print(num)
    elif num_1 < num_2:
        print(f'The numbers between {num_1} and {num_2} are the following: ')
        for rep in range((num_1 + 1), num_2):
                print(rep)
    else:
        print('Those are equals. No numbers in between')
    

while True:
    try:
        choice = int(input('''What would you like to do?
        #Program 1: Ask user to input 2 numbers. Print the smaller number.
        #Program 2: Ask user to input 2 numbers. Print "Not Equal" when the numbers are not the same.
        #Program 3: Ask user to input 2 numbers. Print the difference of the two numbers.
        #Program 4: Ask user to input 2 numbers. Print the quotient of the two numbers without the decimal point
        #Program 5: Ask user to input 2 numbers. Print the remainder when the first number is divided by the second number.
        #Program 6: Ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.
        #Program 7: Ask user to input 10 numbers. Print how many are even numbers.
        #Program 8: Print all the odd numbers starting from 0 to 100. (Use while loop)
        #Program 9: Print all the numbers starting from 0 to 100 except numbers ending in zero or ending five.
        #Program 10: Ask user to input 2 numbers. Print all the numbers between the two numbers.
        Choose from 1-10: '''))
    except ValueError:
        print("Invalid input, please use only numbers.")


    if choice == 1:
        prog01()
    elif choice == 2:
        prog02()
    elif choice == 3:
        prog03()
    elif choice == 4:
        prog04()
    elif choice == 5:
        prog05()
    elif choice == 6:
        prog06()
    elif choice == 7:
        prog07()
    elif choice == 8:
        prog08()
    elif choice == 9:
        prog09()
    elif choice == 10:
        prog10()
    else:
        print("Please only choose from 1-10")

                    

