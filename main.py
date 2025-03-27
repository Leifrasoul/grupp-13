import leif
import alex

def main():
    user_input = input("Skriv t.ex. 'leif food', 'alex drink' eller bara 'leif': ").lower().split()

    # Standard: om bara ett namn anges, använd "hello"
    if len(user_input) == 1:
        name = user_input[0]
        action = "hello"
    elif len(user_input) == 2:
        name = user_input[0]
        action = user_input[1]
    else:
        print("Fel format")
        return

    # LEIF
    if name == "leif":
        if action == "hello":
            leif.hello()
        elif action == "food":
            leif.food()
        elif action == "drink":
            leif.drink()
        else:
            print("Okänd funktion för Leif")

    # ALEX
    elif name == "alex":
        if action == "hello":
            alex.hello()
        elif action == "food":
            alex.food()
        elif action == "drink":
            alex.drink()
        else:
            print("Okänd funktion för Alex")

    else:
        print("Ingen sådan person")

if __name__ == "__main__":
    main()