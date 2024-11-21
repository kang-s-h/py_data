# 코드 4.7: 미로의 깊이우선탐색 (참고 파일: ch04/MazeStack.py)
from  _2W_3_3 import ArrayStack

map =[[ '1', '1', '1', '1', '1', '1', '1' , '1' , '1' , '1'  ],
    [ 'e', '0', '1', '1', '1', '1', '1' , '1' , '1' , '1'  ],
    [ '1', '0', '1', '0', '1', '1', '1' , '1' , '1' , '1'  ],
    [ '1', '0', '0', '0', '0', '1', '1' , '0' , '1' , '1'  ],
    [ '1', '0', '1', '1', '1', '0', '0' , '0' , '0' , '1'  ],
    [ '1', '0', '0', '0', '0', '0', '1' , '0' , '1' , '1'  ],
    [ '1', '0', '1', '0', '1', '1', '1' , '0' , '1' , '1'  ],
    [ '1', '0', '1', '0', '0', '0', '1' , '0' , '0' , '1'  ],
    [ '1', '1', '1', '1', '1', '1', '1' , '1' , '0' , 'x'  ],
    [ '1', '1', '1', '1', '1', '1', '1' , '1' , '1' , '1'  ]]
MAZE_SIZE = 10


# 코드 4.7: 갈 수 있는 위치인지를 판단하는 알고리즘 (참고 파일: ch04/MazeStack.py)
def isValidPos(x, y) :		# (x,y)가 갈 수 있는 방인지 검사하는 함수
    if 0 <= x < MAZE_SIZE and 0 <= y < MAZE_SIZE :
        if map[y][x] == '0' or map[y][x] == 'x':
            return True
    return False


def DFS() :			# 깊이우선탐색 함수
    print('DFS: ')
    stack = ArrayStack(100)	# 사용할 덱 객체를 준비
    stack.push((0,1))		# 후단에 시작위치 삽입. (0,1)은 튜플
    distance = 0

    while not stack.isEmpty():  # 스택이 비어있지 않을 동안 반복
        here = stack.pop()      # 현재 위치를 스택에서 꺼냄
        print(here, end='->')   # 현재 위치 출력
        (x, y) = here

        if map[y][x] == 'x':    # 출구에 도달하면 성공
            return True, distance
        else:
            map[y][x] = '.'     # 지나온 경로 표시
            distance += 1       # 이동할 때마다 거리 증가

            # 상하좌우로 이동 가능한 위치 확인
            if isValidPos(x, y - 1): stack.push((x, y - 1))  # 상
            if isValidPos(x + 1, y): stack.push((x + 1, y))  # 우
            if isValidPos(x, y + 1): stack.push((x, y + 1))  # 하
            if isValidPos(x - 1, y): stack.push((x - 1, y))  # 좌

        print(' 현재 스택: ', stack)
    
    return False, distance

result, total_distance = DFS()
if result:
    print(' --> 미로탐색 성공')
else:
    print(' --> 미로탐색 실패')

print(f'총 이동거리: {total_distance}칸')