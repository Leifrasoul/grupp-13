import leif 
import alex
def main():
    user_input = input("Vem vill du prata med").lower().split()

    if len(user_input) == 1:
        name = user_input[0]
        action = "hello"
    elif len(user_input) == 2:
        name, action = user_input
    else:
        print("Fel format")
        return

    if name == "sebbe":
        if action == "hello":
            leif.hello()
        elif action == "food":
            leif.food()
    elif name == "alex":
        if action == "hello":
            alex.hello()
        elif action == "food":
            alex.food()
    else:
        print("Ingen sådan person ")

if __name__ == "__main__":
    main()