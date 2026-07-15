def main():
    grocery_dict = {}
    while True:
        try:
            item = input().upper()
        except EOFError:
            print()
            print_list(grocery_dict)
            break
        else:
            if item in grocery_dict:
                grocery_dict[item] += 1
            else:
                grocery_dict[item] = 1

def print_list(item_dict):
    for item in sorted(item_dict):
        print(f"{item_dict[item]} {item}")
    

main()