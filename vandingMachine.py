import tkinter as tk

# 초기 상품 정보
products = {
    "짜장면": {"price": 6000, "quantity": 5},
    "짬뽕": {"price": 7000, "quantity": 3},
    "탕수육": {"price": 12000, "quantity": 10},
    "볶음밥": {"price": 8000, "quantity": 8}
}

# 초기 잔액
balance = 0

def update_display():
    for product, info in products.items():
        label_quantity[product].config(text=f"{product}: {info['quantity']} 개 남음")

    label_balance.config(text=f"잔액: {balance} 원")

def charge_money():
    global balance
    amount = int(charge_entry.get())
    balance += amount
    charge_entry.delete(0, 'end')  # 입력 필드 지우기
    update_display()

def buy_product(product):
    global balance
    if products[product]["quantity"] > 0 and balance >= products[product]["price"]:
        products[product]["quantity"] -= 1
        balance -= products[product]["price"]
        update_display()
        if products[product]["quantity"] == 0:
            label_quantity[product].config(text=f"{product}: 매진")

# tkinter 창 생성
root = tk.Tk()
root.title("중국집 자판기")

# 레이블 및 입력 필드
charge_label = tk.Label(root, text="충전할 금액:")
charge_label.pack()

charge_entry = tk.Entry(root)
charge_entry.pack()

# 충전 버튼
charge_button = tk.Button(root, text="돈 충전", command=charge_money)
charge_button.pack()

# 상품 목록 및 버튼 생성
label_quantity = {}
for product in products:
    label_quantity[product] = tk.Label(root, text=f"{product}: {products[product]['quantity']} 개 남음")
    label_quantity[product].pack()
    buy_button = tk.Button(root, text=f"구매 ({products[product]['price']}원)", command=lambda p=product: buy_product(p))
    buy_button.pack()

# 잔액 표시 레이블
label_balance = tk.Label(root, text=f"잔액: {balance} 원")
label_balance.pack()

# 초기 화면 업데이트
update_display()

# tkinter 실행
root.mainloop()
