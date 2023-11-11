import tkinter as tk
import random

# 게임 보드 크기와 지뢰 개수 설정
board_size = 10
num_mines = 15

# 보드 초기화
board = [[0] * board_size for _ in range(board_size)]
mines = []

# 게임 진행 상태 초기화
game_over = False

def initialize_board():
    global game_over
    game_over = False
    for y in range(board_size):
        for x in range(board_size):
            board[y][x] = 0
    mines.clear()

    # 지뢰 배치
    while len(mines) < num_mines:
        x, y = random.randint(0, board_size - 1), random.randint(0, board_size - 1)
        if board[y][x] != -1:
            board[y][x] = -1
            mines.append((x, y))

    # 주변 지뢰 개수 계산
    for x, y in mines:
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if 0 <= x + dx < board_size and 0 <= y + dy < board_size and board[y + dy][x + dx] != -1:
                    board[y + dy][x + dx] += 1

initialize_board()

def click_cell(x, y):
    global game_over
    if game_over:
        return

    if board[y][x] == -1:
        # 지뢰 클릭 시 게임 종료
        label.config(text="지뢰를 클릭했습니다. 게임 종료!")
        reveal_board()
        game_over = True
    elif board[y][x] == 0:
        # 주변에 지뢰가 없는 경우 주변 영역 열기
        reveal_empty(x, y)
    else:
        # 숫자 표시
        buttons[y][x].config(text=str(board[y][x]))

def reveal_empty(x, y):
    if 0 <= x < board_size and 0 <= y < board_size and buttons[y][x]["state"] != "disabled":
        buttons[y][x].config(state="disabled")
        if board[y][x] == 0:
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    reveal_empty(x + dx, y + dy)
        else:
            buttons[y][x].config(text=str(board[y][x]))

def reveal_board():
    for y in range(board_size):
        for x in range(board_size):
            if board[y][x] == -1:
                buttons[y][x].config(bg="red")  # 지뢰를 빨강색으로 표시

def new_game():
    initialize_board()
    label.config(text="새 게임을 시작합니다.")
    for y in range(board_size):
        for x in range(board_size):
            buttons[y][x].config(text="", state="normal", bg="SystemButtonFace")
    mines_label.config(text=f"지뢰 개수: {num_mines}")

# GUI 생성
root = tk.Tk()
root.title("지뢰 찾기 게임")

buttons = [[None] * board_size for _ in range(board_size)]

for y in range(board_size):
    for x in range(board_size):
        buttons[y][x] = tk.Button(root, width=2, height=1, command=lambda x=x, y=y: click_cell(x, y))
        buttons[y][x].grid(row=y, column=x)

label = tk.Label(root, text="")
label.grid(row=board_size, columnspan=board_size)

new_game_button = tk.Button(root, text="새 게임 시작", command=new_game)
new_game_button.grid(row=board_size + 1, columnspan=board_size)

mines_label = tk.Label(root, text=f"지뢰 개수: {num_mines}")
mines_label.grid(row=board_size + 2, columnspan=board_size)

root.mainloop()


