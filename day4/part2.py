def process(list_of_numbers, evaluate_most_common, idx):
    ones_list = []
    zeros_list = []
    if len(list_of_numbers) == 1:
        return int("0b" + list_of_numbers[0], 2)
    for item in list_of_numbers:
        if item[idx] == "0":
            zeros_list.append(item)
        else:
            ones_list.append(item)

    if len(ones_list) > len(zeros_list):
        if evaluate_most_common:
            return process(ones_list, evaluate_most_common, idx + 1)
        else:
            return process(zeros_list, evaluate_most_common, idx + 1)
    elif len(ones_list) < len(zeros_list):
        if evaluate_most_common:
            return process(zeros_list, evaluate_most_common, idx + 1)
        else:
            return process(ones_list, evaluate_most_common, idx + 1)
    elif evaluate_most_common:
        return process(ones_list, evaluate_most_common, idx + 1)
    else:
        return process(zeros_list, evaluate_most_common, idx + 1)


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
        f.close()
    oxygen_generator_rating = process(lines, True, 0)
    co2_scrubber_rating = process(lines, False, 0)
    print(oxygen_generator_rating * co2_scrubber_rating)
