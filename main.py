import leif
import alex
import ammar

def main():
    user_input = input("Skriv t.ex. 'leif food', 'alex drink' eller bara 'ammar': ").lower().split()

    if len(user_input) == 1:
        name = user_input[0]
        action = "hello"
    elif len(user_input) == 2:
        name = user_input[0]
        action = user_input[1]
    else:
        print("Fel format")
        return

    if name == "leif":
        if action == "hello":
            leif.hello()
        elif action == "food":
            leif.food()
        elif action == "drink":
            leif.drink()
        else:
            print("Okänd funktion för Leif")

    elif name == "alex":
        if action == "hello":
            alex.hello()
        elif action == "food":
            alex.food()
        elif action == "drink":
            alex.drink()
        else:
            print("Okänd funktion för Alex")

    elif name == "ammar":
        if action == "hello":
            ammar.hello()
        elif action == "food":
            ammar.food()
        elif action == "drink":
            ammar.drink()
        else:
            print("Okänd funktion för Ammar")

    else:
        print("Ingen sådan person")

if __name__ == "__main__":
    main()