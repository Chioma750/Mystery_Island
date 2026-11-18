def main_menu():
    while True:
        print("=====You are at the beach=====")
        print("1. Look around")
        print("2. Quit")

        choice = input("Make a choice from 1 and 2: ")

        if choice == "1":
            print("Taking a look around the beach")
        elif choice == "2":
            print("Quitting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()