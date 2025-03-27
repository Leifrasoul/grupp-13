import leif 
import alex
def main():
    namn = input("Vem vill du säga hej till? ").lower()

    if namn == "leif":
        leif.hello()
    elif namn == "alex":
        alex.hello()
    else:
        print("Ingen sådan person ")

if __name__ == "__main__":
    main()