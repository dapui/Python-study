light_on = 3 > 6
print(light_on)

# ===========================

suf = 10
vol = 20
isStop = suf == vol
print(isStop)

# ===========================

temp = 20
fruit = "apple"

print(temp >= 27 and fruit == "pear")
print(temp <= 27 or fruit == "pear")
print(not temp >= 27)

# ===========================
# 반지름 사용자 입력
rad = int(input("반지름을 입력하세요:"))
# 높이 사용자 입력
hei = int(input("높이를 입력하세요:"))

if rad > 0 and hei > 0:
    # 부피&겉넓이 계산
    vol = 1/3 * 3.14 * rad ** 2 * hei
    suf = 3.14 * rad ** 2 + 3.14 * rad * hei
    print("원뿔의 부피는" ,vol, "입니다.")
    print("원뿔의 겉넓이는" ,suf, "입니다")

# ===========================

# esle를 이용한 원뿔 프로그램 개선
# 반지름 사용자 입력
rad = int(input("반지름을 입력하세요:"))
# 높이 사용자 입력
hei = int(input("높이를 입력하세요:"))

if rad > 0 and hei > 0:
    # 부피&겉넓이 계산
    vol = 1/3 * 3.14 * rad ** 2 * hei
    suf = 3.14 * rad ** 2 + 3.14 * rad * hei
    print("원뿔의 부피는" ,vol, "입니다.")
    print("원뿔의 겉넓이는" ,suf, "입니다")
else :
    print("반지름과 높이의 값을 모두 양수로 입력해주세요.")

# ===========================

# 가장 큰 수 찾는 프로그램
# A, B, C 사용자 입력
A = int(input("A 입력 : "))
B = int(input("B 입력 : "))
C = int(input("C 입력 : "))

# A, B, C 중 가장 큰 수 출력
# max(A, B, C) : 내장함수
if A > B :
    if A > C :
        print(A)
    else :
        print(C)
else :
    if B > C :
        print(B)
    else :
        print(C)