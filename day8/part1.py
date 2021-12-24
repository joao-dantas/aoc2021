# ZERO = [1, 1, 1, 0, 1, 1, 1]  # uses 6 segments
# ONE = [0, 0, 1, 0, 0, 1, 0]  # only digit with two segments
# TWO = [1, 0, 1, 1, 1, 0, 1]  # uses 5 segments
# THREE = [1, 0, 1, 1, 1, 0, 1]  # uses 5 segments
# FOUR = [0, 1, 1, 1, 0, 1, 0]  # only digit with four segments
# FIVE = [1, 1, 0, 1, 0, 1, 1]  # uses 5 segments
# SIX = [1, 1, 0, 1, 1, 1, 1]  # uses 6 segments
# SEVEN = [1, 0, 1, 0, 0, 1, 0]  # only digit with three segments
# EIGHT = [1, 1, 1, 1, 1, 1, 1]  # only digit with seven segments
# NINE = [1, 1, 1, 1, 0, 1, 1]  # uses 6 segments
#
#
def check_signal(s):
    if len(s) == 7:
        print(s + " is an eight")
        return 8
    elif len(s) == 2:
        print(s + " is a one")
        return 1
    elif len(s) == 4:
        print(s + " is a four")
        return 4
    elif len(s) == 3:
        print(s + " is a seven")
        return 7
    else:
        return 0


if __name__ == '__main__':
    with open('input.txt') as f:
        sum_of_digits = 0
        while True:
            file_line = f.readline()
            if not file_line:
                break
            file_line = file_line.strip()
            parts = file_line.split(" | ")
            signals = parts[0].split(" ")
            numbers = parts[1].split(" ")
            for number in numbers:
                if check_signal(number) > 0:
                    sum_of_digits += 1
        print(sum_of_digits)
    f.close()
