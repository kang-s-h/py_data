# Selection Sort
def selection_sort(arr):
    comparisons = 0
    movements = 0
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            movements += 2
    return arr, comparisons, movements

# Insertion Sort
def insertion_sort(arr):
    comparisons = 0
    movements = 0
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                movements += 1
                j -= 1
            else:
                break
        arr[j + 1] = key
        movements += 1
    return arr, comparisons, movements
 # 1회전 제자리 값에서 이동 안해도 체크됨 
# Bubble Sort
def bubble_sort(arr):
    comparisons = 0
    movements = 0
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                movements += 2
    return arr, comparisons, movements

# Shell Sort
def shell_sort(arr):
    comparisons = 0
    movements = 0
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap:
                comparisons += 1
                if arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    movements += 1
                    j -= gap
                else:
                    break
            arr[j] = temp
            movements += 1
        gap //= 2
    return arr, comparisons, movements

# Heap Sort
def heapify(arr, n, i, stats):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n:
        stats["comparisons"] += 1
        if arr[l] > arr[largest]:
            largest = l
    if r < n:
        stats["comparisons"] += 1
        if arr[r] > arr[largest]:
            largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        stats["movements"] += 2
        heapify(arr, n, largest, stats)

def heap_sort(arr):
    stats = {"comparisons": 0, "movements": 0}
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, stats)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        stats["movements"] += 2
        heapify(arr, i, 0, stats)
    return arr, stats["comparisons"], stats["movements"]

# Merge Sort
def merge_sort(arr):
    global comparisons, movements
    comparisons = 0
    movements = 0

    def merge(left, mid, right):
        global comparisons, movements
        n1 = mid - left + 1
        n2 = right - mid
        L = arr[left:left + n1]
        R = arr[mid + 1:mid + 1 + n2]
        i = j = 0
        k = left
        while i < n1 and j < n2:
            comparisons += 1
            if L[i] <= R[j]:
                arr[k] = L[i]
                movements += 1
                i += 1
            else:
                arr[k] = R[j]
                movements += 1
                j += 1
            k += 1
        while i < n1:
            arr[k] = L[i]
            movements += 1
            i += 1
            k += 1
        while j < n2:
            arr[k] = R[j]
            movements += 1
            j += 1
            k += 1

    def merge_recursive(left, right):
        if left < right:
            mid = (left + right) // 2
            merge_recursive(left, mid)
            merge_recursive(mid + 1, right)
            merge(left, mid, right)

    merge_recursive(0, len(arr) - 1)
    return arr, comparisons, movements

# Quick Sort
def quick_sort(arr):
    global comparisons, movements
    comparisons = 0
    movements = 0

    def partition(low, high):
        global comparisons, movements
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            comparisons += 1
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                movements += 2
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        movements += 2
        return i + 1

    def quick_sort_recursive(low, high):
        if low < high:
            pi = partition(low, high)
            quick_sort_recursive(low, pi - 1)
            quick_sort_recursive(pi + 1, high)

    quick_sort_recursive(0, len(arr) - 1)
    return arr, comparisons, movements

# Radix Sort
from queue import Queue

def radix_sort(arr):
    comparisons = 0
    movements = 0
    max_digit = len(str(max(arr)))
    queues = [Queue() for _ in range(10)]
    for d in range(max_digit):
        factor = 10 ** d
        for num in arr:
            bucket = (num // factor) % 10
            queues[bucket].put(num)
            movements += 1
        idx = 0
        for queue in queues:
            while not queue.empty():
                arr[idx] = queue.get()
                movements += 1
                idx += 1
    return arr, comparisons, movements

# Main Program
if __name__ == "__main__":
    algo_map = {
        "SEL": selection_sort,
        "INS": insertion_sort,
        "BUB": bubble_sort,
        "SHE": shell_sort,
        "HEA": heap_sort,
        "MER": merge_sort,
        "QUI": quick_sort,
        "RAD": radix_sort,
    }

    data = list(map(int, input("Please input a data list: ").split(',')))
    print("Target Sorting Algorithm List:")
    print("Selection(SEL), Insertion(INS), Bubble(BUB), Shell(SHE), Heap(HEA), Merge(MER), Quick(QUI), Radix(RAD)")
    algo = input("Select sorting algorithm: ").strip().upper()

    if algo in algo_map:
        sorting_function = algo_map[algo]
        original_data = data[:]
        sorted_data, comparisons, movements = sorting_function(data)
        print(f">> Sorted: {', '.join(map(str, data))}")
        print(f">> Number of Comparisons: {comparisons}")
        print(f">> Number of Data Movements: {movements}")
    else:
        print("Invalid algorithm selection.")