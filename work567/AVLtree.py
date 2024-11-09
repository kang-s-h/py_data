from BinaryTree3 import count_node, count_leaf, calc_height
from BinSrchTree import BSTNode, delete_bst

def calc_height_diff(n):
    if n is None:
        return 0
    return calc_height(n.left) - calc_height(n.right)

def rotateLL(A):
    B = A.left
    A.left = B.right
    B.right = A
    return B

def rotateRR(A):
    B = A.right
    A.right = B.left
    B.left = A
    return B

def rotateRL(A):
    B = A.right
    A.right = rotateLL(B)
    return rotateRR(A)

def rotateLR(A):
    B = A.left
    A.left = rotateRR(B)
    return rotateLL(A)

def reBalance(parent):
    hDiff = calc_height_diff(parent)

    if hDiff > 1:
        if calc_height_diff(parent.left) > 0:
            parent = rotateLL(parent)
        else:
            parent = rotateLR(parent)
    elif hDiff < -1:
        if calc_height_diff(parent.right) < 0:
            parent = rotateRR(parent)
        else:
            parent = rotateRL(parent)
    return parent

def insert_avl(parent, node):
    if node.key < parent.key:
        if parent.left is not None:
            parent.left = insert_avl(parent.left, node)
        else:
            parent.left = node
        return reBalance(parent)

    elif node.key > parent.key:
        if parent.right is not None:
            parent.right = insert_avl(parent.right, node)
        else:
            parent.right = node
        return reBalance(parent)
    else:
        print("중복된 키 에러")

def delete_avl(root, key):
    root = delete_bst(root, key)
    if root is not None:
        root = reBalance(root)
    return root

def levelorder(root):
    from CircularQueue import CircularQueue
    queue = CircularQueue(100)
    queue.enqueue(root)
    while not queue.isEmpty():
        n = queue.dequeue()
        if n is not None:
            print(n.key, end=' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)

if __name__ == "__main__":
    node = [7, 8, 9, 2, 1, 5, 3, 6, 4]
    root = None
    for i in node:  
        n = BSTNode(i)
        if root is None:
            root = n
        else:
            root = insert_avl(root, n)

        print("AVL(%d): " % i, end='')
        levelorder(root)
        print()

    print(" 노드의 개수 =", count_node(root))
    print(" 단말의 개수 =", count_leaf(root))
    print(" 트리의 높이 =", calc_height(root))

    # 삭제 연산 테스트
    delete_keys = [3, 4, 8]
    for key in delete_keys:
        root = delete_avl(root, key)
        print("After deleting %d: " % key, end='')
        levelorder(root)
        print()