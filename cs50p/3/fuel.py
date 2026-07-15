def main():
    z = user_input("Fraction: ")
    print(f"{z}")

def user_input(prompt):
    while True:
        try:
            x , y = map(int, input(prompt).split('/'))
        except ValueError:
            pass
        else:
            if 0 <= x <=y and y !=0:
                result = round((x/y) * 100)
                if result <= 1:
                    return "E"
                elif result >= 99:
                    return "F"
                else:
                    return f"{result}%"

main()