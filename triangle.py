#Create lower triangular, upper triangular and pyramid containing the "*" character.

def lower_triangle(m):
    for i in range(m):    
        for j in range(i+1):
            print('*',end="")
        print()
        
def upper_triangle(m):
    for i in range(m):    
        for j in range (i): print(" ",end='')
        for j in range(i,m):
            print('*',end="")
        print()
        
def pyramid(m):
    for i in range(m):
        for j in range(i,m): print(" ", end='')
        for j in range(i): print("*", end='')
        for j in range(i+1): print('*',end='')
        print()

user = input("Enter one option(1,2,3) \n1.Lower Triangle \n2.Upper Triangle \n3.Pyramid\n")

match user:
    case "1":
        n= int(input("Enter the maximum number of * = "))
        lower_triangle(n)
    case "2":
        n= int(input("Enter the maximum number of * = "))
        upper_triangle(n)
    case "3":
        pyramid(7)
    case _:
        print("Invalid Input try again")




