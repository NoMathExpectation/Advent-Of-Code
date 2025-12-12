def parse_input(text: str) -> tuple[list[list[list[bool]]], list[tuple[tuple[int, int], list[int]]]]:
    presents_text, regions_text = text.strip().rsplit("\n\n", 1)

    presents: list[list[list[bool]]] = []
    for lines in presents_text.split("\n\n")[1:]:
        present: list[list[bool]] = []
        for line in lines.split("\n"):
            row = [x == '#' for x in line.strip()]
            present.append(row)
        presents.append(present)

    regions: list[tuple[tuple[int, int], list[int]]] = []
    for line in regions_text.strip().split("\n"):
        size_text, present_counts_text = line.split(":")
        x_length, y_length = map(int, size_text.split("x"))
        present_counts = [int(x) for x in present_counts_text.strip().split()]
        regions.append(((x_length, y_length), present_counts))

    return presents, regions

def main():
    with open("input.txt", "r") as infile:
        presents, regions = parse_input(infile.read())

    

if __name__ == "__main__":
    main()