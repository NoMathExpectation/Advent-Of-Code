# less optimized one, too slow to work
def main():
    outputs: dict[str, list[str]] = {}
    with open("input.txt", "r") as infile:
        for line in infile.readlines():
            key, value = line.strip().split(":")
            outputs[key] = value.strip().split(" ")

    memory: dict[tuple[str, str], list[list[str]]] = {}

    def paths(start: str, end: str) -> list[list[str]]:
        if start == end:
            return [[end]]

        if (start, end) in memory:
            return memory[(start, end)]

        print("cache miss", start, end)

        all_paths: list[list[str]] = []
        for dest in outputs.get(start, []):
            for path in paths(dest, end):
                all_paths.append([start] + path)

        memory[(start, end)] = all_paths
        return all_paths

    print(
        len(
            [
                path
                for path in paths("svr", "out")
                if all(x in path for x in ["dac", "fft"])
            ]
        )
    )


if __name__ == "__main__":
    main()
