import sys
import csv

def main():
    validate_args()

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    cleaned_students = []

    try:
        with open(input_file, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                last, first = row["name"].split(",")
                first = first.strip()
                last = last.strip()

                cleaned_students.append(

                    {"first": first, "last": last, "house": row["house"]}
                )

    except FileNotFoundError:
        sys.exit("File does not exist")

    with open(output_file, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        writer.writerows(cleaned_students)
            

def validate_args():

    args = len(sys.argv)

    if args > 3:
        sys.exit("Too many command-line arguments")
    elif args < 3:
        sys.exit("Too few command-line arguments")

    if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()