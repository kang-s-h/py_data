import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(chars, freqs):
    heap = [Node(char, freq) for char, freq in zip(chars, freqs)]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heapq.heappop(heap)

def build_codes(node, prefix="", codebook={}):
    if node is not None:
        if node.char is not None:
            codebook[node.char] = prefix
        build_codes(node.left, prefix + "0", codebook)
        build_codes(node.right, prefix + "1", codebook)
    return codebook

def huffman_encoding(data, codebook):
    return ''.join(codebook[char] for char in data)

def calculate_compression_rate(original, encoded):
    original_bits = len(original) * 8
    encoded_bits = len(encoded)
    return (original_bits - encoded_bits) / original_bits * 100

if __name__ == "__main__":
    chars = ['k', 'o', 'r', 'e', 'a', 't', 'c', 'h']
    freqs = [10, 5, 2, 15, 18, 4, 7, 11]

    huffman_tree = build_huffman_tree(chars, freqs)
    codebook = build_codes(huffman_tree)

    while True:
        data = input("Please a word : ")
        if all(char in codebook for char in data):
            encoded_data = huffman_encoding(data, codebook)
            compression_rate = calculate_compression_rate(data, encoded_data)
            print(f"결과 비트 열: {encoded_data}")
            print(f"압축률: {compression_rate:.2f}%")
            break
        else:
            print("illegal character")