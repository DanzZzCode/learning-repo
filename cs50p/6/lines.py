import sys
import os

def main():

    check_args()
    file_name = sys.argv[1]

    try:
        with open(file_name, "r") as file:
            line_count = 0
            for line in file:
                is_code_line(line)
                line_count += 1
            print(line_count)

    except FileNotFoundError:
        sys.exit("file does not exist.")

def is_code_line(line):
    striped_line = line.lstrip()

    if not striped_line:
        return False

    if striped_line.startswith("#"):
        return False

    return True

def check_args():
    if len(sys.argv) < 2:
        sys.exit("Too few command line arguments.")
    
    elif len(sys.argv) > 2:
        sys.exit("Too many command line arguments.")

    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a python file.")

if __name__ == "__main__":
    main()
