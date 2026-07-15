def main():
    name = input("camelCase: ")
    snake_case(name)

def snake_case(word):
    word = word.strip()
    new_word = ""
    for c in word:
        if c == c.lower():
            new_word = new_word + c
        else:
            new_word = new_word + "_" + c.lower()
    print(new_word)

main()
