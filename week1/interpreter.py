def main():
    x, y, z = input("Expression: ").split()
    print(calculate(int(x), y, int(z)))


def calculate(int1, operator, int2):
    if operator == "+":
        return float(int1 + int2)
    elif operator == "-":
        return float(int1 - int2)
    elif operator == "*":
        return float(int1 * int2)
    else:
        return float(int1 / int2)

main()
