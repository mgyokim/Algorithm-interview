'''
1번부터 N번까지 총 N개의 문제로 되어 있는 문제집을 풀려고함.
문제 난이도는 순서대로 출제되어 있음. 1번문제가 가장 쉬운 문제, N번 문제가 가장 어려운 문제.
먼저풀면 좋은문제가 있다는 것을 알게되어, 다음의 세가지 조건에 따라 문제를 풀 순서를 정하기로 함.
1. N개의 문제는 모두 풀어야함.
2. 선수 문제가 있는 문제는, 반드시 선수문제 먼저 풀어야함
3. 가능하면 쉬운 문제부터 풀어야함.

ex) 4개의 문제가 있다고 가정하자. 4번 문제는 2번 문제보다 먼저 푸는 것이 좋고, 3번 문제는 1번 문제보다 먼저 푸는 것이 좋다고함.
만일, 4-3-2-1의 순서로 문제를 풀게되면 조건 1과 조건 2를 만족함. 하지만 조건 3을 만족하지 않음. 왜냐하면 4보다 3을 충분히 먼저 풀 수 있기 때문.
따라서 조건 3을 만족하는 문제풀기 순서는 3-1-4-2가 된다.

- 입력
첫째 줄에 문제의 수 N(1 <= N <= 32,000)과 선수문제의 개수 M(1 <= M <= 100,000)이 주어짐.
둘째 줄부터 M개의 줄에 걸쳐서 두 정수 A와 B가 빈칸을 사이에 두고 주어짐. 이는 A번 문제는 B번 문제보다 먼저 푸는 것이 좋다는 의미이다.
항상 문제를 모두 풀 수 있는 경우만 입력으로 주어짐.

- 출력
첫째 줄에 풀어야 하는 순서대로 공백을 사이에 두고 문제 번호를 출력


i) 위의 예시를 토대로 생각을 해보자.
선수문제 관계에 있는 것을 그래프로 생각하자.
그러면 3번 노드는 1번 노드를 가리킬 것이고, 4번 노드는 2번 노드를 가리킬 것이다.
3번 노드와 4번 노드 중 더 쉬운 문제는 3번 노드이다.
그러면 3번 노드를 먼저 풀고나면(1번의 진입차수를 -1해줌), 우리가 풀 수 있는 문제는 진입차수가 0인 1번 노드와 4번 노드가 된다.
그런데, 1번 노드가 4번 노드보다 더 쉬운 문제이므로 1번 노드를 풀 것이다.
그러면 남은 노드는 4번 노드와 2번 노드인데, 진입차수가 0인 4번 노드를 먼저 풀고, 그다음 2번 노드를 풀면 될 것이다.

전형적인 위상 정렬 로직으로 판단된다.
위상정렬 로직으로 구현해보자.

ii)
큐를 이용하여 일반적인 위상정렬을 구현해보니,
3-1-4-2 가 아니라 3-4-1-2가 나온다 이유를 고민해보니,
처음에 진입차수가 0인 3과 4가 큐에 들어가는데, 3을 처리하면서 1의 진입차수가 0이되어 큐에 들어가도 큐에는 4가 있는 상태라서 4, 1 이렇게 큐에 존재하게 된다.
그러면 큐의 popleft 특성상 4가 나오게 되서 발생하는 문제다.
우리는 진입차수가 0인 4와 1이 있으면, 문제의 난이도가 더 낮은 1이 나와야 한다.

heapq를 이용하자.
파이썬의 heapq는 기본적으로 최소힙이기 때문에, 넣었다가 빼는 것 만으로도 오름차순 정렬이 된다.
어차피 큐에 들어가는 것들은 진입차수가 0인 것들이기 때문에, 그 안에서 최솟값을 찾아서 뽑아주면 된다.
heapq가 제격이다.
'''

# 문제의 수 n, 선수 문제의 개수 m
import sys
import heapq

n, m = map(int, input().split())

# 문제간의 정보를 저장 할 그래프
graph = [[] for i in range(n + 1)]

# 문제의 진입차수(선수문제)를 저장하기 위한 리스트
indegree = [0 for i in range(n + 1)]
for i in range(m):
    first, last = map(int, sys.stdin.readline().rstrip().split())
    graph[first].append(last)
    indegree[last] = indegree[last] + 1

def topology_sort():
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = [] # 문제번호가 작은 순서대로 정렬하기 위한 힙큐

    # 처음 시작할 때는 진입 차수가 0인 노드를 큐에 삽입 (단, 문제 번호가 작은 것 부터)
    for i in range(1, n + 1):
        if indegree[i] == 0:
            heapq.heappush(q, i)

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = heapq.heappop(q)
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1빼기
        for j in graph[now]:
            indegree[j] = indegree[j] - 1
            # 새롭게 진입 차수가 0이 되는 노드를 큐에 삽입
            if indegree[j] == 0:
                heapq.heappush(q, j)

    # 위상 정렬 수행 결과 출력
    for i in result:
        print(i, end = ' ')


topology_sort()