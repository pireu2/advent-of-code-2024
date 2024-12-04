

INPUT_FILE = "input.in"

def main():
    list1 = []
    list2 = []
    with open(INPUT_FILE, 'r') as file:
        for line in file:
            num1, num2 = line.split()
            list1.append(int(num1))
            list2.append(int(num2))

    frequency = {num: list2.count(num) for num in set(list2)}

    s = 0

    for num in list1:
        freq = 0
        try:
            freq = frequency[num] 
        except KeyError:
            pass
        s += num * freq

    print(s)





if __name__ == "__main__":
    main()