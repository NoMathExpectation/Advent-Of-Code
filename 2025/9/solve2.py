import itertools


def area(a, b) -> int:
    return (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)


def line_crossed_rectangle_inside(
    line: tuple[tuple[int, ...], tuple[int, ...]],
    min_x: int,
    max_x: int,
    min_y: int,
    max_y: int,
) -> bool:
    if any(min_x < x < max_x and min_y < y < max_y for x, y in line):
        return True

    (ax, ay), (bx, by) = line
    line_min_x = min(ax, bx)
    line_max_x = max(ax, bx)
    line_min_y = min(ay, by)
    line_max_y = max(ay, by)
    if ax == bx:
        return min_x < ax < max_x and not (line_max_y <= min_y or line_min_y >= max_y)
    else:
        return min_y < ay < max_y and not (line_max_x <= min_x or line_min_x >= max_x)


def main():
    with open("input.txt", "r") as infile:
        coords = [
            tuple(map(int, line.strip().split(","))) for line in infile.readlines()
        ]

    lines = list(itertools.pairwise(coords))
    lines += [(coords[-1], coords[0])]

    def rectangle_is_inside(a, b) -> bool:
        # print("Checking", a, b)

        min_x = min(a[0], b[0])
        max_x = max(a[0], b[0])
        min_y = min(a[1], b[1])
        max_y = max(a[1], b[1])

        if any(
            line_crossed_rectangle_inside(line, min_x, max_x, min_y, max_y)
            for line in lines
        ):
            return False

        # print("Double Checking", a, b)
        crossed_lines = sorted(
            (
                line
                for line in lines
                if line[0][1] == line[1][1]
                and 0 < line[0][1] <= min_y
                and (line[0][0] - min_x) * (line[1][0] - min_x) <= 0
            ),
            key=lambda l: l[0][1],
        )
        # print(crossed_lines)

        # print("Crossed Lines:", crossed_lines)
        idx = 0
        while idx < len(crossed_lines) - 1:
            l1 = crossed_lines[idx]
            l2 = crossed_lines[idx + 1]
            if l1[1][0] != l2[0][0]:
                idx += 1
                continue

            if (l1[0][0] - min_x) * (l2[1][0] - min_x) > 0:
                crossed_lines.pop(idx)
                crossed_lines.pop(idx)
                continue

            crossed_lines.pop(idx + 1)
            idx += 1

        return len(crossed_lines) % 2 != 0

    combines = itertools.combinations(coords, 2)

    max_area = max((area(a, b), a, b) for a, b in combines if rectangle_is_inside(a, b))

    print(max_area)


if __name__ == "__main__":
    main()
