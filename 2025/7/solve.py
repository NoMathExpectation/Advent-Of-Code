def main():
    with open("input.txt", "r") as infile:
        lines = [list(line) for line in infile.readlines()]

    def cast(row: int, col: int):
        if col < 0 or col >= len(lines[0]):
            return

        while row < len(lines):
            symbol = lines[row][col]
            if symbol == "|":
                return

            if symbol == "^":
                cast(row + 1, col - 1)
                cast(row + 1, col + 1)
                return

            lines[row][col] = "|"
            row += 1

    start = lines[0].index("S")
    cast(0, start)

    cnt = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "^" and lines[i - 1][j] == "|":
                cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
