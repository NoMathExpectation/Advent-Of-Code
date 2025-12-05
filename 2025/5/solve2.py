def parse_range(line) -> tuple[int, int]:
    start, stop = line.split("-")
    return (int(start), int(stop))


def merge_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    ranges.sort()
    current_idx = 0
    while current_idx < len(ranges) - 1:
        cmin, cmax = ranges[current_idx]
        nmin, nmax = ranges[current_idx + 1]
        if not (cmax < nmin or cmin > nmax):
            new_min = min(cmin, nmin)
            new_max = max(cmax, nmax)
            ranges[current_idx] = (new_min, new_max)
            del ranges[current_idx + 1]
        else:
            current_idx += 1

    return ranges


def main():
    with open("input.txt", "r") as infile:
        lines = infile.readlines()

    split_idx = lines.index("\n")
    fresh_ranges = list(map(parse_range, lines[:split_idx]))

    no_overlap_ranges = merge_ranges(fresh_ranges)
    print(sum(b - a + 1 for a, b in no_overlap_ranges))


if __name__ == "__main__":
    main()
