import tkinter as tk
from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

def search():
    search_query = entry.get()
    if search_query:
        # Chrome 웹 드라이버 초기화
        chrome_driver_path = "./chromedriver.exe"  # chromedriver.exe 파일의 실제 경로로 변경
        service = Service(chrome_driver_path)
        driver = webdriver.Chrome(service=service)

        # 네이버 쇼핑 검색 페이지 열기
        driver.get("https://shopping.naver.com/")

        # 검색어 입력
        search_box = driver.find_element_by_css_selector("#autocompleteWrapper input")
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)

        # 검색 결과 출력
        product_elements = driver.find_elements_by_css_selector(".basicList_info_area")
        for product_element in product_elements:
            product_title = product_element.find_element_by_css_selector(".basicList_title").text
            product_price = product_element.find_element_by_css_selector(".price_num").text
            text_box.insert(tk.END, f"{product_title} - {product_price}\n")

        # 웹 드라이버 종료
        driver.quit()

# tkinter 창 초기화
root = tk.Tk()
root.title("네이버 쇼핑 상품 크롤러")

# 검색어 입력 레이블과 입력 상자
label = ttk.Label(root, text="검색어:")
label.pack()
entry = ttk.Entry(root)
entry.pack()

# 검색 버튼 생성 및 연결
search_button = ttk.Button(root, text="검색", command=search)
search_button.pack()

# 검색 결과를 표시할 텍스트 박스
text_box = tk.Text(root, height=10, width=50)
text_box.pack()

# tkinter 창 실행
root.mainloop()






