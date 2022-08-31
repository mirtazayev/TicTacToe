from typing import Any
from colorama import Fore

board = [' ' for x in range(10)]


def print_success(obj: Any):
    print(Fore.GREEN + str(obj) + Fore.RESET)


def print_fail(obj: Any):
    print(Fore.RED + str(obj) + Fore.RESET)


def print_choice(obj: Any):
    print(Fore.CYAN + str(obj) + Fore.RESET)


def insert_letter(letter, pos):
    board[pos] = letter


def space_is_free(pos):
    return board[pos] == ' '


def print_board(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')


def is_winner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (
            bo[1] == le and bo[2] == le and bo[3] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (
                   bo[2] == le and bo[5] == le and bo[8] == le) or (
                   bo[3] == le and bo[6] == le and bo[9] == le) or (
                   bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le)


def player_move():
    run = True
    while run:
        print_choice("Iltimos, \'X\' qo'yish uchun joyni tanlang (1-9): ")
        move = input()
        try:
            move = int(move)
            if move > 0 and move < 10:
                if space_is_free(move):
                    run = False
                    insert_letter('X', move)
                else:
                    print_fail('Kechirasiz, bu joy band!')
            else:
                print_fail('Iltimos, diapazonga raqam kiriting!')
        except:
            print_fail('Iltimos, raqam yozing!')


def compyuter_move():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if is_winner(boardCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = select_random(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = select_random(edgesOpen)

    return move


def select_random(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


def is_board_full(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def main():
    print_success('Tic Tac Toe-ga xush kelibsiz!')
    print_board(board)

    while not (is_board_full(board)):
        if not (is_winner(board, 'O')):
            player_move()
            print_board(board)
        else:
            print_fail("Kechirasiz, O bu safar g'alaba qozondi!")
            break

        if not (is_winner(board, 'X')):
            move = compyuter_move()
            if move == 0:
                print_fail("Bog'lash o'yini!")
            else:
                insert_letter('O', move)
                print_success(f"Kompyuter {move} o'rniga O  qo'ydi :")
                print_board(board)
        else:
            print_success('X\' yutdi barakalla')
            break

    if is_board_full(board):
        print_fail("Bog'lash o'yini!")


while True:
    print_choice("Yana o'ynashni xohlaysizmi? (Y/N)")
    answer = input()
    if answer.lower() == 'y' or answer.lower == 'yes':
        board = [' ' for x in range(10)]
        print('-----------------------------------')
        main()
    else:
        print_fail("Xayr o'yin tugatildi ...")
        break
