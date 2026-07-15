def main():
    usrin = input("Please enter your sentence: ")
    usrin = convert(usrin)
    print(usrin)

def convert(text):
    text = text.replace(':)' , "🙂")
    text = text.replace(':(' , "🙁")
    return text

main()