# dir, help 함수 테스트
# dir() : 객체가 가지고 있는 속성과 메서드 목록을 보여줌
import math

# dir()
# dir(math)
# help(math.gamma)


# === math 모듈을 사용한 원뿔 계산 프로그램 ===
# 원뿔 클래스 정의
class Cone :
    def __init__(self, radius = 20, height = 30):
        self.r = radius
        self.h = height
    
    def get_vol(self) :
        return 1/3 * math.pi * self.r ** 2 * self.h

    def get_surf(self) :
        return math.pi * self.r ** 2 + math.pi * self.r * self.h


# ======================================================
# 유용한 모듈

# === 두 변의 길이 a, b와 끼인각 α인 삼각형의 넓이를 구하는 프로그램 ===
from math import sin
a, b = 10, 20
area = 1 / 2 * a * b * sin(math.radians(60))

print(area)


# === 1 ~ 45 숫자 6개를 입력 받아 당첨 숫자와 비교하는 프로그램 ===
import random

guess_str = input("1 ~ 45 사이의 숫자 6개를 쉼표로 분리하여 입력하세요 : ").split(",")
guess_list = list()

for i in guess_str :
    guess_list.append(int(i))

lotto_list = random.sample(range(1, 46, 1), 6)

print("예상 번호는", guess_list, "입니다.")
print("추첨 번호는", lotto_list, "입니다.")

hit_count = 0

for guess in guess_list :
    if guess in lotto_list :
        hit_count = hit_count + 1

print("축하합니다 " + str(hit_count) + "개 맞혔습니다.")


# === 20번의 기회 안에 1 ~ 1000 사이의 숫자를 맞히는 스무고개 프로그램 ===
hit_number = random.randint(1, 1001)
guess_count_list = range(1, 21, 1)
passfail = False

for guess_count in guess_count_list :
    guess = int(input("1 ~ 1000 사이의 숫자를 맞혀보세요(" + str(guess_count) + "번째 시도): "))

    if hit_number == guess :
        passfail = True
        break
    elif hit_number > guess :
        print(str(guess) + "보다 큽니다.", end = "")
    else :
        print(str(guess) + "보다 작습니다.", end = "")

if passfail == True :
    print("맞혔습니다. 축하합니다.")
else :
    print("모든 기회를 다 사용하셨습니다. 다음에 다시 도전하세요.")


# === 1000보다 작은 소수(prime number) 찾기 프로그램 ===
import time

start_time = time.time()

def is_prime(x) :
    for i in range(2, x) :
        if x % i == 0 :
            return False
    return True

prime_count = 0

for i in range(2, 50001) :
    if is_prime(i) :
        prime_count = prime_count + 1
        print(i, end = ", ")

end_time = time.time()
print("\n", end_time - start_time, "초 실행했습니다.")