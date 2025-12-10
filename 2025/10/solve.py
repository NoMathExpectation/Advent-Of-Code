def parse_line(line: str) -> tuple[tuple[bool, ...], list[set[int]], list[int]]:
    right_middle_brace = line.index("]")
    left_curly_brace = line.index("{")

    light_req = tuple(x == '#' for x in line[1:right_middle_brace])
    buttons = [set(int(i) for i in x[1:-1].split(',')) for x in line[right_middle_brace + 2:left_curly_brace - 1].split()]
    voltage_req = [int(x) for x in line[left_curly_brace + 1:-2].split(',')]

    return light_req, buttons, voltage_req

def modify_lights(light_now: tuple[bool, ...], button: set[int]) -> tuple[bool, ...]:
    new_lights = list(light_now)
    for index in button:
        new_lights[index] = not new_lights[index]
    return tuple(new_lights)

def fewest_to_light(light_req: tuple[bool, ...], buttons: list[set[int]]) -> int:
    if all(not x for x in light_req):
        return 0

    lights_nows = set([tuple([False] * len(light_req))])

    cnt = 0
    while True:
        cnt += 1
        next_lights_nows: set[tuple[bool, ...]] = set()
        for light_now in lights_nows:
            for button in buttons:
                new_lights = modify_lights(light_now, button)
                if new_lights == light_req:
                    return cnt
                next_lights_nows.add(new_lights)
        lights_nows = next_lights_nows
    

def main():
    with open("input.txt", "r") as infile:
        machines = [parse_line(line) for line in infile.readlines()]

    print(sum(fewest_to_light(light_req, buttons) for light_req, buttons, _ in machines))

if __name__ == "__main__":
    main()