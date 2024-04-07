#Password Complexity Checker

def password_complexity_checker(input_string):
    n=len(input_string)
    
    hasUpper=False
    hasLower=False
    hasDigit=False
    specialchar=False
    normalchar="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    
    
    for char in input_string:
        if char.isupper():
            hasUpper=True
        if char.islower():
            hasLower=True
        if char.isdigit():
            hasDigit=True
        if char not in normalchar:
            specialchar=True
    
    # Strength of password  
    print("Strength of Password:-", end=" ")
    if(hasUpper and hasLower and hasDigit and specialchar and n>=8):
        print("Strong")
    elif((hasUpper or hasLower) and hasDigit and specialchar and n>=6):
        print("Moderate")
    else:
        print("Weak")

#User Input        
input_string=input("Enter a Password: ")
password_complexity_checker(input_string)
