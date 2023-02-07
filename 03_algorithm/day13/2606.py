import sys
sys.stdin = open("input.txt")

def pprint(arr):
    for row in arr:
        print(row)
# 인접 행렬 풀이
# 정점의 수
N = int(input())

# 간선의 수
M = int(input())

# 인정 행렬
graph = []
for _ in range(N+1):
    temp = [0] * (N+1)
    graph.append(temp)

# pprint(graph)
# 정점의 쌍 입력(간선만큼)
for _ in range(M):
    node1, node2 = list(map(int,input().split()))
    
    # (node1, node2) -> 간선 표현
    graph[node1][node2] = 1

    # (node2, node1) -> 간선 표현
    graph[node2][node1] = 1

# 시작점
start = 1

# 스택, 방문 확인 변수
stack = [] 
visit = set()

# 시작점을 스택에 넣고, 방문 표시
stack.append(start)
visit.add(start)

# 무한 반복 -> 스택에 값이 있을 때
while len(stack) != 0:
    # 스택에서 값을 꺼내기
    current_node = stack.pop()
    print(current_node)

    for index_node in range(N+1):
        # print(f"확인 정점 : {index_node}")
        # print(f"간선 여부 : {graph[current_node][index_node]}")
        
        # 인접한 정점 -> 간선 여부가 1인
        # 인접 정점 확인
        if graph[current_node][index_node] == 1:
            # 방문 확인
            if index_node not in visit:
                # 스택에 인접 정점 append
                stack.append(index_node)
                # 인접 정점 방문 표시
                visit.add(index_node)


"""
# 인접리스트 풀이
# 정점의 수
N = int(input())

# 간선의 수
M = int(input())

# 그래프 표현 방법 1
# 인접 리스트
# 리스트의 수는 노드의 수(N)
# N + 1 만큼 리스트를 가진 리스트
graph = []
for _ in range(N+1):
    graph.append([])



# print(graph)

# 정점의 쌍 입력(간선만큼)
for _ in range(M):
    node1, node2 = list(map(int,input().split()))

    # 양방향 그래프
    # node1의 인접리스트에 node2를 추가
    graph[node1].append(node2)
    
    # node2의 인접리스트에 node1을 추가
    graph[node2].append(node1)

    # print(node1, node2) 

### 템플릿 1번
# 시작점 
start = 1


### 템플릿 2번
# 스택
stack = [] 

# 방문 여부를 확인할 변수
# visit = [False] * (N + 1)

# 중복을 확인할 때 사용하는 자료구조?
# set 데이터 타입을 활용해서 방문 여부를 확인 가능
# set의 탐색 시간 복잡도 -> O(1)
visit = set()

### 템플릿 3번
# 시작점 스택에 넣기
stack.append(start)
# 시작점 방문 표시
visit.add(start)

visit_count = 0

### 템플릿 4번
while len(stack) != 0:
    # 템플릿 5-1
    current_node = stack.pop()
    # print(current_node)
    
    # 템플릿 5-2
    adj_graph = graph[current_node]
    
    # 템플릿 5-3
    for node in adj_graph:
        # 미방문 확인
        if node not in visit:
            # 템플릿 5-3-1
            stack.append(node)
            
            # 템플릿 5-3-2
            visit.add(node)

            # 방문한 횟수 + 1
            visit_count += 1


# 문제에서 요구하는 것
# 1번 컴퓨터와 연결된 모든 컴퓨터의 수
# 방문한 모든 노드의 수
# 방문한 횟수
# 방문한 횟수 == 1번 컴퓨터와 연결된 모든 컴퓨터 수
print(visit_count)
"""