def parse_range(line):
    start, stop = line.split("-")
    return range(int(start), int(stop) + 1)

def main():
    with open("input.txt", "r") as infile:
        lines = infile.readlines()

    split_idx = lines.index("\n")
    fresh_ranges = list(map(parse_range, lines[:split_idx]))
    availables = list(map(int, lines[split_idx + 1:]))

    cnt = 0
    for i in availables:
        if any(i in r for r in fresh_ranges):
            cnt += 1

    print(cnt)

if __name__ == "__main__":
    main()