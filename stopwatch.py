import tkinter as tk
from datetime import datetime

# 스톱워치 변수 초기화
is_running = False
start_time = None
lap_times = []

# 스톱워치 시작 함수
def start_stop():
    global is_running, start_time
    if is_running:
        is_running = False
        stop_button.config(text="시작")
    else:
        is_running = True
        stop_button.config(text="종료")
        if start_time is None:
            start_time = datetime.now()
        else:
            current_time = datetime.now()
            elapsed_time = current_time - start_time
            start_time = current_time - elapsed_time

# 스톱워치 리셋 함수
def reset():
    global is_running, start_time, lap_times
    is_running = False
    start_time = None
    lap_times = []
    time_var.set("00:00.00")
    lap_times_text.delete(1.0, tk.END)

# 랩 타임 기록 함수
def lap():
    global is_running, lap_times
    if is_running:
        current_time = datetime.now()
        lap_time = current_time - start_time
        lap_times.append(lap_time)
        time_var.set(format_time(lap_time))
        update_lap_times()

# 시간 업데이트 함수
def update_time():
    if is_running:
        current_time = datetime.now() - start_time
        time_var.set(format_time(current_time))
    root.after(10, update_time)

# 랩 타임 업데이트 함수
def update_lap_times():
    lap_times_text.delete(1.0, tk.END)
    for lap in lap_times:
        lap_times_text.insert(tk.END, format_time(lap) + "\n")

# 시간 포맷 함수
def format_time(time):
    minutes, seconds = divmod(time.seconds, 60)
    microseconds = time.microseconds
    return f"{int(minutes):02d}:{int(seconds):02d}.{int(microseconds / 10000):02d}"

# tkinter 애플리케이션 초기화
root = tk.Tk()
root.title("스톱워치")

# 시간 표시 레이블
time_var = tk.StringVar()
time_var.set("00:00.00")
time_label = tk.Label(root, textvariable=time_var, font=("Arial", 30))
time_label.pack(pady=20)

# 시작, 종료, 리셋, 랩 버튼
start_button = tk.Button(root, text="시작", command=start_stop)
stop_button = tk.Button(root, text="종료", command=start_stop)
reset_button = tk.Button(root, text="리셋", command=reset)
lap_button = tk.Button(root, text="랩", command=lap)

start_button.pack()
stop_button.pack()
reset_button.pack()
lap_button.pack()

# 랩 타임 표시 박스
lap_times_text = tk.Text(root, height=10, width=20, font=("Arial", 12))
lap_times_text.pack(pady=10)

# 시간 업데이트 시작
update_time()

root.mainloop()
