import heapq

INPUT_FILE = "input.in"

def main():
    list1 = []
    list2 = []
    with open(INPUT_FILE, 'r') as file:
        for line in file:
            num1, num2 = line.split()
            list1.append(int(num1))
            list2.append(int(num2))

    difference = 0

    heapq.heapify(list1)
    heapq.heapify(list2)

    while list1:
        num1 = heapq.heappop(list1)
        num2 = heapq.heappop(list2)
        difference += abs(num1 - num2)

    print(difference)






if __name__ == "__main__":
    main()