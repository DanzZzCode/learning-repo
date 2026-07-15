import emoji

def main():
    x = input("Input: ")
    print(f"Output: {emoji.emojize(x, language='alias')}")

if __name__ == "__main__":
    main()