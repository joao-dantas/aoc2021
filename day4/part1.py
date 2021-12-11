class BingoParticipant:
    board = {}
    rounds_to_win = 0
    win_num = 0
    already_won = False

    def __init__(self):
        self.rounds_to_win = 0
        self.win_num = 0
        self.board = {}


def check_participant(participant_checked):
    if participant_checked.board:
        for current_round, sel_num in enumerate(selected_numbers):
            if participant_checked.already_won is False:
                for key in participant_checked.board:
                    for i, x in enumerate(participant_checked.board[key]):
                        if x == sel_num:
                            participant_checked.board[key][i] = participant_checked.board[key][i] * (-1)
                    if all(elem < 0 for elem in participant_checked.board[key]):
                        participant_checked.already_won = True
                        participant_checked.rounds_to_win = current_round
                        participant_checked.win_num = sel_num
            else:
                continue
    return participant_checked


if __name__ == '__main__':
    with open('example_input.txt') as f:
        selected_numbers = {}
        current_read_index = 0
        current_board_line = 0
        participant = BingoParticipant()
        winner = BingoParticipant()
        best_rounds_to_win = 99999
        while True:
            file_line = f.readline()
            if not file_line:
                break
            file_line = file_line.strip()
            # print file_line
            if current_read_index == 0:
                selected_numbers = map(int, file_line.split(','))
            elif file_line != '':
                line = map(int, file_line.replace("  ", " ").split(" "))
                participant.board["l" + str(current_board_line)] = line
                for col_idx in range(5):
                    if "c" + str(col_idx) not in participant.board:
                        participant.board["c" + str(col_idx)] = [
                            participant.board["l" + str(current_board_line)][col_idx]]
                    else:
                        participant.board["c" + str(col_idx)].append(
                            participant.board["l" + str(current_board_line)][col_idx])
                current_board_line += 1
                if len(participant.board) == 10:
                    participant = check_participant(participant)
                    if participant.already_won and participant.rounds_to_win < best_rounds_to_win:
                        winner = participant
                        best_rounds_to_win = participant.rounds_to_win
            else:
                participant = BingoParticipant()
                current_board_line = 0
            current_read_index += 1

        total_unmarked = 0
        for key in winner.board:
            for num in winner.board[key]:
                if num >= 0:
                    total_unmarked += num
        print (total_unmarked / 2) * winner.win_num
        f.close()
