def main():
    with open("input.txt", "r") as infile:
        lines = [list(line) for line in infile.readlines()]

    memory = {}

    def cast(row: int, col: int) -> int:
        if col < 0 or col >= len(lines[0]):
            return 0

        while row < len(lines):
            symbol = lines[row][col]

            if (row, col) in memory:
                return memory[(row, col)]

            if symbol == "^":
                result = cast(row + 1, col - 1) + cast(row + 1, col + 1)
                memory[(row, col)] = result
                return result

            row += 1

        return 1

    start = lines[0].index("S")
    cnt = cast(0, start)

    print(cnt)


if __name__ == "__main__":
    main()
