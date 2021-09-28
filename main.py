import tkinter as tk
from PIL import Image, ImageTk

price_meal = {"김밥": 3000, "라면": 3500, "떡볶이": 5000, "튀김": 5000, "쫄면": 7000}
price_drink = {"아메리카노": 3000, "라떼": 3500, "아이스티": 4000, "레몬에이드": 4500, "딸기스무디": 5000}

order_meal = {}
order_drink = {}

total_price = 0


def show_meal():
    btn_meal.configure(bg="yellow")
    btn_drink.configure(bg="white")
    frame4.pack_forget()
    frame3.pack_forget()
    frame2.pack(fill="both", expand=True)
    frame4.pack(fill="both", expand=True)


def show_drink():
    btn_meal.configure(bg="white")
    btn_drink.configure(bg="yellow")
    frame4.pack_forget()
    frame2.pack_forget()
    frame3.pack(fill="both", expand=True)
    frame4.pack(fill="both", expand=True)


def meal_add(m):
    global price_meal, order_meal, total_price
    if m not in price_meal:
        print("입력한 메뉴가 존재하지 않습니다.")
    this_price = price_meal.get(m)
    total_price += this_price

    if m in order_meal:
        order_meal[m] = order_meal.get(m) + 1
    else:
        order_meal[m] = 1
    print_order()
    print_price()


def drink_add(m):
    global price_meal, order_meal, total_price
    if m not in price_drink:
        print("입력한 메뉴가 존재하지 않습니다.")
    this_price = price_drink.get(m)
    total_price += this_price

    if m in order_drink:
        order_drink[m] = order_drink.get(m) + 1
    else:
        order_drink[m] = 1
    print_order()
    print_price()


def print_order():
    global order_meal, order_drink

    tmp = ""
    price_tmp = 0
    for i in order_meal:
        price_tmp = price_meal[i] * order_meal.get(i)
        tmp = tmp + i + " : " + str(order_meal.get(i)) +  "개\n"
    for i in order_drink:
        price_tmp = price_drink[i] * order_drink.get(i)
        tmp = tmp + i + " : " + str(order_drink.get(i)) +  "개\n"

    text_1.delete('1.0', tk.END)
    text_1.insert(tk.INSERT, tmp)


def order_end():
    global total_price, order_meal, order_drink
    total_price = 0
    del order_meal
    del order_drink

    order_meal = {}
    order_drink = {}
    print_price()
    print_order()
    show_meal()


def print_price():
    global total_price
    label_price.configure(text=str(total_price)+" 원")


window = tk.Tk()
window.title("주문 프로그램")

#창 크기
window.geometry("600x600+500+100")

#실행후 사이즈 맘대로 늘렸다 줄였다 가능
window.resizable(True, True)

frame1 = tk.Frame(window, width="600", height="10")
frame1.pack(fill="both")

frame2 = tk.Frame(window, width="600")
frame2.pack(fill="both", expand=True)

frame3 = tk.Frame(window, width="600")
# frame3.pack(fill="both", expand=True)

frame4 = tk.Frame(window, width="600", height="10")
frame4.pack(fill="both",side="bottom", expand=True)

btn_meal = tk.Button(frame1, text="식사", padx="10", pady="10", bg="yellow", command=show_meal)
btn_meal.grid(row=0, column=0, padx=10, pady=10)

btn_drink = tk.Button(frame1, text="음료", padx="10", pady="10", bg="white", command=show_drink)
btn_drink.grid(row=0, column=1, padx=10, pady=10)

btn_end = tk.Button(frame1, text="주문종료", padx="10", pady="10", command=order_end)
btn_end.grid(row=0, column=2, padx=10, pady=10)

label_price = tk.Label(frame1, text="0 원", width="20", padx=10, pady="10", fg="blue", font='Arial 15')
label_price.grid(row=0, column="3", padx="10", pady="10")

