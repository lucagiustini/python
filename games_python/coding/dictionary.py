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
variable = TARGETS[0]["ip_address"]

TARGETS = {
    "Left" : {"ip_address": "ok", "user_name": "ok", "psw": "ok"},
    "Right" : {"ip_address": "ok", "user_name": "ok", "psw": "ok"},
    "W" : {"ip_address": "ip_address", "user_name": "ok", "psw": "ok"},
    "daje" : {"ip_address": "ok", "user_name": "ok", "psw": "ok"},
    "T" : {"ip_address": "ok", "user_name": "ok", "psw": "ok"}
}

# to call the ip address of the HA_Left, I can use the following syntax:
variable = TARGETS["Left"]["ip_address"]

TARGETS = [{
    'Server':{'target_name': 'UBUNTU', 'ip': '192.168.1.100', 'user_name': 'user', 'arch_type': 'x86',
    'containers_ip_base': '192.168.1.23', 'it_name': 'ens33', 'network_lan':'ipvlan', 'nb_container': '1'},
    'Client':{'target_name': 'UBUNTU_RT', 'ip': '192.168.2.200', 'user_name': 'user', 'arch_type': 'x86',
    'containers_ip_base': '192.168.1.26', 'it_name': 'eno1', 'network_lan':'ipvlan', 'nb_container': '1'}
}]
# I want to call the ip of the Server
for element in TARGETS:
    print(element['Server']['ip'])

TARGETS_SERVER = [
    {'target_name': 'UBUNTU', 'ip': '192.168.1.100', 'user_name': 'user', 'arch_type': 'x86',
    'containers_ip_base': '192.168.1.23', 'it_name': 'ens33', 'network_lan':'ipvlan', 'nb_container': '1'},
]
# I want to call the ip of the Server
for element in TARGETS_SERVER:
    print(element['ip'])

TARGETS_CLIENT = [
    {'target_name': 'UBUNTU_RT', 'ip': '192.168.2.200', 'user_name': 'user', 'arch_type': 'x86',
    'containers_ip_base': '192.168.1.26', 'it_name': 'eno1', 'network_lan':'ipvlan', 'nb_container': '1'}
]
