# uppgift 1
name_list = ["Daniil", "Alice", "Angelina", "John", "Nick"]

for name in name_list:
    print(name)


# uppgift 2
name_list[0] = name_list[0][::-1].capitalize() # First name reversed.


# uppgift 3
new_name = "Viktor"
name_list.append(new_name)

for name in name_list:
    print(name)


# uppgift 4
print(f"name list length : {len(name_list)}")


# uppgift 5
name_list.pop()
print(name_list) # last name in the list disappears (if no index provided)


# uppgift 6 - 7 (lägga till och ta bort namn)
def show_names(name_list):
    if len(name_list) == 0:
        print("\nYour name list is empty.")
        return

    print("\nCurrent name list: ") 
    for index, name in enumerate(name_list, 1):
        print(f"{index}.{name}")


def remove_name(name_list):
    print(f"Type in name for removal (or 'q' to quit removal mode)")

    while True: 
        show_names(name_list)
        user_input = input("name to remove :")
        
        if user_input == "q":
            return name_list
        elif user_input in name_list:
            removal_name_index = name_list.index(user_input)
            name_list.pop(removal_name_index) # name_list.remove(name) if you want to delete multiple identical same names. 
        elif len(name_list) > 0:
            print("No such name found in the list.")
        

def add_name(name, name_list):
    name_list.append(name)
    return name_list


name_list = []

# main
while True:
    user_input = input("name to add: ").strip(" ")

    if user_input == "q":
        break
    elif user_input == "r":
        name_list = remove_name(name_list)
    else:
        name_list = add_name(user_input, name_list)

# final list
show_names(name_list)


# uppgift 8
car_brand = {"mark" : "BMV", "color": "gray", "year" : 1929}

for key in car_brand.keys():
    print(f"{key} : {car_brand[key]}")

