# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
        x_pos = 0
        y_pos = 0
        aim = 0
        for command in lines:
            splitted = command.split(" ")
            action = splitted[0]
            size = int(splitted[1])
            if action == "forward":
                x_pos += size
                y_pos += aim * size
            elif action == "down":
                aim += size
            elif action == "up":
                aim -= size
        print(x_pos * y_pos)
