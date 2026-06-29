# lists in python 
#lists are ordered, mutable, and allow duplicate elements. They are defined using square brackets [].
# we can store different types of data in a list, including integers, floats, strings, and even other lists.
marks: list = [90, 85, 78, 92, 88]
# Accessing elements
print(marks[1])  # Output: 85
print(type(marks))  # Output: <class 'list'>

details: list = ["John", 25, "Engineer", 3.5]
print(details[0], "is an", details[2], "with a GPA of", details[3])  # Output: John is an Engineer with a GPA of 3.5
details.append("USA")  # Adding an element to the end of the list
print(details)  # Output: ['John', 25, 'Engineer', 3.
# print(details.sort())  # This will raise an error because the list contains different data types

print(marks)  # Output: [90, 85, 78, 92, 88]
marks.sort()  # This will sort the list of marks in ascending order
print(marks)  # This will sort the list of marks in ascending order
marks.sort(reverse= True)  # This will sort the list of marks in reverse order
print(marks)  # Output: [92, 90, 88, 85, 78]

# Program to ask the user to enter their three favorite movies and store them in a tuple
print("PROGRAM TO STORE THREE FAVORITE MOVIES IN A LIST")
movies = input("Enter your three favorite movies, separated by commas: ")
movies_list = movies.split(",")  # Split the input string into a list of movies
movies_list = list(movies_list)  # Convert the list to a list (though it's already a list)
print("Your favorite movies are:" , movies_list)  # Output: Your favorite movies are: ['Movie1', 'Movie2', 'Movie3']


# Write a Program ( without using functions, loops) to check if a list contain a palindrome of elements. (Hint: use copy() method
# [1,2,3,2,1]   [1, "abc", "abc", 1] are a palindrome list because it reads the same backward as forward.
print("PROGRAM TO CHECK IF A LIST CONTAINS A PALINDROME OF ELEMENTS")
lst: list = input("Enter a list of elements, separated by commas: ").split(",")  # Get user input and split it into a list 
lst_copy = lst.copy()  # Create a copy of the original list
lst_copy.reverse()  # Reverse the copy
if lst == lst_copy:
    print("The list is a palindrome")
else:
    print("The list is not a palindrome")