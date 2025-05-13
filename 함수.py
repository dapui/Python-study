# === 원뿔 부피 계산 함수 정의 ===
def prt_cone_vol(r, h) :
    if r > 0 and h > 0 :
        # r, h 모두 양수일 때
        vol = 1/3 * 3.14 * r ** 2 * h
        print("원뿔의 부피는", vol, "입니다.")
    else :
        # r, h가 음수일 때
        print("반지름과 높이 값에 양수를 입력하세요")

rad = int(input("반지름을 입력하세요: "))
hei = int(input("높이를 입력하세요: "))

prt_cone_vol(rad, hei) # 원뿔 부피 계산 함수 호출

# === 숫자를 입력받고 역순으로 출력하는 함수를 사용한 프로그램 문제 ===
num = int(input("숫자를 입력하세요: "))

def reverse_num(num) :
    while num != 0 :
        digit = num % 10
        num = num // 10
        print(digit, end="") # end="" : 개행문자 대신 한 줄에 이어서 출력

reverse_num(num)
print()

# ======================================================

# === 원뿔 부피 계산 결과 반환 함수 정의 ===
def rtn_cone_vol(r, h) :
    if r > 0 and h > 0 :
        # r, h 모두 양수일 때
        vol = 1/3 * 3.14 * r ** 2 * h
        return vol
    else :
        # r, h가 음수일 때
        print("반지름과 높이 값에 양수를 입력하세요")

print(format(rtn_cone_vol(10, 20), ">20.3f"), "입니다.")

# === 원뿔 부피 및 겉넓이 반환 함수 정의 (동시할당) ===
def rtn_cone_vol_surf(r, h) :
    if r > 0 and h > 0 :
        # r, h 모두 양수일 때
        vol = 1/3 * 3.14 * r ** 2 * h
        surf = 3.14 * r ** 2 + 3.14 * r * h
        return vol, surf
    else :
        # r, h가 음수일 때
        print("반지름과 높이 값에 양수를 입력하세요")

vol1, surf1 = rtn_cone_vol_surf(50, 100)
print(format(vol1, ".3f"), "입니다.")
print(surf1, "입니다.")


# === 세 개의 사용자 입력을 오름차순으로 정렬하는 함수를 이용하여 정렬된 값을 출력하는 문제 ===

a = int(input("첫번째 숫자를 입력하세요: "))
b = int(input("첫번째 숫자를 입력하세요: "))
c = int(input("첫번째 숫자를 입력하세요: "))

def sort3(a, b, c) :
    if a > b :
        a, b = b, a
    if a > c :
        a, c = c, a
    if b > c :
        b, c = c, b

    print(a, b, c)

sort3(a, b, c)
print("출력 이후", a, b, c)

# ======================================================

# === 값의 전달 ===
def rtn_cone_vol1(r, h) :
    if r > 0 and h > 0 :
        # r, h 모두 양수일 때
        vol = 1/3 * 3.14 * r ** 2 * h
        r, h = 0, 0
        return vol
    else :
        # r, h가 음수일 때
        print("반지름과 높이 값에 양수를 입력하세요")

radius = 50
height = 100
print(format(rtn_cone_vol1(radius, height), ">10.3f"))
print("함수 사용 후", radius, height)

# === 변수의 스코프 ===
x = 1
print("1. x의 값은", x)

def inc1(x) :
    x = x + 1
    print("2. x의 값은", x)

inc1(x)
print("3. x의 값은", x)

# === 단위 원뿔(반지름 20, 높이 30)의 부피와 겉넓이를 출력하는 문제 ===
# 원뿔 계산 함수 정의
def rtn_cone_vol_surf1(r = 20, h = 30) :
    if r > 0 and h > 0 :
        # r, h 모두 양수일 때
        return 1/3 * 3.14 * r ** 2 * h, 3.14 * r ** 2 + 3.14 * r * h
    else :
        # r, h가 음수일 때
        print("반지름과 높이 값에 양수를 입력하세요")

print(rtn_cone_vol_surf1(100, 200))
print(rtn_cone_vol_surf1()) # 기본값 사용

# === 여러개의 수를 입력받고 합과 평균을 반환하는는 var_sum_avg 함수를 사용하여, 
# (20, 25, 10, 85, 100, 150)에 대한 합과 평균을 출력하는 프로그램을 작성하시오. ===
def var_sum_avg(*numbers) :
    sum = 0
    count = 0

    for i in numbers :
        sum = sum + i
        count = count + 1

    return sum, sum/count

print(var_sum_avg(20, 25, 10, 85, 100, 150))