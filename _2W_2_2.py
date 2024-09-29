from _2W_2_1 import ArrayList

# 배열구조의 리스트를 이용한 라인 편집기 프로그램
list = ArrayList(1000)

while True:
    command = input("[메뉴선택] i-입력, d-삭제, r-변경, p-출력, l-파일읽기, s-저장, m-사전 만들기, q-종료=> ")

    if command == 'i':
        pos = int(input("  입력행 번호: "))
        str = input("  입력행 내용: ")
        list.insert(pos, str)

    elif command == 'd':
        pos = int(input("  삭제행 번호: "))
        list.delete(pos)

    elif command == 'r':
        pos = int(input("  변경행 번호: "))
        str = input("  변경행 내용: ")
        list.replace(pos, str)

    elif command == 'p':
        print('Line Editor')
        for line in range(list.size):
            print('[%2d] ' % line, end='')
            print(list.getEntry(line))
        print()

    elif command == 'q':
        exit()

    elif command == 'l':
        # filename = input("  읽어들일 파일 이름: ")
        filename = 'test.txt'
        infile = open(filename, "r")
        lines = infile.readlines()
        for line in lines:
            list.insert(list.size, line.rstrip('\n'))
        infile.close()

    elif command == 's':
        # filename = input("  저장할 파일 이름: ")
        filename = 'test.txt'
        outfile = open(filename, "w")
        len = list.size
        for i in range(len):
            outfile.write(list.getEntry(i) + '\n')
        outfile.close()

    elif command == 'm':  # 새로운 m 명령어 추가
        text = input("입력된 내용: ")  # 사용자로부터 입력받기
        word_count = {}
        words = text.split()
        for word in words:
            word = ''.join(filter(str.isalnum, word))  # 특수기호 제거
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        
        # 단어 출현 빈도수 출력
        print("단어 출현 빈도수:")
        for word, count in word_count.items():
            print(f"{word}: {count}")
        
        # 파일에 저장
        with open('dic.txt', 'w') as dic_file:
            for word, count in word_count.items():
                dic_file.write(f"{word}: {count}\n")
        print("단어 출현 빈도수가 dic.txt 파일에 저장되었습니다.")
