def main():
    dial = 50
    zero_count = 0

    with open("input.txt", "r") as file:
        data = file.read().strip().splitlines()

    for line in data:
        direction = line[0]
        value = int(line[1:])

        if direction == 'L':
            zero_count += ((100 - dial) % 100 + value) // 100
            dial = (dial - value) % 100
        elif direction == 'R':
            zero_count += (dial + value) // 100
            dial = (dial + value) % 100
        else:
            raise ValueError(f"Invalid direction: {direction}")
        
    print(dial)
    print(zero_count)

if __name__ == "__main__":
    main()