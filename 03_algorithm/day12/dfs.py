graph = [
    [1, 2],
    [0, 3, 4],
    [0, 4, 5],
    [1],
    [1, 2, 6],
    [2],
    [4]
]

visited = [False] * n  # 방문 처리 리스트 만들기

start = 0 # 시작 노드
stack = [start]
visited[start] = True  

# 방문 시작..
while stack: # 스택이 빌 때까지
    cur = stack.pop()  
    
    for adj in graph[cur]: 
        if not visited[adj]: 
            visited[adj] = True  
            stack.append(adj)

# 1. 0 
# stack : [0]
# visited : [True, False, False, False, False, False, False]
'''
cur = stack.pop()  
# current : 0

for adj in [1, 2]: # 0과 인접한 노드
    # 첫번째 시행 때 adj : 1
    if not visited[1]: # 방문을 안했으면 False니까 not으로 뒤집음!
        visited[adj] = True  # 방문 체크
        stack.append(adj) # 기록

    if not visited[2]: # 방문을 안했으면 False니까 not으로 뒤집음!
        visited[adj] = True  # 방문 체크
        stack.append(adj) # 기록
'''
# stack : [1, 2]