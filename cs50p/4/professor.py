import random


def main():
    
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y
        attempts = 0
        while attempts < 3:
            try:
                user = int(input(f"{x} + {y} = "))
            except ValueError:
                print("EEE")
                attempts += 1
            else:
                if user == answer:
                    score += 1
                    break
                else:
                    print("EEE")
                    attempts += 1
        if attempts == 3:
            print(f"{x} + {y} = {answer}")
    print(f"Score: {score}")


def get_level():

    while True:
            try:
                x = int(input("Level: "))
            except ValueError:
                pass
            else:
                if x in [1, 2, 3]:
                    return x




def generate_integer(level):
    
    if level not in [1, 2, 3]:
        raise ValueError("Invalid level")

    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()