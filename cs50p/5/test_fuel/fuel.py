def main():
    # Prompt for input inside main, then pass it to convert
    fraction = input("Fraction: ")
    try:
        percentage = convert(fraction)
        print(gauge(percentage))
    except (ValueError, ZeroDivisionError):
        # CS50P expects main to handle or reprompt if needed, 
        # but your convert/gauge functions must handle the core logic.
        pass

def convert(fraction):
    # Split the string by the slash
    if "/" not in fraction:
        raise ValueError
        
    try:
        x, y = fraction.split("/")
        x, y = int(x), int(y)
    except ValueError:
        raise ValueError

    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError

    return round((x / y) * 100)

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
