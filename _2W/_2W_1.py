# 코드 1.6: 하노이의 탑
import time
count = 0
def hanoi_tower(n, fr, tmp, to) :
    global count
    if (n == 1) :
        print("원판 1: %s --> %s" % (fr, to))
        count +=1
    else :
        hanoi_tower(n - 1, fr, to, tmp)
        print("원판 %d: %s --> %s" % (n, fr, to))
        hanoi_tower(n - 1, tmp, fr, to)
        count +=1



# 테스트 프로그램
recive = int(input("원하는 층 수를 입력하세요"))
start = time.time()
hanoi_tower(recive, 'A', 'B', 'C')
end = time.time()
print("총 함수 실행 횟수:", count)
print("총 실행 시간: %.5f 초" % (end - start))
