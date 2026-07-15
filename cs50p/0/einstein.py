def main():
    m = int(input("m: "))
    e = calcE(m)
    print("e:" , e)

def calcE(mass):
    E = mass * pow(300000000 , 2)
    return E

main()