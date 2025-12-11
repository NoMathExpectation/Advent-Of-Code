def main():
    outputs: dict[str, list[str]] = {}
    with open("input.txt", "r") as infile:
        for line in infile.readlines():
            key, value = line.strip().split(":")
            outputs[key] = value.strip().split(" ")

    memory: dict[tuple[str, str], int] = {}

    def paths_cnt(start: str, end: str) -> int:
        if start == end:
            return 1

        if (start, end) in memory:
            return memory[(start, end)]

        cnt = 0
        for dest in outputs.get(start, []):
            cnt += paths_cnt(dest, end)

        memory[(start, end)] = cnt
        return cnt

    print(
        paths_cnt("svr", "dac") * paths_cnt("dac", "fft") * paths_cnt("fft", "out")
        + paths_cnt("svr", "fft") * paths_cnt("fft", "dac") * paths_cnt("dac", "out")
    )


if __name__ == "__main__":
    main()
