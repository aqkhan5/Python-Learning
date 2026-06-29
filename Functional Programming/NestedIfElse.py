#WhileLoop
n=0
while n<=10:
    print(n)
    n=n+1
if n>0:
    print("True")

print("Hello World")
#If-else
if n>0:
    print("Cr is Good!")
else:
    print("Cr is Bad  boy")
    print("So he need some consultancey")
#Elif
budget=200
applePrice=210
if(applePrice<=budget):
    print("Jarvis add apple to the cart")
else:
    print("Jarvis. don't add apple to the cart")

#IfElseIf

f=int(input("Enter the number"))
if(f<0):
    print("The number is negative")
elif(f>0):
    if(f<=10):
        print("The number is between 1-10")
    elif(f>10and f<=20):
        print("The number is between 11-20")
    else:
        print("The number is greater than 20")
elif(f==99):
    print("The number is special")
else:
    print("The number is zero")
