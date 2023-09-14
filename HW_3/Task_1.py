def create_board():
    # Создаем пустую игровую доску 3x3
    board = [[' ' for _ in range(3)] for _ in range(3)]
    return board

def print_board(board):
    # Выводим игровую доску на экран
    for row in board:
        print('|'.join(row))
        print('-----')

def is_valid_move(move, board):
    # Проверяем, что ход валидный (незанятая клетка)
    row, col = move
    if row < 0 or row >= len(board) or col < 0 or col >= len(board[row]):
        return False
    if board[row][col] != ' ':
        return False
    return True

def make_move(player, move, board):
    # Совершаем ход
    row, col = move
    board[row][col] = player

def has_won(player, board):
    # Проверяем, выиграл ли игрок
    winning_combinations = [
        [(0,0), (0,1), (0,2)],  # горизонтальные
        [(1,0), (1,1), (1,2)],
        [(2,0), (2,1), (2,2)],
        [(0,0), (1,0), (2,0)],  # вертикальные
        [(0,1), (1,1), (2,1)],
        [(0,2), (1,2), (2,2)],
        [(0,0), (1,1), (2,2)],  # диагонали
        [(0,2), (1,1), (2,0)],
    ]
    for combination in winning_combinations:
        if all(board[row][col] == player for row, col in combination):
            return True
    return False

def is_board_full(board):
    # Проверяем, заполнена ли доска
    for row in board:
        if ' ' in row:
            return False
    return True

def play_game():
    # Основная функция игры
    board = create_board()
    players = ['X', 'O']
    current_player = players[0]
    
    while True:
        print_board(board)
    
        print(f"Ход игрока {current_player}")
        move = input("Введите координаты хода (в формате 'строка столбец'): ")
        move = move.split()
        move = (int(move[0]), int(move[1]))
    
        if not is_valid_move(move, board):
            print("Неверный ход. Попробуйте еще раз.")
            continue
    
        make_move(current_player, move, board)
    
        if has_won(current_player, board):
            print_board(board)
            print(f"Игрок {current_player} победил!")
            break
    
        if is_board_full(board):
            print_board(board)
            print("Ничья!")
            break
    
        current_player = players[(players.index(current_player) + 1) % len(players)]

play_game()