# 식사
btn_meal_1 = tk.Button(frame2, text="김밥\n(3000원)", padx="10", pady="10", width="10", command=lambda: meal_add('김밥'))
btn_meal_1.grid(row=0, column=0, padx=10, pady=10)

btn_meal_2 = tk.Button(frame2, text="라면\n(3500원)", padx="10", pady="10", width="10", command=lambda: meal_add('라면'))
btn_meal_2.grid(row=0, column=1, padx=10, pady=10)

btn_meal_3 = tk.Button(frame2, text="떡볶이\n(5000원)", padx="10", pady="10", width="10", command=lambda: meal_add('떡볶이'))
btn_meal_3.grid(row=0, column=2, padx=10, pady=10)

btn_meal_4 = tk.Button(frame2, text="튀김\n(5000원)", padx="10", pady="10", width="10", command=lambda: meal_add('튀김'))
btn_meal_4.grid(row=0, column=3, padx=10, pady=10)

btn_meal_5 = tk.Button(frame2, text="쫄면\n(7000원)", padx="10", pady="10", width="10", command=lambda: meal_add('쫄면'))
btn_meal_5.grid(row=0, column=4, padx=10, pady=10)

btn_meal_6 = tk.Button(frame2, text="순대\n(3000원)", padx="10", pady="10", width="10", command=lambda: meal_add('김밥'))
btn_meal_6.grid(row=1, column=0, padx=10, pady=10)

btn_meal_7 = tk.Button(frame2, text="돈가스\n(5000원)", padx="10", pady="10", width="10", command=lambda: meal_add('라면'))
btn_meal_7.grid(row=1, column=1, padx=10, pady=10)

btn_meal_8 = tk.Button(frame2, text="냉면\n(5000원)", padx="10", pady="10", width="10", command=lambda: meal_add('떡볶이'))
btn_meal_8.grid(row=1, column=2, padx=10, pady=10)

btn_meal_9 = tk.Button(frame2, text="오므라이스\n(6000원)", padx="10", pady="10", width="10", command=lambda: meal_add('튀김'))
btn_meal_9.grid(row=1, column=3, padx=10, pady=10)


# 음료
americano = Image.open('아메리카노.png')
americano = americano.resize((80, 100), Image.ANTIALIAS)
resized_americano = ImageTk.PhotoImage(americano)
btn_drink_1 = tk.Button(frame3, image=resized_americano, padx="10", pady="10", width="80", command=lambda: drink_add('아메리카노'))
btn_drink_1.grid(row=0, column=0, padx=10, pady=10)

latte = Image.open('라떼.png')
latte = latte.resize((80, 100), Image.ANTIALIAS)
resized_latte = ImageTk.PhotoImage(latte)
btn_drink_2 = tk.Button(frame3, image=resized_latte, padx="10", pady="10", width="80", command=lambda: drink_add('라떼'))
btn_drink_2.grid(row=0, column=1, padx=10, pady=10)

milk_tea = Image.open('밀크티.png')
milk_tea = milk_tea.resize((80, 100), Image.ANTIALIAS)
resized_milk_tea = ImageTk.PhotoImage(milk_tea)
btn_drink_3 = tk.Button(frame3, image=resized_milk_tea, padx="10", pady="10", width="80", command=lambda: drink_add('아이스티'))
btn_drink_3.grid(row=0, column=2, padx=10, pady=10)

strawberry = Image.open('딸기스무디.png')
strawberry = strawberry.resize((80, 100), Image.ANTIALIAS)
resized_strawberry = ImageTk.PhotoImage(strawberry)
btn_drink_4 = tk.Button(frame3, image=resized_strawberry, padx="10", pady="10", width="80", command=lambda: drink_add('레몬에이드'))
btn_drink_4.grid(row=0, column=3, padx=10, pady=10)


# 주문 리스트
bucket = tk.Label(frame4, text='장바구니',font=('Malgun Gothic',15),padx=10,pady=10)
bucket.pack()
text_1 = tk.Text(frame4)
text_1.pack()

window.mainloop()
