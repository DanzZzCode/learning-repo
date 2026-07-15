def main ():
    x , y , z = input("Expression: ").strip().split()

    num1 = float(x)
    num2 = float(z)
    if y == '/' and num2 == 0.0:
        print("Can't divide by zero")
    else:
        match y:
            case "+":
                print(f"{num1 + num2:.1f}")
            case "-":
                print(f"{num1 - num2:.1f}")
            case "*":
                print(f"{num1 * num2:.1f}")
            case "/":
                print(f"{num1 / num2:.1f}")

main()