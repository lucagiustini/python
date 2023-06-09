value1 = int("32")
value2 = int("56")
print(value1+value2)
print(value1-value2)
print(value1/value2)
print(value1*value2)
print(value1%value2)

userName = str("Luca")
print("Name: " + userName)


stringDataTypes = "12"
intDataType = 12
# conversion of string to int
stringDataTypeToIntDataType = int(stringDataTypes)
print(type(stringDataTypeToIntDataType))
# conversion of int to string
intDataTypeToStringDataType = str(intDataType)
print(type(intDataTypeToStringDataType))
#conversion of int to float
intDataTypeToFloatDataType = float(intDataType)
print(type(intDataTypeToFloatDataType))



print("Lambda Functions in Python")
print("lambda Function in python")

# addition using lambda
doSum = lambda a, b: a+b
print(doSum(2,3))
doSub = lambda a, b: a-b
print(doSub(2,3))
doMultiPly = lambda a, b: a*b
print(doMultiPly(2,3))
doDivision = lambda a, b: a/b
print(doDivision(2,3))


