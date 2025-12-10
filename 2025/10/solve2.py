# does not work now, needs to be optimized

from tqdm import tqdm

def parse_line(line: str) -> tuple[tuple[bool, ...], tuple[frozenset[int], ...], tuple[int, ...]]:
    right_middle_brace = line.index("]")
    left_curly_brace = line.index("{")

    light_req = tuple(x == '#' for x in line[1:right_middle_brace])
    buttons = tuple(sorted((frozenset(int(i) for i in x[1:-1].split(',')) for x in line[right_middle_brace + 2:left_curly_brace - 1].split()), key=len, reverse=True))
    voltage_req = tuple(int(x) for x in line[left_curly_brace + 1:-2].split(','))

    return light_req, buttons, voltage_req

def modify_voltages(voltage_reqs: tuple[int, ...], button: frozenset[int], times: int = 1) -> tuple[int, ...]:
    new_voltages = list(voltage_reqs)
    for index in button:
        new_voltages[index] -= times
    return tuple(new_voltages)

def max_clicks(voltage_reqs: tuple[int, ...], button: frozenset[int]) -> int:
    return min(voltage_reqs[i] for i in button)

# memory = {}

def fewest_to_voltages(voltage_reqs: tuple[int, ...], buttons: tuple[frozenset[int], ...]) -> int:
    if all(x == 0 for x in voltage_reqs):
        return 0
    
    if any(x < 0 for x in voltage_reqs) or len(buttons) <= 0:
        return 999999999
    
    # if (voltage_reqs, buttons) in memory:
        # return memory[(voltage_reqs, buttons)]
    
    if len(buttons) == 1:
        button = buttons[0]
        cnt = voltage_reqs[next(button.__iter__())]
        for i, v in enumerate(voltage_reqs):
            if (v > 0 and i not in button) or v != cnt:
                # memory[(voltage_reqs, buttons)] = 999999999
                return 999999999
            
        # memory[(voltage_reqs, buttons)] = cnt
        return cnt
    
    if any(v > 0 and not any(i in b for b in buttons) for i, v in enumerate(voltage_reqs)):
        return 999999999
    
    button_with_cnts = tuple(x for x in ((max_clicks(voltage_reqs, b), b) for b in buttons) if x[0] > 0)
    if len(button_with_cnts) <= 0:
        return 999999999
    buttons = tuple(x[-1] for x in button_with_cnts)

    min_cnt = max(voltage_reqs)
    result = 999999999
    print(voltage_reqs, buttons)
    for max_click, button in button_with_cnts:
        broken = False
        new_buttons = tuple(b for b in buttons if b != button)
        for i in range(max_click, 0, -1):
            new_voltages = modify_voltages(voltage_reqs, button, i)
            cnt = fewest_to_voltages(new_voltages, new_buttons) + 1
            if cnt < result:
                result = cnt
                if result <= min_cnt:
                    broken = True
                    break

        if broken:
            break


    # memory[(voltage_reqs, buttons)] = result
    return result
    

def main():
    with open("input.txt", "r") as infile:
        machines = [parse_line(line) for line in infile.readlines()]

    print(sum(fewest_to_voltages(voltage_reqs, buttons) for _, buttons, voltage_reqs in tqdm(machines)))

if __name__ == "__main__":
    main()