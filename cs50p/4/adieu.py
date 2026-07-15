import inflect

def main():
    
    name_list=[]
    p = inflect.engine()

    while True:
        try:
            name_list.append(input("Name: "))
    
        except EOFError:
            print()
            break
    
    print(f"Adieu, adieu, to {p.join(name_list)}")

if __name__ == "__main__":
    main()