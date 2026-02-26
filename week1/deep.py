def main():
    str = input("What is the answer to the Great Question of Life, The Universe, and Everything? ")
    print(isFourtyTwo(str))

def isFourtyTwo(str):
    str = str.strip().lower()
    if str == "forty two" or str == "forty-two" or str == "42":
        return 'Yes'
    else:
        return 'No'

main()
