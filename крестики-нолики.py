def draw_field(field):
    
    print(f'  1 2 3')
    print('--------')
    for i in range(3):
        print( f"{i+1} {field[i][0]} {field[i][1]} {field[i][2]}" )
    print('--------')
    
field = [[' '] * 3 for i in range(3)]

# Функция, которая проверяет, выиграл ли кто-то
def get_winner(field):
# Проверяем строки
    for i in range(3):
        if field[i][0] == field[i][1] == field[i][2] and field[i][0] != ' ':
            return field[i][0]
# Проверяем столбцы
    for i in range(3):
        if field[0][i] == field[1][i] == field[2][i] and field[0][i] != ' ':
            return field[0][i]
# Проверяем диагонали
        if field[0][0] == field[1][1] == field[2][2] and field[0][0] != ' ':
            return field[0][0]
        if field[2][0] == field[1][1] == field[0][2] and field[2][0] != ' ':
            return field[2][0]
# Если никто не выиграл, возвращаем None
    return None

def cords():
    while True:
        
        row = input("Введите номер строки: ")
        
        if not (row.isdigit()):
            print('Символ вне диапазона, выбери другй (1, 2 или 3)')
            continue
        
        row = int(row) - 1
        
        if row < 0 or row > 2:
            print('Символ вне диапазона, выбери другй (1, 2 или 3)')
            continue
        
        col = input("Введите номер столбца: ")
        
        if not (col.isdigit()):
            print('Символ вне диапазона, выбери другй (1, 2 или 3)')
            continue
        
        col = int(col) - 1
        
        if col < 0 or col > 2:
            print('Символ вне диапазона, выбери другй (1, 2 или 3)')
            continue
        
        if field[row][col] != ' ':
            print("Эта клетка уже занята, попробуйте еще раз")
            continue
        return row, col

# Запускаем игру
counter = 0
current_player = 'X'
while True:
    
    draw_field(field)
    print("Ход игрока", current_player)
    row, col = cords()
    
    counter += 1
    
    field[row][col] = current_player
    winner = get_winner(field)
    if winner:
        draw_field(field)
        print("Выиграл игрок", winner)
        break
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'
    if counter == 9:
        draw_field(field)
        print('Ничья!')
        break