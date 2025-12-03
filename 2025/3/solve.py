def main():
    with open("input.txt", "r") as infile:
        battery_banks = infile.read().strip().splitlines()

    s = 0
    for bank in battery_banks:
        capacities = list(map(int, bank))
        max_ten_idx = 0
        for i in range(len(capacities) - 1):
            if capacities[i] > capacities[max_ten_idx]:
                max_ten_idx = i

        max_one_idx = max_ten_idx + 1
        for i in range(max_ten_idx + 1, len(capacities)):
            if capacities[i] > capacities[max_one_idx]:
                max_one_idx = i

        s += capacities[max_ten_idx] * 10 + capacities[max_one_idx]

    print(s)

    

if __name__ == "__main__":
    main()