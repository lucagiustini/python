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


# I want to define a list of dictionaries, each dictionary containing the variables of each target
TARGETS = [
    {"ip_address": "ok", "user_name": "ok", "psw": "ok"},
    {"ip_address": "ok", "user_name": "ok", "psw": "ok"},
    {"ip_address": "ok", "user_name": "ok", "psw": "ok"},
    {"ip_address": "ok", "user_name": "ok", "psw": "ok"},
    {"ip_address": "ok", "user_name": "ok", "psw": "ok"},
    {"ip_address": "ok", "user_name": "ok", "psw": "ok"}
]
# to call the ip address of the first target, I can use the following syntax:
# variable = TARGETS[0]["ip_address"]

# I want to define a dictionary containing key-value pairs, 
# where each key represents a target name and the corresponding value is another dictionary with IP address, username, and password information.

TARGETS = {
    "HA_Left" : {"ip_address": "ok", "user_name": "ok", "psw": "ok"},
    "HA_Right" : {"ip_address": "ok", "user_name": "ok", "psw": "ok"},
    "CRD" : {"ip_address": "ip_address", "user_name": "ok", "psw": "ok"},
    "SWITCH_1" : {"ip_address": "ok", "user_name": "ok", "psw": "ok"},
    "SWITCH_2" : {"ip_address": "ok", "user_name": "ok", "psw": "ok"}
}

# to call the ip address of the HA_Left, I can use the following syntax:
# variable = TARGETS["HA_Left"]["ip_address"]