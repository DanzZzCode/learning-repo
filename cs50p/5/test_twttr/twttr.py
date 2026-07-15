def main():
    usr_input = input("Input: ")
    print("Output:", omit_vowels(usr_input))

def omit_vowels(sentence):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    new = ""
    for c in sentence:
        if c not in vowels:
            new += c
    return new

if __name__ == "__main__":
    main()