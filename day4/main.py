# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
        control_array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for diagnostic in lines:
            for idx in range(12):
                if diagnostic[idx] == '0':
                    control_array[idx] = control_array[idx] - 1
                elif diagnostic[idx] == '1':
                    control_array[idx] = control_array[idx] + 1
        gamma_string = "0b"
        epsilon_string = "0b"
        print(control_array)
        for idx in range(12):
            if int(control_array[idx]) > 0:
                gamma_string += "1"
                epsilon_string += "0"
            else:
                gamma_string += "0"
                epsilon_string += "1"
        gama = int(gamma_string, 2)
        epsilon = int(epsilon_string, 2)
        print(gama)
        print(epsilon)
        print(gama * epsilon)
