import random

def main():
    print(reminder())
    new_reminder()

def reminder():
    with open("reminders.txt", "r", encoding="utf-8") as fhand:
        lst = list()
        for item in fhand:
            if item.strip(): 
                lst.append(item)
    
    # Safety check: If the file exists but has nothing inside it yet
    if not lst:
        return "No reminders found! Add one below."
        
    random.shuffle(lst)
    return construct(lst[0])

def new_reminder():
    reminder = input("Would you like to add a new reminder? ")
    if reminder == "n":
        quit()
    else:
        # Extra safety: Don't let users accidentally save a purely blank reminder
        if not reminder.strip():
            print("Skipped saving because the input was empty.")
            return
            
        with open("reminders.txt", "a", encoding="utf-8") as file:
            file.write(reminder + "\n")

def construct(x):
    clean_reminder = x.rstrip()
    boarder = "#" * (len(clean_reminder) + 4)
    output = f"\n{boarder}\n# {clean_reminder} #\n{boarder}\n"
    return output

if __name__ == "__main__":
    main()
