def main():
    with open("input.txt", "r") as infile:
        mat = list(map(list, infile.read().strip().splitlines()))

    last_cnt = 0
    cnt = 0
    while True:
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] != "@":
                    continue

                adjs = (
                    (i - 1, j - 1),
                    (i - 1, j),
                    (i - 1, j + 1),
                    (i, j - 1),
                    (i, j + 1),
                    (i + 1, j - 1),
                    (i + 1, j),
                    (i + 1, j + 1),
                )
                c = 0

                for x, y in adjs:
                    if x < 0 or x >= len(mat) or y < 0 or y >= len(mat[i]):
                        continue

                    if mat[x][y] == "@":
                        c += 1

                if c < 4:
                    cnt += 1
                    mat[i][j] = "."

        if cnt == last_cnt:
            break
        last_cnt = cnt

    print(cnt)


if __name__ == "__main__":
    main()
