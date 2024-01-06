student = {
    "name": "John Doe",
    "age": 20,
    "grade": "A",
    "subjects": ["Math", "Science", "English"],
    "address": {
        "street": "123 Main St",
        "city": "Exampleville",
        "state": "ABC"
    }
}

address = student["address"]
print(address)

student["age"] = 32
age_of_student = student["age"]
print(age_of_student)

student["sesso"] = "M"
sesso = student["sesso"]
print(sesso)

print()
for value in student.values():
    print(value)
print()

for key in student.keys():
    print(key)

print()
for key, value in student.items():
    print(key, "=", value)
