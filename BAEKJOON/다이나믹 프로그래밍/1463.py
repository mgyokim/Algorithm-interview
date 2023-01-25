'''
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지이다.
1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
2. X가 2로 나누어 떨어지면, 2로 나눈다.
3. 1을 뺀다.

정수 N이 주어졌을 떄, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 할 때,
연산을 사용하는 횟수의 최솟값을 구해서 출력해야 한다.

i)
가장 쉬운 방법으로는, 어떤 수N이 주어지면,
해당 N을 위에서 주어진 3개의 연산을 사용해서 연산을 사용할 때마다 횟수 변수에 +1로 카운팅을 하고 N이 1이 되었을 때의 count를 출력하면 될 것이다.

그런데, 문제이 입력 조건을 보면, n은 최대값이 10^6이다. 1000000(백만) 이다.
1000000에 대하여 위의 연산만을 이용하여 1을 만들려면, 시간 제한 0.15초 만에 해결 할 수 없을 것으로 예상된다.

즉, 다른 로직을 생각해 봐야 한다.
dp 테이블을 만들고, 해당 DP테이블의 각 요소값은, 해당 인덱스 값이 1이 되는데 필요한 연산 횟수를 저장한다.
예를 들어 d[1]은 0으로 1이 1로 되는데 필요한 연산은 0회이기 때문이다.
d[2]는 2가 1이 되는데 필요한 최소 연산 횟수인 1이 될 것이다.

n을 가능한 큰 수인 3으로 먼저 나누어 떨어진다면 해당 연산을 진행하는게 유리해보이지만, 실제로는 그렇지 않다.
3으로 나누어 떨어진다고해서 무조건 먼저 3으로 나눈 것이 이득이 아니다.

생각해보자.

n을 연산하여 1로 만들 때,
예를 들어 30을 생각해보자.
30을 3으로 나누면 10
10을 2로 나누면 5
5에서 1을 빼면 4
4를 2로 나누면 2
2에서 1을 빼면 1

총 5번의 연산을 진행했다.
하지만 30으로 1로 만드는 최소 연산 횟수는 5번이 아니다.
30을 3으로 나누면 10
10에서 1을 빼면 9
9를 3으로 나누면 3
3을 3으로 나누면 1
총 4번

30을 1로 만드는 최소 연산 횟수는 4번이다.

i)
그렇다면, 우리는 연산을 진행할 때,
현재 n을 -1할지, //3 할지, // 2 할지 비교하여 가장 작은 값으로 dp테이블을 갱신할 수 있을 것이다.
그렇다면,
1. n이 2와 3으로 나누어 떨어지는 경우,
2. n이 2로만 나누어 떨어지는 경우,
3. n이 3으로만 나누어 떨어지는 경우
4. n이 2와 3으로 나누어 떨어지지 않는 경우
이렇게 4가지로 나누어 dp테이블을 갱신할 수 있을 것이다.

구현 해보자.
'''

import sys

n = int(sys.stdin.readline().rstrip())

dp = [0] * int(n + 1)

for i in range(2, n + 1):
    if i % 2 == 0 and i % 3 == 0:   # 현재 i가 2와 3으로 나누어 떨어지는 경우
        dp[i] = min(dp[i // 2], dp[i // 3], dp[i - 1]) + 1
    elif i % 3 == 0:    # 현재 i가 3으로 나누어 떨어지는 경우
        dp[i] = min(dp[i - 1] + 1, dp[i // 3] + 1)
    elif i % 2 == 0:    # 현재 i가 2로 나누어 떨어지는 경우
        dp[i] = min(dp[i - 1] + 1, dp[i // 2] + 1)
    else:   # 현재 i가 2와 3으로 나누어 떨어지지 않는 경우
        dp[i] = dp[i - 1] + 1

print(dp[n])
