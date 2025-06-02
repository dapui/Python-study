# ======================================================
# 틱택토 게임 규칙
# ======================================================

# 1. 한 플레이어가 아직 기록되지 않은 빈 칸에 자신의 기호로 표시한다.
# 2. 다른 플레이어가 아직 기록되지 않은 빈 칸에 자신의 기호로 표시한다.
# 3. 둘 중 한 플레이어가 가로, 세로 또는 대각선을 자신의 기호만으로 채우면 승리한다.
# 4. 게임은 한 플레이어가 승리하거나 빈 칸이 남지 않아 비길 때까지 계속된다.

# ======================================================
# 틱택토 게임 설계
# ======================================================

# 1. 2차원 리스트를 사용하여 게임판을 생성하고 각각의 칸을 빈칸으로 초기화
#   빈칸에 대한 지정한 기호(*)를 사용

# 2. 게임판에 빈칸이 남아있는지 확인
#   게임판 전체를 확인하고 True/False 반환

# 3. 둘 중 한 플레이어가 승리했는지 확인
#   8가지의 승리 상황에 따른 가능성을 확인
#   각각의 행, 열과 두 개의 대각선 방향을 확인

# 4. 게임판의 현재 상태를 출력

# 5. 게임 시작
#   무작위로 선공할 플레이어를 선택
#   게임 루프를 기동
#   게임판의 현재 상태를 출력하고 다음 플레이어가 빈칸을 선택
#   플레이어가 선택할 빈칸의 위치(행과 열 번호)를 입력받음

#   플레이어가 선택한 위치에 기호를 표시하고 게임판을 업데이트
#   현재 플레이어가 승리했는지 확인

#   게임판에 빈칸이 남아있는지 확인
#       승리 상황인 경우, 승리한 플레이어에 대한 메시지를 출력하고 게임 루프를 종료

#       사용자일 경우 사용자 입력을 통해 행과 열 번호를 입력받음
#       컴퓨터일 경우 무작위로 행과 열 번호를 선택

#       게임판이 가득찬 경우, 무승부 메시지를 출력하고 게임 루프를 종료

# ======================================================
import random

class Tic_Tac_Toe:

    ### 게임판 생성
    def __init__(self) : # 클래스에서 객체가 만들어질 때 자동적으로 호출, 초기화. 항상 __init__으로 명명
        self.board = [] # 게임판을 저장할 리스트

    ### 게임판 초기화
    def create_board(self) :
        for i in range(3) :
            row = [] # 1.하나의 행 생성
            for j in range(3) :
                row.append('*') # 2.'*'로 채운 3개의 칸 만들기
            self.board.append(row) # slef.board판에 1~2에서 만든 row 넣음

    ### 첫 플레이어 선택
    def select_first_player(self) :
        if random.randint(0, 1) == 0 : # range(0,3) 범위는 0,1,2를 의미하는데 반해, randint(0,3) 범위는 0,1,2,3을 의미함
            return 'X' # 컴퓨터(X)가 첫 플레이어
        else :
            return 'O' # 사용자(O)가 첫 플레이어

    ### 기호 표시
    def mark_spot(self, row, col, player) :
        self.board[row][col] = player
        
    ### 승리 상태 확인
    def is_win(self, player) :

        n = len(self.board) # board가 가리키는 리스트의 원소의 개수 추출

        ### 행 확인
        for i in range(n) :
            win = True
            for j in range(n) :
                if self.board[i][j] != player : # 행의 모든 칸이 player의 기호로 채워져 있는지 확인
                    win = False
                    break
            if win == True :
                return win
            
        ### 열 확인 
        for i in range(n) :
            win = True
            for j in range(n) :
                if self.board[j][i] != player :
                    win = False
                    break
            if win == True :
                return win

        ### 오른쪽 대각선 확인
        win = True
        for i in range(n) :
            if self.board[i][i] != player :
                win = False
                break
        if win == True :
            return win
    
        ### 왼쪽 대각선 확인
        win = True
        for i in range(n) :
            if self.board[i][n - i - 1] != player :
                win = False
                break
        if win == True :
            return win

        return False # 위의 모든 경우에 해당하지 않는 경우 False 반환

    ### 잔여 빈칸 여부 확인
    def is_board_full(self) :
        for row in self.board :
            for item in row :
                if item == '*' :
                    return False
                
        return True

    ### 플레이어 변경
    def next_player(self, player) :
        if player == 'O' :
            return 'X'
        else :
            return 'O'
        
        #return 'X' if player == 'O' else 'O' # 파이썬의 삼항 연산자 사용

    ### 현재 게임판 상태 출력
    def show_board(self) :
        for row in self.board :
            for item in row :
                print(item, end=" ")
            print()

    ### 게임 시작
    def start(self) :

        ### 새 게임판 생성
        self.create_board()
        self.show_board() # 게임판 상태 출력

        ### 첫 플레이어 선택
        player = self.select_first_player()

        ### 게임 루프 시작
        while True :

            ### 다음 플레이어 안내
            if player == 'X' :
                print("컴퓨터 차례입니다.")
            else :
                print("사용자 차례입니다.")

            ### 현재 게임판 상태 출력
            self.show_board()

            ### 사용자 입력 대기, 컴퓨터일 경우 랜덤 위치 반환
            if player == 'X' :
                while True :
                    row, col = random.randint(1, 3), random.randint(1, 3) # 컴퓨터는 무작위로 행과 열 선택
                    if self.board[row - 1][col - 1] == '*' :
                        break
            
                print("컴퓨터가 행 " + str(row) + ", 열 " + str(col) + "을/를 선택했습니다.")
                print()
            else : # 사용자 입력 받기
                row, col = list(map(int, input("선택할 빈칸의 위치를 입력하세요(예: 1 3) : ").split())) # map 함수 : 1. 리스트 각각의 요소에 함수를 적용해주는 역할 2.input으로 입력받은 위칫값에 (정수로 바꾸는 함수인) int 함수 적용 3. 마무리: 어떤 형태로 만들어 주어야 하는지 명시
                print("사용자가 행 " + str(row) + ", 열 " + str(col) + "을/를 선택했습니다.")
                print()

            ### row, col 입력값이 0, 0인 경우 게임 종료
            if row == 0 and col == 0 :
                print("게임을 종료합니다.")
                break
            
            ### 입력된 위치 표시
            self.mark_spot(row - 1, col - 1, player)
            self.show_board()

            ### 현재 플레이어가 이겼는지 확인 
            if self.is_win(player) == True :
                if player == 'X' :
                    print("컴퓨터가 이겼습니다. 다시 도전하세요.")
                else :  
                    print("사용자가 이겼습니다. 축하합니다")
                
                break

            ### 게임판 가득참 확인, 빈칸 여부 확인
            if self.is_board_full() == True :
                print("무승부입니다. 다시 도전하세요.")
                break

            ### 플레이어 변경
            player = self.next_player(player)

        ### 최종 게임판 출력
        print()
        self.show_board()


### 게임 생성
TTT = Tic_Tac_Toe()

### 게임 시작
TTT.start()