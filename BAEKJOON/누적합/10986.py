'''
수가 n개 주어졌을 때,
연속된 부분 구간의 합이 m으로 나누어 떨어지는 구간의 개수를 구해야한다.

예를 들어
입력이
n = 5, m = 3이고,
1 2 3 1 2 가 주어졋으면,
3으로 나누어 떨어지는 부분 구간은,

3
1 2
1 2
1 2 3
3 1 2
2 3 1
1 2 3 1 2

이렇게 총 7개다.

이것을 어떻게 하면 쉽게 구할 수 있을까?

i)
일단은 누적합 테이블을 작성해보는 것은 어떨까?
위의 예제를 그대로 사용해서 누적합 테이블을 작성해보면,
[0, 1, 3, 6, 7, 9]
이다.

구간의 부분합을 구하는 방법으로 구해보면,

3
6
9
6
3
6
3
이렇게 총 7가지가 나온다.

위에서 7가지 나온 것과 동일한 갯수다.
이런 방식으로 하면되려나? 한번 코드를 짜서 확인해보자.

위의 방식을 코드로 작성해서 돌려보니, 시간초과가 뜬다.

ii)
흠.. 일단 바로 보이는 비효율적인 부분은, 이중 포문인데,
저걸 어떻게 해결할 수 있을까?


m으로 누적합 리스트를 계속 나누면 어떨까?
[0, 1, 3, 6, 7, 9]
m으로 나누어 지는 경우 //m
[0, 0, 1, 2, 0, 3] -> 1 + 2 + 3  -> 6
[0, 0, 0, 0, 0, 1] -> 6 + 1 -> 7
[0, 0, 0, 0, 0, 0] 끝

m으로 나누어 지지 않는 경우 (나머지로 구성한 테이블)
[0, 1, 0, 0, 1, 0]


7개가 맞긴한데? 우연의 일치겠지? 일단 구현해보자.


iii)
또 시간초과가 뜬다.
그러면 생각한 방법 자체는 맞는다는 건데..

또 보면 포문이 두개 쓰이긴 했다.
이걸 줄일 방법을 생각해보자.

- (A + B) % C = ((A % C) + (B % C)) %C 이다.

예를 들어서 m = 3이라면,
((1 % 3) + (2 % 3)) % 3 값과
(1 + 2) % 3 의 값은 동일하다.

그리고 당연한 이야기지만,
- 구간 합 배열을 이용한 식 S[i] - S[j] 는 원본 리스트 A의 A[j + 1]부터 A[i] 까지의 구간 합이다.

원본리스트 A[0, 1, 2, 3, 4, 5, 6]
누적리스트 S[0, 1, 3, 6, 10, 15, 21] 이면
S[5] - S[2] = 12
A[3] + A[4] + A[5] = 3 + 4 + 5 = 12

- 한 배열의 원소를 M으로 나눈 나머지로 업데이트하고 S[i]와 S[j]가 같은 (i, j)쌍을 찾으면 원본 리스트에서 j + 1 부터 i 구간의 합이 M으로 나누어 떨어진다는 것을 알 수 있다.
원본 A[3, 2, 4, 5, 1]
누적 S[3, 5, 9, 14, 15]
m = 3
m으로 나눈 나머지로 누적 배열을 업데이트 해보자.
누적 S[0, 2, 0, 2, 0]
2, 2가 같으니까 이걸로 예시를 들어보면,
S[3] - S[1] 을 하게되면 A[2] + A[3] 이 m으로 나누면 나머지가 0이다.

즉, 누적 합배열을 m으로 나눈 나머지 값으로 업데이트를 하고,
인덱스 0을 제외한 0의 갯수를 세서 answer 에 그 수를 더해준다.
그리고,
나머지가 같은 구간을 찾아서 서로 빼주면 같은 값을 갖고 있으면 빼면 0이 되므로 이는 곧 m으로 나누어 떨어짐을 의미한다.
그렇다면, 누적합을 m으로 나눈 나머지로 업데이트한 배열에서 0이 아니면서 서로 같은 값을 가지는 수를 인덱스로 하는 배열을 생성해서  해당 배열에 개수를 갱신하고,
배열에 저장된 각 수의 콤비네이션 값을 구해서 answer에 더해주면 된다.

ex) 누적 합 배열을 m으로 나눈 나머지 배열을 s라고 가정하자. s[0, 0, 0, 1, 0, 1, 0] 이라고 가정하면,
s에서 0이 아닌데 같은 나머지를 갖는 것은 인덱스 3의 1, 인덱스 5의 1이  즉 1 2개다.
그러면 m + 1의 크기를 갖는 배열을 생성하고, 그 배열의 인덱스 1에 2를 갱신해준다. m이 3이라고 가정하면 [0, 2, 0, 0] 이렇게 된다.
그러면 해당 배열을 돌면서 각 요소의 콤비네이션 값을 구해서 answer에 더해주면 된다.

'''
import sys

# 정답 변수
answer = 0

# 수의 갯수 n, 나눌 값 m
n, m = map(int, sys.stdin.readline().rstrip().split())
# print('n =', n, 'm =', m)

# 수열 입력받기
table = list(map(int, sys.stdin.readline().rstrip().split()))
table.insert(0, 0)
# print('입력 받은 table =', table)

# 누적합 테이블 생성
accum_table = [0] * (n+1)
# print(accum_table)

# 누적합의 나머지 값 저장 할 테이블 생성
remainder_list = [0] * (m + 1)

# 누적합 테이블 갱신
for i in range(1, n + 1):
    if accum_table[i - 1] != 0:
        accum_table[i] = accum_table[i - 1] + table[i]
    else:
        accum_table[i] = table[i]


for i in range(1, n + 1):
    remainder = accum_table[i] % m
    # 누적합의 나머지 값이 0이면 answer에 +1을 해주고,
    if remainder == 0:
        answer = answer + 1
    remainder_list[remainder] = remainder_list[remainder] + 1 # remainder_list에 나머지 값에 해당하는 인덱스에 + 1

for i in range(m + 1):
    if remainder_list[i] > 1:
        # 같은 나머지 값이 2개 이상이면 콤비네이션 만큼 answer에 더해주기 ex) 3C2 = (3 * 2) / (2 * 1)
        answer = answer + (remainder_list[i] * (remainder_list[i] - 1)) // 2



print(answer)