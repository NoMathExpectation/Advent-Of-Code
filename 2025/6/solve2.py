import numpy as np


def main():
    with open("input.txt", "r") as infile:
        mat = infile.readlines()

    opline = mat[-1]
    split_idxs = [i for i, c in enumerate(opline) if c in "+*"]
    split_idxs = split_idxs + [len(opline) + 1]
    new_mat = []
    for line in mat:
        new_row = []
        for i in range(len(split_idxs) - 1):
            start = split_idxs[i]
            end = split_idxs[i + 1] - 1
            new_row.append(line[start:end])
        new_mat.append(new_row)
    mat = new_mat

    mat = np.array(mat).transpose()

    s = 0
    for row in mat:
        op = row[-1].strip()
        row = row[:-1]

        max_len = max(len(x) for x in row)
        row = np.array([list(x + " " * (max_len - len(x))) for x in row]).transpose()
        row = np.array(list(map(int, ["".join(x) for x in row])))

        if op == "+":
            s += row.sum()
        elif op == "*":
            s += row.prod()
        else:
            raise ValueError(f"Unknown operation: {op}")

    print(s)


if __name__ == "__main__":
    main()
