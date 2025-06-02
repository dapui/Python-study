# 'Khan.txt' 파일을 읽고 처리하는 프로그램을 작성하시오.
Khan_fp = open("Khan.txt", "r") # 'Khan.txt' 파일을 읽기 모드(r)로 열기
print(Khan_fp.read(10)) # 처음 10글자 출력
print(Khan_fp.readline()) # 첫 번째 줄 출력

# 'Khan.txt' 파일의 모든 줄을 출력
for motto in Khan_fp.readlines():
    print(motto.strip()) # 각 줄의 양쪽 공백 제거 후 출력(strip() -> 특정 문자를 제거)

Khan_fp.close()


Khan_fp = open("Khan.txt", "a") # 'Khan.txt' 파일을 append 모드(a: 내용 추가)로 열기

Khan_fp.write("\n")
Khan_fp.write(format("-칭기스 칸-", ">50s"))

Khan_fp.close() # 파일 닫기

# ======================================================
# 데이터 분석 프로그램
#"hamlet_by_Shakespeare.txt" 파일에 포함된 단어와 각 단어의 출현 횟수를 출력하는 프로그램을 작성하시오
h_fp = open("Hamlet_by_Shakespeare.txt", "r") # 'Hamlet_by_Shakespeare.txt' 파일을 읽기 모드(r)로 열기

word_dict = dict() # 비어있는 딕셔너리 생성

for line in h_fp.readlines(): # 파일의 모든 줄을 읽어오기
    for word in line.strip().split(): # 불필요한 개행문자 제거: strip() -> 결과물을 하나씩 분할: split()
        word = word.strip(" .,;?[]\"\':-!").lower() # 단어의 양쪽 공백과 특수문자 제거 후 소문자로 변환

        if word_dict.get(word) is not None:
            count = word_dict[word]
        else:
            count = 0

        word_dict[word] = count + 1 # 단어의 출현 횟수를 1 증가시킴
        
for key in word_dict: # 딕셔너리의 키(단어)를 순회하며
    print("[" + key + "]", str(word_dict[key]) + "회") # 단어와 그 출현 횟수를 출력

h_fp.close() # 파일 닫기

# ======================================================
# 데이터 분석 프로그램
#'hamlet_by_Shakespeare.txt' 파일에 포함된 단어 중 출현한 횟수가 100 이상되는 단어와 출력 횟수를 출력하는 프로그램을 작성하시오
h_fp = open("Hamlet_by_Shakespeare.txt", "r") # 'Hamlet_by_Shakespeare.txt' 파일을 읽기 모드(r)로 열기

word_dict = dict() # 비어있는 딕셔너리 생성

for line in h_fp.readlines(): # 파일의 모든 줄을 읽어오기
    for word in line.strip().split(): # 불필요한 개행문자 제거: strip() -> 결과물을 하나씩 분할: split()
        word = word.strip(" .,;?[]\"\':-!").lower() # 단어의 양쪽 공백과 특수문자 제거 후 소문자로 변환

        if word_dict.get(word) is not None:
            count = word_dict[word]
        else:
            count = 0

        word_dict[word] = count + 1 # 단어의 출현 횟수를 1 증가시킴
        
word_dict = {v:k for (k, v) in word_dict.items()} # 키와 값을 바꿔서 출현 횟수를 키로, 단어를 값으로 하는 딕셔너리 생성

word_dict = {k:v for (v, k) in sorted(word_dict.items(), reverse=True)} # 키와 값을 바꿔서(원복) word_r_dict에서 가져온 것들을 정렬 -> 내림차순(reverse=True)하여 다시 딕셔너리로 구성

for key in word_dict: # 딕셔너리의 키(단어)를 순회하며
    if word_dict[key] >= 100:
        print("[" + key + "]", str(word_dict[key]) + "회") # 단어와 그 출현 횟수를 출력

h_fp.close() # 파일 닫기