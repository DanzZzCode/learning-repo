def main():
    x = input("Greeting: ")
    checkg(x)

def checkg(greeting):
    greeting = greeting.lstrip().lower()
    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")

main ()