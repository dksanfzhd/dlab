import tkinter as tk
import math

class NewtonSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("뉴턴의 가속도 법칙 시뮬레이터")
        
        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()
        
        self.ball1 = self.canvas.create_oval(50, 50, 100, 100, fill="blue")
        self.ball2 = self.canvas.create_oval(200, 50, 250, 100, fill="red")
        
        self.acceleration1 = 1.0
        self.acceleration2 = 2.0  # 두 번째 물체의 가속도를 2로 설정
        self.velocity = 0.0
        self.time_interval = 0.1
        self.start_button = tk.Button(self.root, text="시작", command=self.start_simulation)
        self.reset_button = tk.Button(self.root, text="리셋", command=self.reset_simulation)
        self.acceleration_scale1 = tk.Scale(self.root, from_=0.1, to=5, resolution=0.1, label="가속도 1", orient="horizontal")
        self.acceleration_scale2 = tk.Scale(self.root, from_=0.1, to=5, resolution=0.1, label="가속도 2", orient="horizontal")

        self.start_button.pack()
        self.reset_button.pack()
        self.acceleration_scale1.set(self.acceleration1)
        self.acceleration_scale2.set(self.acceleration2)
        self.acceleration_scale1.pack()
        self.acceleration_scale2.pack()

    def start_simulation(self):
        self.acceleration1 = self.acceleration_scale1.get()
        self.acceleration2 = self.acceleration_scale2.get()
        self.velocity = 0.0
        self.animate()

    def animate(self):
        self.canvas.move(self.ball1, self.velocity * self.time_interval, 0)
        self.canvas.move(self.ball2, self.velocity * self.time_interval, 0)
        self.velocity += self.acceleration1 * self.time_interval
        self.root.after(100, self.animate)
        
    def reset_simulation(self):
        self.canvas.coords(self.ball1, 50, 50, 100, 100)
        self.canvas.coords(self.ball2, 200, 50, 250, 100)
        self.velocity = 0.0

if __name__ == "__main__":
    root = tk.Tk()
    app = NewtonSimulator(root)
    root.mainloop()
