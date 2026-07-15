def main():
    calc_value()

def calc_value():
	price = 50
	while price > 0:
		print("Amount Due:" , price)
		coin = int(input("Insert coin: "))
		if coin in [25, 10, 5]:
			price = price - coin
		
	print("Change owed:" , price * -1)

main()