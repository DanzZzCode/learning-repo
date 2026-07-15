import random

def main():
    x = validate_lvl()
    z = random.randint(1, x)
    
    # Use an infinite loop to handle the back-and-forth guessing game mechanics
    while True:
        g = validate_gs()
        
        if g < z:
            print("Too small!")
        elif g > z:
            print("Too large!")
        else:
            print("Just right!")
            break  # Exit the loop entirely when they guess correctly


def validate_lvl():
    while True:
        try:
            l = int(input("Level: "))
        except ValueError:
            pass
        else:
            if l > 0:
                return l
            else:
                pass

def validate_gs():
    while True:
        try:
            g = int(input("Guess: "))
        except ValueError:
            pass
        else:
            if g > 0:
                return g
            else:
                pass


if __name__ == "__main__":
    main()