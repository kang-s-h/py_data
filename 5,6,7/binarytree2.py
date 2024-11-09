from binarytree import BSTMap

if __name__ == "__main__":
    data = [35, 18, 7, 26, 12, 3, 68, 22, 30, 99]
    value= ["삼오", "일팔", "영칠", "이육", "일이", "영삼", "육팔", "이이", "삼영", "구구"]

    map = BSTMap()
    map.display("[삽입 전] : ")
    for i in range(len(data)) :
        map.insert(data[i], value[i])
        map.display("[삽입 %2d] : " % data[i])

    print('[최대 키] : ', map.findMax().key)
    print('[최소 키] : ', map.findMin().key)
    print('[탐색 26] : ', '성공' if map.search(26) != None else '실패')
    print('[탐색 25] : ', '성공' if map.search(25) != None else '실패')
    print('[탐색 일팔]:', '성공' if map.searchValue("일팔") != None else '실패')
    print('[탐색 일칠]:', '성공' if map.searchValue("일칠") != None else '실패')

    map.delete(3)
    map.display("[삭제  3] : ")
    map.delete(68)
    map.display("[삭제 68] : ")
    map.delete(18)
    map.display("[삭제 18] : ")
    map.delete(35)
    map.display("[삭제 35] : ")

    print("\nIn-Order Traversal:")
    map.display(order=1)
    print("\nPre-Order Traversal:")
    map.display(order=2)
    print("\nPost-Order Traversal:")
    map.display(order=3)