if __name__ == '__main__':
    with open('input.txt') as f:
        control_array = []
        while True:
            line = f.readline()
            if not line:
                break
            line = line.strip()
            for idx in range(len(line)):
                if len(control_array) <= idx:
                    control_array.append("0")
                if line[idx] == '0':
                    control_array[idx] = int(control_array[idx]) - 1
                elif line[idx] == '1':
                    control_array[idx] = int(control_array[idx]) + 1
            gamma_string = "0b"
            epsilon_string = "0b"
            for idx in range(len(control_array)):
                if int(control_array[idx]) > 0:
                    gamma_string += "1"
                    epsilon_string += "0"
                else:
                    gamma_string += "0"
                    epsilon_string += "1"
            gama = int(gamma_string, 2)
            epsilon = int(epsilon_string, 2)
        print(gama * epsilon)

        f.close()