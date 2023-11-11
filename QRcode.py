import tkinter as tk
import qrcode
from PIL import Image, ImageTk

def generate_qr_code():
    link = entry.get()
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # PIL 이미지를 tkinter PhotoImage로 변환
    img_pil = ImageTk.PhotoImage(img)
    
    # 이미지를 화면에 표시
    label_qr.config(image=img_pil)
    label_qr.image = img_pil
    
    # QR 코드 이미지를 전역 변수로 저장하여 나중에 저장 버튼에서 사용
    global qr_img
    qr_img = img

def save_qr_code():
    if qr_img:
        filename = "qrcode.png"
        qr_img.save(filename)
        print(f"QR Code saved as {filename}")

root = tk.Tk()
root.title("QR Code Generator")

label = tk.Label(root, text="Enter a link:")
label.pack()

entry = tk.Entry(root)
entry.pack()

generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr_code)
generate_button.pack()

save_button = tk.Button(root, text="Save QR Code", command=save_qr_code)
save_button.pack()

# QR 코드를 표시할 라벨
label_qr = tk.Label(root)
label_qr.pack()

# QR 코드 이미지를 저장하기 위한 전역 변수
qr_img = None

root.mainloop()
