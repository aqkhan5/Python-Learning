"""
String METHODS
        Strings are immutible( mean you can't change them) mean we can't change it in place.
        we can make its copy as given in the lower example.
"""
a="Abdul Qadeer Khan !!!"
print(len(a))
print(a)
print(a.upper())

#Now here in lower example it has not change the previous string it has made a new one. so string is immutible
print(a.lower())

#rstrip      it remove the trailing characters
print(a.rstrip("!"))

#Replace        it replace one string with the other
print(a.replace("Qadeer","Khan"))

#Split       it convert string into the list
print(a.split(" "))

#Capitalize     it capitalize the first character and convert all other to lower case
Blog="introductIon to Blog"
print(Blog.capitalize())

#Center     It simply center the string
str="Welcome to phthon"
print(len(str.center(50)))
print(len(str))

#count       It count how many times a word is came in the string
print(a.count("Khan"))

# EndsWith          It tells whether a string is ending with this letter or not
print(a.endswith("!!!"))

# Find      it search first occurence of a given value and returns index where it is present. if string is not presen then
            #it returns -1
found="He is a good boy, He nevers lie. He is a genious"
print(found.find("is"))

#Isalnum    It tells whether the string is alpha numeric or not(mean it contain a-z, A-Z,0-9)
print(a.isalnum())

#IsAlpha        It tells about only alpha(a-z,A-Z). not include numbers or symbols
print(a.isalpha())

#Islower         tells whether the string is in lower case or not( gives true or false)
#Isprintable     If all the value are printable returns true otherwise false(/n,/t are non printable)
print(a.isprintable())

#isspace         It returns true if the string contain the wide spaces( ONly the wide spacesf)
pace="   "
print(pace.isspace())

#Is title  it return true if the first letter of the each word is capital otherwise false
title="My Name Is Abdul Qadeer Khan"
print(title.istitle())

#Startswith       It returns the true value if the first word of the sentence is exact as given in the code
start="Python is interpreted language"
print(start.startswith("Python"))

#swapcase       it convert the upper case into lower case and lower case into the upper case
Swap="Python is interpreted language"
print(Swap.swapcase())

#Title      It capitalize each word of the string only the first word of the letter
TITLE="Python is interpreted language"
print(TITLE.title())

#
