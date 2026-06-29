"""
String
    any thing that is enclosed in the double quotes "" is considered as a string you can also use the single quote
"""
name="AQ Khan"
Friend="Arslan Ali Shah"
#we use escape sequence to add double quote into a string
apple="He said, \"I want to eat apple"

#Multiline String
Orange="""" Hey Gentleman,
Iam Good at all 
How are you """
print("Harry, ",name)
print(apple)
print(Orange)

#In python string is like an array of character
a="Hello world"
print(a[1])
print(a[0])

#Looping through the string
#                we can loop through the string using the for loop
print("Lets used the loop")
for abu in a:
    print(abu)
print(5)
print("Daddy")

#String Length
#       we can find length of string using this function:  len()
print(len(a))

#CheckStringDaddy
#       The key word  'in' is used to find that whether the character or pharase is present in a string or not
txt="The life is free! just imagine"
print("free" in txt)

#Use of check string in if statement
if "free" in txt:
    print("Yes! 'free' is present in the text")

#Check if Not
    # keyword    not in    is used to check if the pharase is not present in string
    print("expensive" not in txt)

#For if statement
if "expensive" not in txt:
    print("NO! 'expensive' is not present in string")

#String Slicing
        # String slicing is used to get the specific part of the string
Ali="TheBullRun"
print(Ali[3:7])
#To get slice from start to specific point just right end position
print(Ali[:5])
#To get slice till end just give the point whethere to start
print(Ali[5:])
#Negative indexing
            #to start the string from the end to specific point
print(Ali[5:-2])
print(Ali)

#Format String
        # we cannot simply concatinate string by just adding + between  in and string
        #We use variablename.format(int)
age=36
text="I am Abdul Qadeer and {} is my age"
print(text.format(age))
#For unlimited numbers arguments are placed in the following ways
quantity=3
item=70
price=30.4
MyOrder="I want {} pieces of {} items in {} dollars"
print(MyOrder.format(quantity,item,price))

# we can also use the {0} index numbers to ensure that he argument are placed in correct placehold
Order="I want to pay {2} dollar for {0} pieces of {1} items"
print(Order.format(quantity,item,price))