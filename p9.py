INF = 9999

def get_path(path, start, end):
    if start == end:
        return []
    if path[start][end] == start:
        return []
    return get_path(path, start, path[start][end]) + [path[start][end]]

# Floyd 알고리즘
def shortest_path_floyd(vertex, adj):
    vsize = len(vertex)
    A = [list(row) for row in adj]
    path = [[-1 if i != j and adj[i][j] == INF else i for j in range(vsize)] for i in range(vsize)]

    for k in range(vsize):
        for i in range(vsize):
            for j in range(vsize):
                if A[i][k] + A[k][j] < A[i][j]:
                    A[i][j] = A[i][k] + A[k][j]
                    path[i][j] = path[k][j]

    return A, path

if __name__ == "__main__":
    # 가중치 그래프
    vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    weight = [
        [0,     7,  INF, INF, 3,    10, INF],
        [7,     0,  4,   10,  2,    6,  INF],
        [INF,   4,  0,   2,   INF,  INF, INF],
        [INF,   10, 2,   0,   11,   9,  4],
        [3,     2,  INF, 11,  0,    13, 5],
        [10,    6,  INF, 9,   13,   0,  INF],
        [INF,   INF, INF, 4,   5,    INF, 0]
    ]

    print("Floyd 알고리즘으로 최단 경로 구하기")
    distances, path = shortest_path_floyd(vertex, weight)

    start_vertex = input("시작 정점 입력: ").strip().upper()
    end_vertex = input("종료 정점 입력: ").strip().upper()

    if start_vertex not in vertex or end_vertex not in vertex:
        print("유효하지 않은 정점입니다. 그래프에 존재하는 정점을 입력하세요.")
        exit()

    start_idx = vertex.index(start_vertex)
    end_idx = vertex.index(end_vertex)

    if distances[start_idx][end_idx] == INF:
        print("입력된 두 정점 사이에 경로가 존재하지 않습니다.")
    else:
        shortest_path = [start_idx] + get_path(path, start_idx, end_idx) + [end_idx]
        shortest_path_vertices = " -> ".join(vertex[idx] for idx in shortest_path)
        print(f"최단 경로: {shortest_path_vertices}")
        print(f"최단 경로 거리: {distances[start_idx][end_idx]}")