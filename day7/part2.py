from functools import cache
import time


@cache
def fuel_calculator(total_steps):
    acc_fuel = 0
    for i in range(total_steps + 1):
        acc_fuel += i
    return acc_fuel


if __name__ == '__main__':
    start_time = time.time()
    with open('input.txt') as f:
        lines = f.readlines()
        list_of_crabs_position = list(map(lambda x: int(x), lines[0].split(",")))
        max_number = max(list_of_crabs_position)
        min_number = min(list_of_crabs_position)
        less_fuel = 99999999999999
        list_of_fuels = []
        previous_fuel = 0
        for pos1 in range(min_number, max_number + 1):
            total_fuel = 0
            for pos2 in list_of_crabs_position:
                fuel_used = fuel_calculator(abs(pos1 - pos2))
                total_fuel += fuel_used
            if total_fuel < less_fuel:
                less_fuel = total_fuel
        print(less_fuel)
    f.close()
    print("--- %s seconds ---" % (time.time() - start_time))