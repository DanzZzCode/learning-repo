import csv
import sys
from tabulate import tabulate

def main():

    items = []
    check_arguments()

    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                items.append(row)

    except FileNotFoundError:
        sys.exit("File does not exist")

    print(tabulate(items, headers="keys", tablefmt="grid"))

def check_arguments():

    args = len(sys.argv)

    if args > 2:
        sys.exit("Too many command-line arguments")
    elif args < 2:
        sys.exit("Too few command-line arguments")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file") 


if __name__ == "__main__":
    main()