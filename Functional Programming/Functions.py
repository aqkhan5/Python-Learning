def display():
    print("Hello")
    a = reversed("Hello")
    print(a)
    for i in reversed(range(1,10)):
        print(i)
display()

#cube formula using the funtions in python.
def cube(n):
    m=int(n)
    return m*m*m
print("The cube of 4 =",cube(4))
x=5+6+cube(3)
print("The value of x is: ",x)
