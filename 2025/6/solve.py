import numpy as np


def main():
    with open("input.txt", "r") as infile:
        mat = [line.strip().split() for line in infile.readlines()]

    mat = np.array(mat).transpose()

    s = 0
    for row in mat:
        op = row[-1]
        if op == "+":
            s += row[:-1].astype(int).sum()
        elif op == "*":
            s += row[:-1].astype(int).prod()

    print(s)


if __name__ == "__main__":
    main()
