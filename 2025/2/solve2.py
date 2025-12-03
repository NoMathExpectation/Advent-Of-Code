from itertools import batched

def main():
    with open("input.txt", "r") as infile:
        ranges = infile.read().strip().split(',')

    s = 0

    for r in ranges:
        start, end = map(int, r.split('-'))
        for num in range(start, end + 1):
            numstr = str(num)
            for c in range(1, len(numstr) // 2 + 1):
                if len(numstr) % c != 0:
                    continue

                parts = list(batched(numstr, c))
                example = parts[0]
                if all(p == example for p in parts):
                    s += num
                    break

    print(s)

if __name__ == "__main__":
    main()