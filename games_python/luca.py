my_list = [1, 2, 3, [4, 5]]

object = input("Enter a number or string: ")

str = object[0]

print(str)


my_list[3][0] = 6
my_list.append(str)
my_list.append(object)

print(my_list)


for ella in my_list:
    print(ella)
print()
    
for i in range(2, len(my_list)):
    elemento = my_list[i]
    print("L'elemento e' con indice ", i, " e' ", elemento)