front = "어서오세요 맛있는음식점입니다.\n"
menu = '   [메뉴판] \n 1.보쌈 : 30000\n 2.족발 : 25000\n 3.삼겹살 : 15000\n 4.제육볶음 : 9000\n 5. 음료수 : 1000\n'
what = '무엇을 주문하시겠습니까? : '
more = '주문을 더 하신다면 1번\n결제하시려면 2번을 눌러주세요 : '
totalMsg = '총 계산금액은 '
payment = '결제수단을 선택해주세요. \n 1.현금 \n 2.카드 \n 3.삼성페이 '

name = ['보쌈', '족발', '삼겹살', '제육볶음', '음료수']
price = [30000, 25000, 15000, 9000, 1000]

order_menu = []  #주문서
wallet = 50000 #지갑
total = 0  #총 가격
change = 0  #거스름돈

#메뉴를 주문하는 함수
def order():
    global order_menu
    global total
    print(menu)  #메뉴출력
    choice = int(input(what))
    #보쌈
    if choice == 1:
        order_menu.append('보쌈')  #빈 주문서에 추가
        total += price[0]
    #족발
    elif choice == 2:
        order_menu.append('족발')
        total += price[1]
    #삼겹살
    elif choice == 3:
        order_menu.append('삼겹살')
        total += price[2]
    #제육볶음
    elif choice == 4:
        order_menu.append('제육볶음')
        total += price[3]
    #음료수
    else:
        order_menu.append('음료수')
        total += price[4]

# 결제하는 함수
def pay():
    count = 0
    while True:
        change = wallet - total
        if change < 0:
            print("잔액이 부족합니다.")
        else:
            print("주문 내역은", order_menu,'입니다.')
            print('거스름돈은 ' + str(change) + '원 입니다.')
            break

## 메인함수
print(front)

#주문하기
order()
#추가주문 물어보기
while True:
    choice = int(input(more))
    if choice == 1:
        order()
    elif choice == 2:
        break
    else:
        print('다시 입력하세요.')

#계산하기
print('\n' + totalMsg + str(total) + '원 입니다.')
pay()
