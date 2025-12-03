from itertools import batched

def main():
    with open("input.txt", "r") as infile:
        ranges = infile.read().strip().split(',')

    s = 0

    for r in ranges:
        start, end = map(int, r.split('-'))
        for num in range(start, end + 1):
            numstr = str(num)
            if len(numstr) % 2 != 0:
                continue

            p1 = numstr[:len(numstr)//2]
            p2 = numstr[len(numstr)//2:]
            if p1 == p2:
                s += num

    print(s)

if __name__ == "__main__":
    main()