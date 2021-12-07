def process(list_of_numbers, evaluate_most_common, idx):
    ones_list = []
    zeros_list = []
    if len(list_of_numbers) == 1:
        return "0b" + list_of_numbers[0]
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
        initial_ones_list = []
        initial_zeros_list = []
        initial_idx = 0
        lines = f.readlines()

        for line in lines:
            line = line.strip()
            if line[initial_idx] == "0":
                initial_zeros_list.append(line)
            else:
                initial_ones_list.append(line)
        f.close()

        if len(initial_ones_list) >= len(initial_zeros_list):
            oxygen_generator_rating_binary = process(initial_ones_list, True, initial_idx + 1)
            co2_scrubber_rating_binary = process(initial_zeros_list, False, initial_idx + 1)
        else:
            oxygen_generator_rating_binary = process(initial_zeros_list, True, initial_idx + 1)
            co2_scrubber_rating_binary = process(initial_ones_list, False, initial_idx + 1)
        oxygen_generator_rating = int(oxygen_generator_rating_binary, 2)
        co2_scrubber_rating = int(co2_scrubber_rating_binary, 2)
        print(oxygen_generator_rating * co2_scrubber_rating)
