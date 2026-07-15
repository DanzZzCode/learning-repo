def main():
    while True:
        try:
            date = input("Date: ")
            if not validate(date):
                raise ValueError
        except ValueError:
            pass
        else:
            print_date(date)
            break

def validate(usr_input):
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

    if "/" in usr_input:
        try:
            parts = usr_input.split('/')
            month = int(parts[0])
            day = int(parts[1])
            year = int(parts[2])
            if 1 <= month <= 12 and 1 <= day <= 31 and 0 <= year <= 9999:
                return True
        except (ValueError , IndexError):
            return False
    elif "," in usr_input:
        try:
            clean = usr_input.replace("," , "")
            parts = clean.split(" ")
            month = parts[0].title()
            day = int(parts[1])
            year = int(parts [2])
            if month in months and 1 <= day <= 31 and 0 <= year <= 9999:
                return True
        except (ValueError , IndexError):
            return False
    return False

def print_date(usr_input):
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

    if "/" in usr_input:
        parts = usr_input.split("/")
        month = int(parts[0])
        day = int(parts[1])
        year = int(parts[2])

    else:
        clean = usr_input.replace("," , "").split(" ") 
        month = months.index(clean[0].title()) + 1
        day = int(clean[1])
        year = int(clean[2])

    print(f"{year:04d}-{month:02d}-{day:02d}")

main()