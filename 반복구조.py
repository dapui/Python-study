num = int(input("어디까지 더할까요?"))

sum = 0
i = 1

while i <= num :
    sum = sum + i
    i = i + 1
    
print("1부터", num, "까지의 합은", sum, "입니다.")

# ======================================================

# === 사용자가 입력한 단의 구구단 출력 문제 ===
base = int(input("출력할 구구단의 단을 입력하세요: "))

i = 1
while i <= 9 :
    print(base, "X", i, "=", base * i)
    i = i + 1

# ======================================================

# 리스트 생성
hei_list = [1, 4, 14, 26, 31]

for hei in hei_list :
    print(hei)

# ======================================================

# === 반지름은 10이고 높이가 1, 5, 14, 26, 31인 원뿔의 부피와 겉넓이를 각각 출력하는 문제 ===
rad = 10
hei_list = [1, 5, 14, 26, 31]

for hei in hei_list :
    #부피&겉넓이 계산
    vol = 1/3 * 3.14 * rad ** 2 * hei
    surf = 3.14 * rad ** 2 + 3.14 * rad * hei
    print("반지름", rad, "높이", hei, "원뿔")
    print("원뿔의 부피는" ,vol, "입니다.")
    print("원뿔의 겉넓이는" ,surf, "입니다")

# ======================================================

# === 반지름과 높이가 (10, 1), (20, 5), (30, 14)인원뿔의 부피와 겉넓이를 각각 출력하는 문제 ===
# range 함수 (리스트 생성 자동화)
# range(a, b, k) -> a부터 b보다 작은 값까지 k씩 증가시켜 시퀀스 생성
# a 생략 시 기본값 0, k 생략 시 기본값 1

rad_list = range(10, 31, 10)
hei_list = [1, 5, 14]

for rad, hei in zip(rad_list, hei_list) :
    #부피&겉넓이 계산
    vol = 1/3 * 3.14 * rad ** 2 * hei
    surf = 3.14 * rad ** 2 + 3.14 * rad * hei
    print("반지름", rad, "높이", hei, "원뿔")
    print("원뿔의 부피는" ,vol, "입니다.")
    print("원뿔의 겉넓이는" ,surf, "입니다")

# ======================================================

# === 구구단 표를 출력하는 문제 ===
# format 함수 : 데이터를 양식에 맞춰 형식화
# format("구구단표",">10s")
# > -> 정렬방향
# 10 -> 필드 폭
# s -> 데이터 타입(문자=s, 정수=d)
print(format("구구단표",">20s"))

# 표 머리 출력
print("  |", end = "")
for j in range(1, 10):
    print("  ", j, end = "") # end = "" -> 다음 라인으로 넘기지 말고 해당 라인에 출력
# 새로운 행 삽입
print()
print("-----------------------------------------")

# 중첩 반복 구조
# 구구단 표 출력
for i in range(1, 10, 1) :
    print(i, "|", end = "")
    for j in range(1, 10, 1) :
        print(format(i * j, ">4d"), end = "")
    print() # 라인을 바꾸기 위한 print