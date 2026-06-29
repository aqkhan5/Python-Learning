# Tuples in python
# Tuples are ordered, immutable, and allow duplicate elements. They are defined using parentheses ().
# Unlike lists, tuples cannot be changed after creation.
tup: tuple = (10, 20, 30, 50,70)
print(tup[1])  # Output: 20
print(type(tup))  # Output: <class 'tuple'>
details_tuple: tuple = ("Alice", 30, "Doctor", 4.0)
print(details_tuple[0], "is a", details_tuple[2], "with a GPA of", details_tuple[3])  # Output: Alice is a Doctor with a GPA of 4.0
print(tup[:4])

