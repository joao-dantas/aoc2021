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
                for k in participant_checked.board:
                    for i, x in enumerate(participant_checked.board[k]):
                        if x == sel_num:
                            participant_checked.board[k][i] = -1
                    if all(elem < 0 for elem in participant_checked.board[k]):
                        participant_checked.already_won = True
                        participant_checked.rounds_to_win = current_round
                        participant_checked.win_num = sel_num
    return participant_checked


if __name__ == '__main__':
    with open('input.txt') as f:
        selected_numbers = {}
        current_read_index = 0
        current_board_line = 0
        participant = BingoParticipant()
        loser = BingoParticipant()
        worst_round_to_win = 0
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
                    if participant.already_won and participant.rounds_to_win > worst_round_to_win:
                        loser = participant
                        worst_round_to_win = participant.rounds_to_win
            else:
                participant = BingoParticipant()
                current_board_line = 0
            current_read_index += 1

        total_unmarked = 0
        for key in loser.board:
            for num in loser.board[key]:
                if num >= 0:
                    total_unmarked += num
        print (total_unmarked / 2) * loser.win_num
        f.close()
