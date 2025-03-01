#Activity for Object Oriented Programming
#Prog01: Create a program that ask user to input 2 numbers. Print the bigger number.
#Prog02: Create a program that ask user to input 2 numbers. Print "Equal" when the numbers are the same.
#Prog03: Create a program that ask user to input 2 numbers. Print the sum of the two numbers.
#Prog04: Create a program that ask user to input 2 numbers. Print the product of the two numbers.
#Prog05: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers with the decimal point
#Prog06: Create a program that ask user to input 2 numbers. Print the result when the first number is raised to the second number.
#Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.
#Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.
#Prog09: Create a program that print all the even numbers starting from 0 to 100. (Use for loop)
#Prog10: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.

def prog01():
    while True:
        try:
            first_num = float(input("Please input the first number here: \n"))
            second_num = float(input("Please input the second number here: \n"))
            if first_num > second_num:
                print("The bigger number is:", first_num)
            elif first_num == second_num:
                print("There are no bigger number")
            else:
                print("The bigger number is:", second_num)
            break    
        except ValueError:
            print("Invalid Input! Please Enter numbers only!")        

def prog02():
    while True:
        try:
            first_num = float(input("Please input the first number here: \n"))
            second_num = float(input("Please input the second number here: \n"))
            if first_num == second_num:
                print("Equal")
            else:
                print("Not Equal")
            break    
        except ValueError:
            print("Invalid Input! Please Enter numbers only!")        
       

def prog03():
    while True:
        try:
            first_num = float(input("Please input the first number here: \n"))
            second_num = float(input("Please input the second number here: \n"))
            print("The sum of your two numbers is:", first_num + second_num)
            break
        except ValueError:
            print("Invalid Input! Please Enter numbers only!")            

def prog04():
    while True:
        try:  
            first_num = float(input("Please input the first number here: \n"))
            second_num = float(input("Please input the second number here: \n"))
            print("The product of your two numbers is:", first_num * second_num)
            break
        except ValueError:
            print("Invalid Input! Please Enter numbers only!")            

def prog05():
    while True:
        try:  
            first_num = float(input("Please input the first number here: \n"))
            second_num = float(input("Please input the second number here: \n"))    
            print(f"The quotient of your two numbers is: {first_num / second_num:.2f}")
            break
        except ValueError:
            print("Invalid Input! Please Enter numbers only!")
        except ZeroDivisionError:
            print("You cannot divide by 0, please change the second input!")                       

def prog06():
    while True:
        try:  
            first_num = float(input("Please input the first number here: \n"))
            second_num = float(input("Please input the second number here: \n"))
            print("Your first number when raised to your second number is:", first_num ** second_num) 
            break
        except ValueError:
            print("Invalid Input! Please Enter numbers only!")        
    
def prog07():
    total = 0
    for i in range(10):
        while True:
            try:
                num = float(input(f"Please input number {i + 1}: \n"))
                break
            except ValueError:
                print("Invalid Input! Please Enter numbers only!")            
        total += num
    print("The sum of your numbers is:", total)  

def prog08():
    odd = 0
    for i in range(10):
        while True:
            try:
                num = int(input(f"Please input number {i + 1}: \n"))
                break
            except ValueError:
                print("Invalid Input! Please Enter numbers only!")        
        if num % 2 == 1:
            odd +=1
    print("You have inputted", odd, "odd numbers")  
     

def prog09():
    for i in range(0, 101, 2):
        print(i)     

def prog10():
      for i in range (101):
        if i % 10 != 0:
            print(i)


run = True

while run:
    print("Please select which program you want to run")
    print("Program 01: Asks user to input 2 numbers. Print the bigger number.")
    print("Program 02: Asks user to input 2 numbers. Print 'Equal' when the numbers are the same.")
    print("Program 03: Asks user to input 2 numbers. Print the sum of the two numbers.")
    print("Program 04: Asks user to input 2 numbers. Print the product of the two numbers.")
    print("Program 05: Asks user to input 2 numbers. Print the quotient of the two numbers with the decimal point")
    print("Program 06: Asks user to input 2 numbers. Print the result when the first number is raised to the second number.")
    print("Program 07: Asks user to input 10 numbers. Print the sum of all the numbers.")
    print("Program 08: Asks user to input 10 numbers. Print how many are odd numbers.")
    print("Program 09: Print all the even numbers starting from 0 to 100. (Use for loop)")
    print("Program 10: Print all the numbers starting from 0 to 100 except numbers ending in zero.")
    while True:
        try:
            choice = int(input("Please pick from 1 - 10: "))
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
                print("Invalid Input! Please pick from 1-10")      
            break
        except ValueError:
            print("Invalid Input! Please Enter numbers only!") 
    while True:
        choice2 = input("Would you like to run again? (Y/N): ").strip().upper()
        if choice2 == "Y":
            break  
        elif choice2 == "N":
            run = False
            break  
        else:
            print("Invalid choice! Please enter 'Y' for Yes or 'N' for No.")
                

  

