# dictionaries in python.
# Dictionaries are unordered, mutable, and do not allow duplicate keys. They are defined using curly braces {}.
# A dictionary consists of key-value pairs, where each key is unique and maps to a value. The keys can be of any immutable data type, such as strings, numbers, or tuples,

diction_1: dict = {"name": "Abdul", "age": 25, "profession": "Computer Scientist"}
print(f"I am {diction_1['name']} a {diction_1['age']} years old {diction_1['profession']}")

# Nested Dictionary
students= {
    "name": "AQ Khan",
    "Subjects" : {
        "phy" : 97,
        "chem" : 98,
        "math" : 95
    }
}

print(students)
print(students["Subjects"])
print(students["Subjects"]["math"])

#Dictionary methods
print(students.keys())

# Converting dictionary into lists.
print(list(students.keys()))
print(len(list(students.keys())))

#Getting Dictionary values
print(students.values())
print(list(students.values()))

# Getting dicitonary items
print(students.items())
print(list(students.items()))

# Getting Key according to value.
print(students["name"])
print(students.get("name
" \
"





"))