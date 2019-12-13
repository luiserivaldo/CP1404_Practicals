string_input = str(input("Insert a string: "))
string_list = string_input.split()
string_dict = {}
for x in string_list:
    string_dict = {string_list[i]: 1 for i in range(0, len(string_list))}

print(string_list)
print(string_dict)
for x in string_dict:
    print(x, ":", string_dict[x])
