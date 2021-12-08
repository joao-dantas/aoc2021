def check_winner(board):
    for line in board:
        if all(num == -1 for (num) in line) is True:
            return True
    for i in range(5):
        if board[0][i] == -1 and board[1][i] == -1 and board[2][i] == -1 and board[3][i] == -1 and board[4][i] == -1:
            return True
    return False


def get_sum_unmarked(board):
    total_unmarked = 0
    for line in board:
        filtered_line = filter(lambda x: x > 0, line)
        for item in filtered_line:
            total_unmarked += int(item)
    return total_unmarked


def process_boards(bingo_boards, number_selected):
    for board in bingo_boards:
        for line in board:
            for idx, num in enumerate(line):
                if num == number_selected:
                    line[idx] = -1
                    if check_winner(board):
                        total_unmarked = get_sum_unmarked(board)
                        print number_selected
                        print total_unmarked
                        print int(number_selected) * total_unmarked
                        return True
    return False

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
        f.close()
        new_board = []
        boards = []
        current_read_index = 0
        while current_read_index < len(lines):
            if current_read_index == 0:
                selected_numbers = lines[current_read_index].strip().split(",")
            elif lines[current_read_index] == "\n":
                boards.append(new_board)
                new_board = []
            else:
                new_board.append(lines[current_read_index].strip().replace("  ", " ").split(" "))
            current_read_index += 1
        boards.append(new_board)

        for selected in selected_numbers:
            if process_boards(boards, selected) is True:
                break
