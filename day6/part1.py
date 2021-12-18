import statistics

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
        list_of_crabs_position = list(map(lambda x: int(x), lines[0].split(",")))
        list_of_crabs_position.sort()
        less_steps = 999999
        for idx_i, pos1 in enumerate(list_of_crabs_position):
            total_steps = 0
            for idx_j, pos2 in enumerate(list_of_crabs_position):
                total_steps += abs(pos1 - pos2)
            if total_steps < less_steps:
                less_steps = total_steps
        print(less_steps)
    f.close()
