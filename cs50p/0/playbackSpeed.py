def main ():
    usrin = input("Please write your sentence: ")
    usrin = repl(usrin)
    print(usrin)

def repl (sentence):
    sentence = sentence.replace(' ' , '...')
    return sentence

main()