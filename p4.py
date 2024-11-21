class CircularQueue:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.array = [None] * capacity
        self.front = 0
        self.rear = 0

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.front == (self.rear + 1) % self.capacity

    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = item
        else:
            print("큐가 가득 찼습니다. 요소를 삽입할 수 없습니다.")

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            removed_item = self.array[self.front]
            self.array[self.front] = None  # 삭제된 요소를 None으로 초기화
            return removed_item
        else:
            print("큐가 비어 있습니다. 요소를 삭제할 수 없습니다.")
            return None

    def size(self):
        return (self.rear - self.front + self.capacity) % self.capacity

    def __str__(self):
        if self.isEmpty():
            return "[]"
        elements = []
        i = (self.front + 1) % self.capacity
        while i != (self.rear + 1) % self.capacity:
            elements.append(self.array[i])
            i = (i + 1) % self.capacity
        return str(elements)

# 테스트 프로그램
if __name__ == "__main__":
    queue = CircularQueue(10)  # 용량 10인 원형 큐 생성

    while True:
        command = input("[메뉴선택] e-삽입(enqueue), d-삭제(dequeue), q-종료 => ")

        if command == 'e':
            element = input("  삽입할 요소를 입력하세요: ")
            queue.enqueue(element)
            print("큐 상태:", queue)

        elif command == 'd':
            removed_element = queue.dequeue()
            if removed_element is not None:
                print(f"삭제된 요소: {removed_element}")
            print("큐 상태:", queue)

        elif command == 'q':
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 명령어입니다. 다시 입력해주세요.")
