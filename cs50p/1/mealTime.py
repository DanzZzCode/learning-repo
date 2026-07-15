def main():
    time_input = input("What time is it? ").strip()
    decimal_hours = convert(time_input)

    if 7.0 <= decimal_hours <= 8.0:
        print("breakfast time")
    if 12.0 <= decimal_hours <= 13.0:
        print("lunch time")
    if 18.0 <= decimal_hours <= 19.0:
        print("dinner time")

def convert(time):
  hours , minutes = time.split(":")
  return float(hours) + (float(minutes) / 60.0)

if __name__ == "__main__":
    main()