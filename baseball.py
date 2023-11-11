import tkinter as tk
from tkinter import messagebox
import random

# 비밀 숫자 생성
def generate_secret_number():
    return ''.join(random.sample('0123456789', 3))

# 힌트 생성
def get_hint(secret_number, guess):
    strikes, balls = 0, 0
    for i in range(3):
        if guess[i] == secret_number[i]:
            strikes += 1
        elif guess[i] in secret_number:
            balls += 1
    return strikes, balls

# 게임 초기화
def new_game():
    global secret_number, attempts, lives
    secret_number = generate_secret_number()
    attempts = 0
    lives = 5  # 라이프 초기화
    label.config(text="야구 게임을 시작합니다. 3자리 숫자를 맞춰보세요! (라이프: 5)")
    play_button.config(state=tk.NORMAL)  # 새 게임 시작 후 확인 버튼 활성화

# 게임 진행
def play_game():
    global attempts, lives
    guess = entry.get()

    if len(guess) != 3 or not guess.isdigit():
        messagebox.showwarning("경고", "올바른 숫자를 입력하세요.")
        return

    attempts += 1
    strikes, balls = get_hint(secret_number, guess)

    if strikes == 3:
        messagebox.showinfo("축하합니다!", f"{secret_number}를 {attempts}번 만에 맞추셨습니다!")
        play_button.config(state=tk.DISABLED)  # 3 스트라이크 시 확인 버튼 비활성화
    else:
        hint = f"스트라이크: {strikes}, 볼: {balls}"
        lives -= 1  # 틀릴 때마다 라이프 감소
        label.config(text=f"야구 게임을 시작합니다. 3자리 숫자를 맞춰보세요! (라이프: {lives})")

        if lives == 0:
            messagebox.showinfo("게임 오버", f"비밀 숫자는 {secret_number}였습니다. 라이프를 모두 소진하셨습니다.\n새 게임을 시작합니다.")
            play_button.config(state=tk.DISABLED)  # 라이프를 모두 소진하면 확인 버튼 비활성화
            new_game()

        else:
            messagebox.showinfo("힌트", hint)

# Tkinter 창 생성
window = tk.Tk()
window.title("야구 게임")

# 비밀 숫자 초기화
secret_number = generate_secret_number()
attempts = 0
lives = 5  # 라이프 초기화

# 라벨 생성
label = tk.Label(window, text="야구 게임을 시작합니다. 3자리 숫자를 맞춰보세요! (라이프: 5)")
label.pack()

# 입력 필드 생성
entry = tk.Entry(window)
entry.pack()

# 버튼 생성
play_button = tk.Button(window, text="확인", command=play_game)
play_button.pack()

# 새 게임 버튼 생성
new_game_button = tk.Button(window, text="새 게임 시작", command=new_game)
new_game_button.pack()

# Tkinter 창 실행
window.mainloop()