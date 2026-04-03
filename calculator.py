

def add() -> int:
    a:int = int(input("Enter a: "))
    b:int = int(input("Enter b: "))
    c:int = a + b   
    return c

def subtract() -> int:
    a:int = int(input("Enter a: "))
    b:int = int(input("Enter b: "))
    c:int = a - b
    return c

def main():
    a=input("Enter mode \n 1. Add\n 2. Subtract\n")
    if (a=="1"):
        print(add())
    elif (a=="2"):
        print(subtract())
        
