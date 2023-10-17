# Addition
def add(x, y):
    return x + y

# Subtraktion
def subtract(x, y):
    return x - y

# Multiplikation
def multiply(x, y):
    return x * y

# Dividering
def divide(x, y):
    return x / y

print("Select option.")

print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True: 
    # Inmatning
    choice = input("Enter choice(1/2/3/4):")
    
    # 
    if choice in ('1', '2', '3', '4'):
        try: 
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
            
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2)) 
            
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2)) 
            
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2)) 
            
    # Fortsätta räkna?
    # Avsluta om användaren inte vill fortsätta räkna
    
    next_calculation = input("Let's do next calculation? (yes/no): ")
    
    # Avslutar om användaren skriver no
    if next_calculation == "no" :
        break
    
    # Fortsätter om användaren skriver yes
    if next_calculation == "yes" : 
        continue   

        
    else:
        print("Invalid Input")