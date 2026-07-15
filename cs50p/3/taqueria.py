def main():
    price = 0.00
    while True:
        try:    
            order = input("Item: ").lower()
        except EOFError:
            break
        else:
            item_price = check_order(order)
            if item_price > 0:
                price += item_price
                print (f"Total: ${price:.2f}")

def check_order(item):
    menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}   

    for dish in menu:
        if item == dish.lower():
            return menu[dish]
    return 0.00

main()