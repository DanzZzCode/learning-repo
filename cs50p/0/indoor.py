def main ():
        userin = input("Please write your sentence: ")
        userin = lowerCase(userin)
        print(userin)

def lowerCase (sentence):
        sentence = sentence.lower()
        return sentence

main ()