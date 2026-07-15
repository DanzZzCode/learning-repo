def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not punc(s):
        return False
    if not start_letters(s):
        return False
    if not len_cor(s):
        return False
    if not num_mid(s):
        return False
    
    return True

def punc(letters_set):
    for c in letters_set:
        if not c.isalnum():
            return False
    return True

def start_letters(letters_set):
    if len(letters_set) < 2:
        return False
    return letters_set[0:2].isalpha()

def len_cor(letters_set):
    return 6 >= len(letters_set) >= 2

def num_mid(letters_set):
    had_num = False
    for c in letters_set:
        if c == '0' and had_num == False:
            return False
        if c.isdigit():
            had_num = True
        if c.isalpha() and had_num == True:
            return False
    return True


main()