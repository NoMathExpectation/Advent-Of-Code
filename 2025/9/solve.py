import itertools


def area(a, b) -> int:
    return (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)

def main():
    with open("input.txt", "r") as infile:
        coords = [tuple(map(int, line.strip().split(','))) for line in infile.readlines()]

    combines = itertools.combinations(coords, 2)

    max_area = max(area(a, b) for a, b in combines)

    print(max_area)

if __name__ == "__main__":
    main()