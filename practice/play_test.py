# def has_key(inventory):
#     if "key" in inventory:
#         return True
#     else:
#         return False

# print(has_key(["sword", "key", "portion"]))
# print(has_key(["sword", "portion"])) 



# items = ['map']
# if "rope" not in items:
#     items.append("rope")

# print(len(items))
# remove = input("Which item do you want to remove: ")
# if remove in items:
#     items.remove(remove)

# print(items)



# def main_menu():
#     while True:
#         print("1")
#         print("2")
#         print("3")
#         print("q")

#         choice = input("choose an option from 1, 2, 3 and q: ")

#         if choice == "1":
#             print("Success")
#         elif choice == "2":
#             print("Success")
#         elif choice == "3":
#             print("Success")
#         elif choice == "q":
#             print("Quitting...")
#             break
#         else:
#             print("Invalid option, Please try again.")

# if __name__ == "__main__":
#     main_menu()



def is_even(n):
    return n % 2 == 0
    
assert is_even(8) == True
assert is_even(5) == False
