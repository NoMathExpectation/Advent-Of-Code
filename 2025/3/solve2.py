def main():
    with open("input.txt", "r") as infile:
        battery_banks = infile.read().strip().splitlines()

    s = 0
    for bank in battery_banks:
        voltage = 0
        capacities = list(map(int, bank))

        last_digit_idx = -1
        for d in range(11, -1, -1):
            max_digit_idx = last_digit_idx + 1
            for i in range(last_digit_idx + 1, len(capacities) - d):
                if capacities[i] > capacities[max_digit_idx]:
                    max_digit_idx = i

            voltage = voltage * 10 + capacities[max_digit_idx]
            last_digit_idx = max_digit_idx

        s += voltage

    print(s)

    

if __name__ == "__main__":
    main()