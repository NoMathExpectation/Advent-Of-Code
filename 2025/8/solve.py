import itertools


def distance_squared(a, b) -> int:
    return sum((a[i] - b[i]) ** 2 for i in range(3))


def main():
    with open("input.txt", "r") as infile:
        coords = [tuple(int(x) for x in line.split(",")) for line in infile.readlines()]

    combines = sorted(
        itertools.combinations(coords, 2),
        key=lambda pair: distance_squared(pair[0], pair[1]),
    )
    circuits = [[x] for x in coords]
    total = 1000
    for a, b in combines[:total]:
        circuit_a = next(c for c in circuits if a in c)
        circuit_b = next(c for c in circuits if b in c)
        if circuit_a is circuit_b:
            continue

        circuits.remove(circuit_b)
        circuit_a.extend(circuit_b)

    circuits.sort(key=len, reverse=True)
    print(len(circuits[0]) * len(circuits[1]) * len(circuits[2]))


if __name__ == "__main__":
    main()
