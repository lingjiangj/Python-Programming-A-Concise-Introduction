# problem1_1

def problem1_1():
    print("Problem Set 1")
    
    
# problem1_2

def problem1_2(x,y):
    sum = x+y
    product = x*y
    print(sum)
    print(product)

    
# problem1_3

def problem1_3(n):
    my_sum = 0
    for i in range (1,n+1):
        my_sum +=i
    print(my_sum)
    

# problem1_4

def problem1_4(miles):
    feet = miles*5280
    print("There are",feet,"feet in",miles, "miles.")
    
# problem1_5

def problem1_5(age):
    if age < 7:
        print("Have a glass of milk.")
    elif age >=7 and age <21:
        print("Have a coke.")
    else:
        print("Have a martini.")
        
 
#problem1_6

def problem1_6():
    for i in range (1,100,2):
        print(i, end=" ")
 

# problem1_7

def problem1_7():
    b1=input("Enter the length of one of the bases: ")
    b2=input("Enter the length of the other base: ")
    h=input("Enter the height: ")
    B1 = float(b1)
    B2 = float(b2)
    H = float(h)
    A = (1/2)*(B1+B2)*H
    print("The area of a trapezoid with bases",B1,"and",B2,"and height",H,"is",A)

 



    

