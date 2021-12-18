from functools import cache


@cache
def process_lanternfish_lifecycle(days_left, current_age):
    family = 1
    for d in range(days_left, 0, -1):
        if current_age == 0:
            family += process_lanternfish_lifecycle(d, 9)
            current_age = 6
        else:
            current_age -= 1

    return family


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
        days = 256
        list_of_ages = map(lambda x: int(x), lines[0].split(","))
        list_of_lanterfishes = 0
        for age in list_of_ages:
            list_of_lanterfishes += process_lanternfish_lifecycle(days, age)
        print("Total: " + str(list_of_lanterfishes))
    f.close()
