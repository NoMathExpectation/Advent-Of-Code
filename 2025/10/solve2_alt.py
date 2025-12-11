import numpy as np
from scipy.optimize import linprog
from tqdm import tqdm


def parse_line(
    line: str,
) -> tuple[tuple[bool, ...], tuple[frozenset[int], ...], tuple[int, ...]]:
    line = line.strip()
    right_middle_brace = line.index("]")
    left_curly_brace = line.index("{")

    light_req = tuple(x == "#" for x in line[1:right_middle_brace])
    buttons = tuple(
        sorted(
            (
                frozenset(int(i) for i in x[1:-1].split(","))
                for x in line[right_middle_brace + 2 : left_curly_brace - 1].split()
            ),
            key=len,
            reverse=True,
        )
    )
    voltage_req = tuple(int(x) for x in line[left_curly_brace + 1 : -1].split(","))

    return light_req, buttons, voltage_req


def fewest_to_voltages(
    voltage_reqs: tuple[int, ...], buttons: tuple[frozenset[int], ...]
) -> int:
    c = np.ones(len(buttons))
    a_eq = []
    for button in buttons:
        row = [1 if i in button else 0 for i in range(len(voltage_reqs))]
        a_eq.append(row)
    a_eq = np.array(a_eq).T
    b_eq = np.array(voltage_reqs)

    result = linprog(c, A_eq=a_eq, b_eq=b_eq, integrality=1)
    if not result.success:
        raise ValueError("Linear programming failed for", voltage_reqs, buttons)

    return int(sum(result.x))


def main():
    with open("input.txt", "r") as infile:
        machines = [parse_line(line) for line in infile.readlines()]

    print(
        sum(
            fewest_to_voltages(voltage_reqs, buttons)
            for _, buttons, voltage_reqs in tqdm(machines)
        )
    )


if __name__ == "__main__":
    main()
