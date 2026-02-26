def main():
    mass = int(input("m: "))
    energy = convertEnergy(mass)
    print(f"E: {energy}")

def convertEnergy(mass):
    return mass * 300000000 ** 2

main()
