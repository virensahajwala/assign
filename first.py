''' Build a calculator to perform airthematic operations'''

#Function to add 2 numbers
def add(x,y):
    a=x+y
    return a

#Function to subtract 2 numbers:
def subtract(x,y):
    a=x-y
    return a

#Function to multiply 2 numbers:
def multiply(x,y):
    a=x*y
    return a

#Function to divide 2 numbers:
def divide(x,y):
    if y==0:
        print("Infinity")
        
    else:
        a=x/y
        return a

print("Choices are: Enter 1-Additon,2-subtaction,3-multiply,4-divide")


def cal(choice):
    if(choice==1):
        print(add(num1,num2))
    elif(choice==2):
        print(subtract(num1,num2))
    elif(choice==3):
        print(multiply(num1,num2))
    elif(choice==4):
        print(divide(num1,num2))
    else:
        print("Invalid")

choice=int(input("Enter selected choice:"))
num1=float(input("Enter 1st number "))
num2=float(input("Enter 2nd number "))
cal(choice)
status = int(input("Continue?0/1:"))
while status == 0:
    choice=int(input("Enter selected choice:"))
    num1=float(input("Enter 1st number "))
    num2=float(input("Enter 2nd number "))
    cal(choice)
    status = int(input("Continue?0/1:"))
    
        
        
    

