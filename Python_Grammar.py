# 부록A
# 코딩 테스트를 위한 파이썬 문법
print('-----------------------------------------------------------------------------------------------------------------------')
# 1. 자료형
# 수 자료형

# 정수형
# 정수형(Integer)은 정수를 다루는 자료형이며 정수형에는 양의 정수, 음의 정수, 0이 있다.

a = 1000    # 양의 정수
print(a)

a = -7      # 음의 정수
print(a)

# 0
a = 0
print(a)


# 실수형
# 실수형(Real Number)은 소수점 아래의 데이터를 포함하는 수 자료형으로 파이썬에서는 변수에 소수점을 분인 수를 대입하면 실수형 변수로 처리한다.
# 소수부가 0이거나, 정수부가 0인 소수는 0을 생략하고 작성할 수 있다.

# 양의 실수
a = 157.93
print(a)

# 음의 실수
a = -1837.2
print(a)

# 소수부가 0일 때 0을 생략
a = 5
print(a)

# 정수부가 0일 때 0을 생략
a = -7
print(a)
print('-----------------------------------------------------------------------------------------------------------------------')

# 실수형 데이터를 표현하는 방식으로 파이썬에서는 e나 E를 이용한 지수 표현 방식을 이용할 수 있다.
# e다음에 오는 수는 10의 지수부를 의미한다.
# 예를들어 1e9라고 입력하게 되면, 10의 9제곱(1,000,000,000)이 된다.
# 유효숫자e^지수 = 유효숫자 * 10^지수
# 예를 들어 최단 경로 문제에서는 도달할 수 없는 노드에 대하여 최단 거리르 '무한(INF)'로 설정하곤 한다.
# 최단 경로로 가능한 최댓값이 10억 미만이라면 무한(INF)를 표현할 때 10억을 이용할 수 있다.
# 또한 큰 수를 표현할 때, 0의 개수가 많아지게 되면 햇갈리므로 10억을 코드에 입력하는 것 보다는 1e9로 표현하는 것이 더 실수할 확률이 적다는 장점도 있다.
# 혹은 987,654,321라고 적으면 이게 1e9와 유사할 정도로 크므로 이렇게 적기도 한다.

# 10억의 지수 표현 방식
a = 1e9
print(a)

# 752.5
a = 75.25e1
print(a)

# 3.954
a = 3954e-3
print(a)
print('-----------------------------------------------------------------------------------------------------------------------')

# 보통 컴퓨터 시스템은 수 데이터를 처리할 때 2진수를 이용하며, 실수를 처리할 때 부동 소수점(Floating-point)방식을 이용한다.
# 오늘날 가장 널리 쓰이는 IEEE754 표준에서는 실수형을 저장하기 위해 4바이트, 혹은 8바이트라는 고정된 크기의 메모리를 할당하며,
# 이러한 이유로 인해 현대 컴퓨터 시스템은 대체로 실수 정보를 표현하는 정확도에 한계를 가진다.
# 예를 들어 10진수 체계에서는 0.3과 0.6을 더한 값이 0.9로 정확히 떨어지지만, 2진수에서는 0.9를 정확히 표현할 수 있는 방법이 없다.
# 물론 최대한 0.9와 가깝게 표현하지만 표현한 값이 정확히 0.9가 아닌 미세한 오차가 발생한다.
# 일반적으로 코딩 테스트 문제를 풀기 위해서 컴퓨터의 내부 동작 방식까지 자세히 알 필요는 없으나 컴퓨터가 실수를 정확히 표현하지 못한다는 사실은 기억하자.
# 다음 예시를 확인해보면, 0.3과 0.6을 더한 값이 0.8999999999999999로 저장되는 것을 알 수 있다.

a = 0.3 + 0.6
print(a)

if a == 0.9:
    print(True)
else:
    print(False)

# 따라서 소수점 값을 비교하는 작업이 필요한 문제라면 실수 값을 비교하지 못해서 원하는 결과를 얻지 못할 수 있다.
# 이럴 때는 round() 함수를 이용할 수 있다.
# round() 함수를 호출할 때는 인자(Argument)를 넣는데 첫 번째 인자는 실수형 데이터이고, 두 번째 인자는 (반올림하고자 하는 위치 -1)이다.
# 예를 들어 123.456을 소수점 셋째 자리에서 반올림 하려면 round(123.456, 2)라고 작성하며 결과는 123.45이다.
# (두 번째 인자 없이) 인자를 하나만 넣을 때는 소수점 첫째 자리에서 반올림한다.

# 다음은 round() 함수를 이용해서 소수점 특정 자릿수에서 반올림하는 예시이다.
# 흔히 코딩 테스트 문제에서는 실수형 데이터를 비교할 때 소수점 다섯 번째 자리에서 반올림한 결과가 같으면 정답으로 인정하는 식으로 처리한다.
# 그럴 때는 다음과 같이 round() 함수를 이용한다.

a = 0.3 + 0.6
print(round(a, 4))

if round(a, 4) == 0.9:
    print(True)
else:
    print(False)
print('-----------------------------------------------------------------------------------------------------------------------')

# 수 자료형의 연산
# 프로그래밍에서는 사칙연산(+, -, *, /)을 이용해 계산한다.
# 이 중에 나누기 연산자(/)를 주의해서 사용하자.
# 파이썬에서 나누기 연산자(/)는 나눠진 결과를 기본적으로 실수형으로 처리한다.
# 코딩 테스트 문제를 풀 때에는 나머지 연산자(%)를 이용해야 할 때가 많은데,
# 예를 들어 특정한 변수 a가 홀수인지 알아볼 때에는 'a를 2로 나눈 나머지가 1인지'확인한다.
# 이럴 때는 나머지 연산자(%)를 사용한다. 또한 나눈 결과에서 몫만을 얻고자 할 때는 몫 연산자(//)를 이용한다.

a = 7
b = 3

# 나누기
print(a / b)

# 나머지
print(a % b)

# 몫
print(a//b)

# 이 외에도 거듭제곱 연산자(**)를 비롯해 다양한 연산자 들이 존재한다.
# 거듭제곱 연산자는 x**y 형식으로 사용하는데 이는 x^y를 의미한다.

a = 5
b = 3

print(a ** b)
print('-----------------------------------------------------------------------------------------------------------------------')

# 리스트 자료형
# 리스트는 여러 개의 데이터를 연속적으로 담아 처리하기 위해 사용할 수 있다.
# 파이썬의 리스트 자료형은 C나 자바와 같은 프로그래밍 언어의 배열(Array) 기능을 포함하고 있으며,
# 내부적으로 연결 리스트 자료구조를 채택하고 있어서 append(), remove() 등의 메서드를 지원한다.
# 파이썬의 리스트는 C++의 STL, vector와 유사하며, 리스트 대신에 배열 혹은 테이블이라고 부르기도 한다.
print('-----------------------------------------------------------------------------------------------------------------------')

# 리스트 만들기
# 리스트는 대괄호 ([])안에 원소를 넣어 초기화하며, 쉼표(,)로 원소를 구분한다.
# 리스트의 원소에 접근할 때는 인덱스(Index) 값을 괄호 안에 넣는다.
# 이때 인덱스는 0부터 시작한다.
# 그리고 비어 있는 리스트를 선언하고자 할 때는 list() 혹은 간단히 대괄호([])를 이용할 수 있다.
# 1부터 9까지의 모든 정수 데이터를 담는 리스트를 만든 다음 특정한 인덱스의 원소에 접근하여 출력하는 예제를 확인해보자.

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)

# 인덱스 4, 즉 다섯 번째 원소에 접근
print(a[4])

# 빈 리스트 선언 방법 (1)
a = list()
print(a)

# 빈 리스트 선언 방법 (2)
a = []
print(a)

# 코딩 테스트 문제에서는 주로 크기가 N인 1차원 리스트를 초기화해야 하는데 다음 방식으로 초기화 하면 편리하다.
# 다음은 크기가 N이고, 모든 값이 0인 1차원 리스트를 초기화하는 소스코드다.

# 크기가 N이고, 모든 값이 0인 1차원 리스트 초기화
n = 10
a = [0] * n
print(a)
print('-----------------------------------------------------------------------------------------------------------------------')

# 리스트의 인덱싱과 슬라이싱
# 인덱스값을 입력하여 리스트의 특정한 원소에 접근하는 것을 인덱싱(Indexing)이라고 한다.
# 파이썬의 인덱스값은 양의 정수와 음의 정수를 모두 사용할 수 있으며, 음의 정수를 넣으면 원소를 거꾸로 탐색하게 된다.

# 예를 들어 인덱스 -1을 넣으면 가장 마지막 원소가 출력된다.
# 이런 성질을 이용해 인덱싱을 하여 특정 원소에 접근한 뒤에, 그 값을 간단하게 바꿀 수 있다.

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 뒤에서 첫 번째 원소 출력
print(a[-1])

# 뒤에서 세 번째 원소 출력
print(a[-3])

# 네 번째 원소 값 변경
a[3] = 7
print(a)

# 또한 리스트에서 연속적인 위치를 갖는 원소들을 가져와야 할 때는 슬라이싱(Slicing)을 이용할 수 있다.
# 이때는 대괄호 안에 콜론(:)을 넣어서 시작 인덱스와 (끝 인덱스 -1)을 설정할 수 있다.
# 예를 들어 a라는 리스트의 두 번째 원소부터 네 번쨰 원소까지의 모든 데이터를 갖는 리스트를 가져오고 싶다면 a[1:4}라고 넣는다.
# 앞서 말했듯이 리스트의 인덱스는 0부터 출발하기 때문에 두 번째 원소의 인덱스는 1이 된다.
# 그리고 끝 인덱스의 경우 1을 뺀 값의 인덱스까지 처리된다.
# 그래서 a[1:4]라고 작성하면 된다.

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 두 번쨰 원소부터 네 번째 원소까지
print(a[1:4])
print('-----------------------------------------------------------------------------------------------------------------------')

# 리스트 컴프리헨션
# 리스트 컴프리헨션은 리스트를 초기화하는 방법 중 하나이다.
# 리스트 컴프리헨션을 이용하면 대괄호([])안에 조건문과 반복문을 넣는 방식으로 리스트를 초기화할 수 있다.
# 간단히 0부터 19까지의 수 중에서 홀수만 포함하는 리스트를 만들고자 할 때는 다음과 같이 리스트를 초기화할 수 있다.
# 이 경우 한 줄의 소스코드로 리스트를 초기화할 수 있어 매우 간편하다.

# 0부터 19까지의 수 중에서 홀수만 포함되는 리스트
array = [i for i in range(20) if i % 2 == 1]
print(array)

# 참고로 위 소스코드를 일반적인 소스코드로  작성하면 아래와 같다.
array = []
for i in range(20):
    if i % 2 == 1:
        array.append(i)

print(array)

# 비교하면 어떠한가?
# 리스트 컴프리헨션을 이용했을 때의 소스코드가 훨씬 짧고 간결한 것을 알 수 있다.

# 또 다른 예시로 1부터 9까지 수의 제곱 값을 포함하는 리스트를 만들고자 할 때는 다음과 같이 리스트를 초기화할 수 있다.

# 1부터 9까지의 수의 제곱 값을 포함하는 리스트
array = [i * i for i in range(1,10)]
print(array)

# 이러한 리스트 컴프리헨션은 코딩 테스트에서 2차원 리스트를 초기화할 때 매우 효과적으로 사용될 수 있다.
# 예를 들어 N * M 크기의 2차원 리스트를 초기화할 때는 다음과 같이 사용한다.

# N * M 크기의 2차원 리스트 초기화
n = 3
m = 4
array = [[0] * m for _ in range(n)]
print(array)

# ※ 언더바(_)는 어떤 역할일까?
# 파이썬 자료구조/알고리즘에서는 반복을 수행하되 반복을 위한 변수의 값을 무시하고자 할 때 언더바(_)를 자주 사용한다.
# 예를 들어 1부터 9까지의 자연수를 더할 때는 (예시1)처럼 작성하지만, 단순히 "Hello World"를 5번 출력할 때는 (예시2)처럼 언더바(_)를 이용하여 무시할 수 있다.

# (예시1)
summary = 0
for i in range(1,10):
    summary += i
print(summary)

# (예시2)
for _ in range(5):
    print("Hello World")

# 참고로 특정 크기의 2차원 리스트를 초기화할 떄는 반드시 리스트 컴프리헨션을 이용해야 한다.
# 만약에 다음과 같이 N * M 크기의 2차원 리스트를 초기화한다면, 의도하지 않은 결과가 나올 수 있다.
# N * M 크기의 2차원 리스트 초기화 (잘못된 방법)
n = 3
m = 4
array = [[0] * m] * n
print(array)

array[1][1] = 5
print(array)
# 실행 결과를 확인해보면 array[1][1] 의 값을 5로 바꾸었을 뿐인데,
# 3개의 리스트에서 인덱스 1에 해당하는 원소들의 값이 모두 5로 바뀐 것을 확인할 수 있다.
# 이는 내부적으로 포함된 3개의 리스트가 모두 동일한 객체에 대한 3개의 레퍼런스로 인식되기 때문이다.
# 따라서 특정한 크기를 가지는 2차원 리스트를 초기화할 때에는 리스트 컴프리헨션을 이용해야 한다는 점을 기억하자.
print('-----------------------------------------------------------------------------------------------------------------------')

# 리스트 관련 기타 메서드
# 리스트와 관련한 기타 메서드를 사용하면 리스트 자료형을 효과적으로 이용할 수 있다.
# 주요 메서드는 다음과 같다.

# 메서드명      사용법                                     설명                                                                      시간 복잡도
# append()    변수명.aapend()                            리스트에 원소를 하나 삽입할 때 사용한다.                                        O(1)
# sort()      변수명.sort()                              기본 정렬 기능으로 오름차순으로 정렬한다.                                        O(NlogN)
# sort()      변수명.sort(reverse = True)                내림차순으로 정렬한다.                                                        O(NlogN)
# reverse()   변수명.reverse()                           리스트의 원소의 순서를 모두 뒤집어 놓는다.                                       O(N)
# insert()    변수명.insert(삽입할 위치 인덱스, 삽입할 값)    특정한 인덱스 위치에 원소를 삽입할 때 사용한다.                                   O(N)
# count()     변수명.count(특정 값)                       리스트에서 특정한 값을 가지는 데이터의 개수를 셀 때 사용한다.                        O(N)
# remove()    변수명.remove(특정 값)                      특정한 값을 갖는 원소를 제거하는데, 값을 가진 원소가 여러 개면 하나만 제거한다.        O(N)

a = [1, 4, 3]
print("기본 리스트: ", a)

# 리스트에 원소 삽입
a.append(2)
print("삽입:", a)

# 오름차순 정렬
a.sort()
print("오름차순 정렬: ", a)

# 내림차순 정렬
a.sort(reverse=True)
print("내림차순 정렬", a)

# 리스트 원소 뒤집기
a.reverse()
print("원소 뒤집기:", a)

# 특정 인덱스에 데이터 추가
a.insert(2, 3)
print("인덱스 2에 3 추가: ",a)

# 특정 값인 데이터 개수 세기
print("값이 3인 데이터 개수: ", a.count(3))

# 특정 값 데이터 삭제
a.remove(1)
print("값이 1인 데이터 삭제: ", a)

# 이 중에서 insert() 함수와 append(), remove()를 특히 더 눈여겨 두자.
# 코딩 테스트에서 insert() 함수를 사용할 때 원소의 개수가 N개면, 시간 복잡도는 O(N)이다.
# 파이썬의 리스트 자료형의 append() 함수는 O(1)에 수행되는 데에 반해 insert() 함수는 동작이 느리다.
# 중간에 원소를 삽입한 뒤에, 리스트의 원소 위치를 조정해줘야 하기 때문이다.
# 따라서 insert() 함수를 남발하면 '시간 초과'로 테스트를 통과하지 못할 수도 있다.
# remove()의 시간 복잡도는 insert() 함수와 마찬가지로 O(N)이라는 점을 유의하자.
# insert() 함수와 마찬가지로 리스트에서 중간에 있는 원소를 삭제한 뒤에, 리스트의 원소 위치를 조정해주어야 하기 때문에 O(N)이 소요된다.
# 그러면 특정한 값의 원소를 모두 제거하려면 어떻게 해야 할까?
# 다른 프로그래밍 언어에서는 remove_all()과 같은 함수로 간단하게 특정한 값을 가지는 모든 원소를 제거할 수 있다.
# 하지만 파이썬의 경우 그러한 함수를 기본적으로 제공해주지 않으므로 다음과 같은 방법을 이용하면 좋다.
# 다음 코드에서 ①부분은 a에 포함된 원소를 하나씩 확인하며 그 원소가 remove_set에 포함되어 있지 않았을 때만 리스트 변수인 result에 넣겠다는 의미이다.

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

# remove_set에 포함되지 않은 값만을 저장
result = [i for i in a if i not in remove_set]  # ①
print(result)
print('-----------------------------------------------------------------------------------------------------------------------')

# 문자열 자료형
# 문자열 초기화
# 문자열 변수를 초기화할 때는 큰따옴표 (")나 작은따옴표(')를 이용한다.
# 다만, 우리가 소스코드를 작성할 떄는 문자열 안에 큰따옴표나 작은따옴표가 포함되어야 하는 경우가 있다.
# 기본적으로 문자열을 큰따옴표로 구성하는 경우, 내부적으로 작은따옴표를 포함할 수 있다.
# 반대로 문자열을 작은따옴표로 구성하는 경우, 내부적으로 큰따옴표를 이용할 수 있다.
# 혹은 백슬래시(\)를 사용하면, 큰따옴표나 작은따옴표를 문자열에 원하는 만큼 포함시킬 수 있다.

data = 'Hello World'
print(data)

data = "Don't you know \"Python\"?"
print(data)

# 문자열 연산
# 파이썬은 문자열에 대한 연산도 지원하는데 문자열을 처리할 때 유용하게 사용할 수 있다.
# 예를 들어 문자열 변수에 덧셈(+)을 이용하면 단순히 문자열이 더해져서 연결된다.

a = "Hello"
b = "World"

print(a+" "+b)

# 문자열 변수를 양의 정수와 곱하는 경우, 문자열이 그 값만큼 여러 번 더해진다.
a = "String"

print(a * 3)
# 파이썬의 문자열은 내부적으로 리스트와 같이 처리된다.
# 문자열은 여러 개의 문자가 합쳐진 리스트라고 볼 수 있다.
# 따라서 문자열 데이터에 대해서도 마찬가지로 인덱싱과 슬라이싱을 이용할 수 있다.
a = "ABCDEF"

print(a[2 : 4])
print('-----------------------------------------------------------------------------------------------------------------------')

# 튜플 자료형
# 파이썬의 튜플 자료형은 리스트와 거의 비슷한데 다음과 같은 차이가 있다.
# ● 튜플은 한 번 선언된 값을 변경할 수 없다.
# ● 리스트는 대괄호([])를 이용하지만, 튜플은 소괄호(())를 이용한다.

# 예를 들어 하나의 튜플 데이터를 선언한 다음, 값을 출력하고 튜플의 특정한 값을 변경해보자.
a = (1, 2, 3, 4)
print(a)

# a[2] = 7

# 튜플의 값 (1, 2, 3, 4)는 그대로 출력되는 것을 확인할 수 있다.
# 하지만 튜플의 특정한 값을 변경하려고 할 때는 오류 메시지가 출력된다.
# 오류의 내용에는 원소의 대입(Item Assigment)이 불가능 하다는 메시지가 출력된다.
# 말 그대로 대입 연산자(=)를 사용하여 값을 변경할 수 없다는 의미이다.
# 튜플 자료형은 그래프 알고리즘을 구현할 떄 자주 사용된다.
# 예를 들어 다익스트라 최단 경로 알고리즘처럼 최단 경로를 찾아주는 알고리즘의 내부에는 우선순위 큐를 이용하는데
# 해당 알고리즘에서 우선순위 큐에 한번 들어간 값은 변경되지 않는다.
# 그래서 그 우선순위 큐에 들어가는 데이터를 튜플로 구성하여 소스코드를 작성한다.
# 이렇게 알고리즘을 구현하는 과정에서 일부러 튜플을 이용하게 되면 혹여나 자신이 알고리즘을 잘못 작성함으로써 변경하면 안 되는 값이 변경되고 있지는 않은지 체크할 수 있다.
# 또한 튜플은 리스트에 비해 상대적으로 공간 효율적이고, 일반적으로 각 원소의 성질이 서로 다를 때 주로 사용한다.
# 흔히 다익스트라 최단 경로 알고리즘에서는 '비용'과 '노드번호'라는 서로 다른 성질의 데이터를 (비용, 노드 번호)의 형태로 함께 튜플로 묶어서 관리하는 것이 관례이다.
print('-----------------------------------------------------------------------------------------------------------------------')

# 사전 자료형
# 사전 자료형 소개
# 사전 자료형은 키(key)와 값(value)의 쌍을 데이터로 가지는 자료형이다.
# 앞서 다루었던 리스트나 뉴플은 값을 순차적으로 저장한다는 특징이 있다.
# 예를 들어 리스트의 값아 [1, 2, 3]이라고 한다면, 첫 번재 원소는 a[0]으로 1이라는 값을 가진다.
# 하지만 사전 자료형은 키-값 쌍을 데이터로 가진다는 점에서, 우리가 원하는 변경 불가능한 데이터를 키로 사용할 수 있다.
# 파이썬의 사전 자료형을 이용한 매우 효과적인 사례가 있다.
# 사전 자료형이 사용되는 대표적인 예시는 사전(Dictionary)이다.
# 예를 들어 다음과 같이 키-값 쌍으로 구성되는 데이터를 담아야 한다면 어떻게 할 수 있을까?

# 키(Key)            값(Value)
#   사과                 Apple
#   바나나               Banana
#   코코넛              Coconut

# 키로 한글 단어를 넣고, 값으로 영어 단어를 넣어 '사과'의 영어 단어를 알고 싶다면 '사과'라는 키 값을 가지는 데이터에 바로 접근하면 된다.
# 파이썬의 사전 자료형은 내부적으로 '해시 테이블(Hash Table)'을 이용하므로 기본적으로 데이터의 검색 및 수정에 있어서 O(1)의 시간에 처리할 수 있다.
# 이 책에서는 해시 테이블에 대해서 깊게 다루지 않을 것이며, 위와 같이 키-값으로 구성된 데이터를 처리함에 있어서 리스트보다 훨씬 빠르게 동작한다는 점을 기억하자.

data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)

# 이러한 사전 자료형은 코딩 테스트에서도 자주 사용될 수 있다.
# 예를 들어 학생의 번호가 1부터 10,000,000까지로 구성되어 있는 상황에서 최대 10,000명의 학생을 선택했다고 가정해보자.
# 이후에 특정한 학생 번호가 주어졌을 때 해당 학생이 선택되었는지를 어떻게 빠르게 알 수 있을까?
# 만약 리스트를 이용한다면, 1부터 10,000,000까지의 각 번호가 '선택되었는지를 저장할 수 있는' 리스트를 만들어야 한다.
# 다시 말해 1,000만 개 데이터를 저장할 수 있는 리스트를 만들어야 하므로 많은 메모리 공간이 낭비된다.
# 이 중 999만 개 가량의 데이터는 쓰이지 않을 것이다.
# 하지만 사전 자료형을 이용하는 경우 1,000만 개의 데이터를 담을 필요가 없으며 10,000개의 데이터만 사전 자료구조에 들어가므로 훨씬 적은 메모리 공간을 사용할 수 있다.
# 실제로 사전을 이용했을 때 문제 풀이가 간결해지는 사례는 2부와 3부의 문제들에서 다루고 있다.
# 사전 자료형에 특정한 원소가 있는지 검사할 때는 '원소 in 사전'의 형태를 사용할 수 있다.
# 이는 리스트나 튜플에 대해서도 사용할 수 있는 문법이다.

data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

if '사과' in data:
    print("'사과'를 키로 가지는 데이터가 존재합니다.")

# ※ 파이썬에서 리스트, 문자열, 튜플 등 순차적인 정보를 담는 자료형을 iterable 자료형이라고 한다. in 문법은 이러한 iterable 자료형에 모두 사용이 가능하다.
print('-----------------------------------------------------------------------------------------------------------------------')

# 사전 자료형 관련 함수
# 또한 사전 자료형을 잘 이용하기 위해서는 이와 관련한 다양한 함수에 대해서 알아야 한다.
# 대표적으로는 키와 값을 별도로 뽑아내기 위한 함수가 있다.
# 키 데이터만 뽑아서 리스트로 이용할 때는 keys() 함수를 이용하며, 값 데이터만을 뽑아서 리스트로 이용할 때는 values() 함수를 이용한다.

data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

# 키 데이터만 담은 리스트
key_list = data.keys()
# 값 데이터만 담은 리스트
value_list = data.values()
print(key_list)
print(value_list)

# 각 키에 따른 값을 하나씩 출력
for key in key_list:
    print(data[key])
print('-----------------------------------------------------------------------------------------------------------------------')

# 집합 자료형
# 집합 자료형 소개
# 파이썬에서는 집합(set)을 처리하기 위한 집합 자료형을 제공하고 있다.
# 집합은 기본적으로 리스트 혹은 문자열을 이용해서 만들 수 있는데, 집합은 다음과 같은 특징이 있다.
# ● 중복을 허용하지 않는다.
# ● 순서가 없다.
# 리스트나 튜플은 순서가 있기 때문에 인덱싱을 통해 자료형의 값을 얻을 수 있었다.
# 반면에 사전 자료형과 집합 자료형은 순서가 없기 때문에 인덱싱으로 값을 얻을 수 없다는 특징이 있다.
# 이와 더불어 집합 자료형에서는 키가 존재하지 않고, 값 데이터만을 담게 된다.
# 특정 원소가 존재하는지를 검사하는 연산의 시간 복잡도는 사전 자료형과 마찬가지로 O(1)이다.

# 이전의 사전 자료형에 대해서 다룰 때 언급했던 '학생 번호가 주어졌을 때 해당 학생이 선택되었는지 여부를 출력하는 분제' 에서도 집합 자료형이 효과적으로 사용될 수 있다.
# 이와 같이 집합 자료형의 사용 방법을 알아두면 효과적으로 이용될 때가 있다.
# 특히 '특정한 데이터가 이미 등장한 적이 있는지 여부'를 체크할 때 매우 효과적이다.
# 집합 자료형을 초기화할 때는 set() 함수를 이용하거나, 중괄호({}) 안에 각 원소를 콤마(,)를 기준으로 구분해서 넣으면 된다.

# 집합 자료형 초기화 방법(1)
data = set([1, 1, 2, 3, 4, 4, 5])
print(data)

# 집합 자료형 초기화 방법(2)
data = {1, 1, 2, 3, 4, 4, 5}
print(data)

# 집합 자료형의 연산
# 기본적인 집합 연산으로는 합집합, 교집합, 차집합, 연산이 있다.
# 파이썬은 이러한 집합 자료형의 연산에 대해서 다루고 있다.
# 집합 자료형 데이터 사이에서 합집합을 계산할 때는 '|'를 이용한다.
# 또한 교집합은 "&", 차집합은 '-'을 이용한다.
a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])

print(a | b) # 합집합
print(a & b) # 교집합
print(a - b) # 차집합

# 집합 자료형 관련 함수
# 집합 자료형 또한 다른 자료형과 마찬가지로 다양한 함수가 존재한다.
# 하나의 집합 데이터에 값을 추가할 때는 add() 함수를 이용할 수 있다.
# update() 함수는 여러 개의 값을 한꺼번에 추가하고자 할 때 사용한다.
# 그리고 특정한 값을 제거할 때는 remove() 함수를 이용할 수 있다.
# 이 때 add(), remove() 함수는 모두 시간 복잡도가 O(1) 이다.

data = set([1, 2, 3])
print(data)

# 새로운 원소 추가
data.add(4)
print(data)

# 새로운 원소 여러 개 추가
data.update([5, 6])
print(data)

# 특정한 값을 갖는 원소 삭제
data.remove(3)
print(data)
print('-----------------------------------------------------------------------------------------------------------------------')

# 조건문
# 조건문은 프로그램을 작성할 때 프로그램의 흐름을 제어하는 문법이다.
# 조건문을 이용하면 조건에 따라서 프로그램의 로직을 설정할 수 있다.
# 예를 들어 어떤 변수의 값이 10 이상일 때에 한해서만, 변수의 값을 출력하는 예시를 생각해보자.
# 이러한 경우 다음과 같이 소스코드를 작성할 수 있다.

x = 15

if x >= 10:
    print(x)

# 파이썬에서 조건문을 작성할 때는 if ~ elif문을 이용한다.
# 그 형태는 다음과 같으며, 조건문을 사용할 때 elif 혹은 else 부분은 경우에 따라서 사용하지 않아도 된다.

# if 조건문 1:
#     조건문 1이 True 일 때 실행되는 코드
# elif 조건문 2:
#     조건문 1에 해당하지 않고, 조건문 2가 True일 때 실행되는 코드
# else:
#     위의 모든 조건문이 모두 True 값이 아닐 때 실행되는 코드

# 다음과 같이 성적 구간에 따른 학점 정보를 출력한다고 가정해보자.
# 이떄 if~elif~else문을 효과적으로 사용할 수 있다.

# ● 성적이 90점 이상일 때: A
# ● 성적이 90점 미만, 80점 이상일 때: B
# ● 성적이 80점 미만, 70점 이상일 때: C
# ● 성적이 70점 미만일 때: F

# 예시 코드는 다음과 같다.

score = 85

if score >= 90:
    print("학점: A")
elif score >= 80:
    print("학점: B")
elif score >= 70:
    print("학점: C")
else:
    print("학점: F")

# 조건문을 작성할 때는 코드의 블록(Block)을 들여쓰기로 설정한다는 점을 기억하자.
# 들여쓰기가 같은 부분은 함께 실행된다.
# 예를 들어 다음 코드에서 ①은 score 변수의 값이 70 미만이라면 함께 실행된다.
# 또한 마지막 줄에 해당하는 코드 ②는 조건문과 상관없이 무조건 실행되는 부분이다.

score = 85

if score >= 70:
    print('성적이 70점 이상입니다.')
    if score >= 90:
        print('우수한 성적입니다.')
else:
    print('성적이 70점 미만입니다.')
    print('조금 더 분발하세요.')

print('프로그램을 종료합니다.')

# 파이썬에서 들여쓰기는 스페이스 바(Space Bar)를 4번 입력하여 작성한다.
# 탭을 사용하는 쪽과 공백문자(space)를 여러 번 사용하는 쪽, 두 진영이 있으며 이에 대한 논쟁은 지금까지도 활발하다.
# 많은 파이썬 커뮤니티에서는 4개의 공백문자를 사용하는 것이 사실상의 표준이므로, 이를 따르는 것을 추천한다.
# 하지만 실제 코딩 테스트 처럼 촉박한 상황에서는 띄어쓰기를 4번 하는 것이 번거로울 수 있다.
# 그럴 때는 탭(Tap)을 이용해도 정답 판정을 받는 것에는 상관없지만, 이왕이면 띄어쓰기 4번으로 할 수 있도록 습관을 들이는 것을 추천한다.
print('-----------------------------------------------------------------------------------------------------------------------')

# 비교 연산자
# # 조건문에는 비교 연산자를 자주 사용한다.
# 비교 연산은 특정한 두 값을 비교할 때 이용할 수 있다.
# 예를 들어 X가 Y보다 큰지를 검사하고 싶다면, 'X>Y'라고 할 수 있다.
# X가 Y보다 클 때 'True'가 반환된다.

#   비교 연산자              설명
#      X == Y              X와 Y가 서로 같을 때 참(True)이다.
#      X != Y              X와 Y가 서로 다를 때 참(True)이다.
#       X > Y              X가 Y보다 클 때 참(True)이다.
#       X < Y              X가 Y보다 작을 때 참(True)이다.
#      X >= Y              X가 Y보다 크거나 같을 때 참(True)이다.
#      X <= Y              X가 Y보다 작거나 같을 때 참(True)이다.

# 논리 연산자
# 논리 연산자는 2개의 논리 값 사이의 연산을 수행할 때 사용하는데 파이썬에는 3가지 논리 연산자(Logical Operators)가 있다.
# 예를 들어 '학생 A가 남자이면서 성적이 90점 이상인지'를 판단하고 싶다면 '학생 A의 성별 == 남자 and 학생 A의 성적 >= 90' 이라고 조건문을 작성할 수 있다.
# 만약 학생 A의 성별이 남자이고 성적이 90점 이상이라면 이 수식은 'True and True'가 되므로 그 결과는 True가 된다.

# 논리 연산자            설명
# X and Y              X와 Y가 모두 참(True)일 때 참(True)이다.
# X or Y               X와 Y중에 하나만 참(True)이어도 참(True)이다.
# not X                X가 거짓(False)일 때 참(True)이다.

# 파이썬의 기타 연산자
# 파이썬에서는 추가적으로 'in 연산자'와 'not in 연산자'를 제공한다.
# 여러 개의 데이터를 담는 자료형으로 리스트, 튜플, 문자열, 사전과 같은 자료형이 존재한다.
# 이러한 자료형은 여러 개의 데이터를 담고 있기 때문에, 이때 자료형 안에 어떠한 값이 존재하는지 확인하는 연산이 필요할 때가 있다.

# in 연산자와 no in 연산자         설명
# X in 리스트                     리스트 안에 X가 들어가 있을 때 참(True)이다.
# X no in 문자열                  문자열 안에 X가 들어가 있지 않을 떄 참(True)이다.

# 또한 파이썬에서는 조건문의 값이 참(True)이라고 해도, 아무것도 처리하고 싶지 않을 때 pass 문을 이용할 수 있다.
# 예를 들어 코드를 작성하면서 디버깅하는 과정에서 일단 조건문의 형태만 만들어 놓고 조건문을 처리하는 부분은 비워놓고 싶을 때가 있다.
# 그럴 때는 다음과 같이 작성할 수 있다.

score = 85

if score >= 80:
    pass    # 나중에 작성할 소스코드
else:
    print('성적이 80점 미만입니다.')

print('프로그램을 종료합니다.')

# 그리고 조건문에서 실행될 소스코드가 한 줄인 경우, 굳이 줄 바꿈을 하지 않고도 간략하게 표현할 수 있다. 예시는 다음과 같다.

score = 85

if score >= 80: result = "Success"
else: result = "Fail"

print(result)
#  더 나아가서, 조건부 표현식(Conditional Expression)을 이용하면 if~else문을 한 줄에 작성해 사용할 수 있다.

score = 85
result = "Success" if score >= 80 else "Fail"
print(result)
# 특히 조건부 표현식은 리스트에 있는 원소의 값을 변경해서, 또 다른 리스트를 만들고자 할 때 매우 간결하게 사용할 수 있다.
# 예를 들어 리스트에서 특정한 원소의 값만을 없앤다고 해보자.
# 원래 일반적인 형태의 조건문을 이용하면 다음과 같이 작성해야 한다.

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

result = []
for i in a:
    if i not in remove_set:
        result.append(i)

print(result)

# 이 코드는 다음과 같이 간단하게 작성할 수 있다.
# 다음 코드는 앞서 리스트 자료형을 설명할 때 다뤘던 코드이다. 실행 결과는 동일하다.

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

result = [i for i in a if i not in remove_set]

print(result)

# 파이썬 조건문 내에서의 부등식
# 다른언어와 달리 파이썬은 조건문 안에서 수학의 부등식을 그대로 사용할 수 있다.
# 예를 들어 "x > 0 and x < 20" 과 "0 < x < 20"은 같은 결과를 반환한다.
# 다만, 파이썬이 아닌 대부분의 프로그래밍 언어에서는 단순히 "0 < x < 20"이라고 하면, 의도하지 않은 결과가 반환될 수 있다.
# 다시 말해 파이썬에서는 다음의 두 조건문이 동일하다.

# "x > 0 and x < 20"
# "0 < x < 20"
print('-----------------------------------------------------------------------------------------------------------------------')

# 반복문
# 반복문은 특정한 소스코드를 반복적으로 실행하고자 할 때 사용할 수 있다.
# 파이썬에서는 while문과 for문이 있는데 어떤 것을 사용해도 상관없다.
# 하지만 코딩 테스트에서의 실제 사용 예시를 확인해보면, 대부분의 경우에 for문이 더 소스코드가 짧은 경우가 많다.
# 먼저 while문에 대해 알아보자.

# while문
# while문은 조건문이 참일 때에 한해서, 반복적으로 코드가 수행된다.
# 예를 들어 다음은 '1부터 9까지 각 정수의 합을 계산하는 코드'이다.
# 아래 코드에서 ①은 i가 9보다 작거나 같을 때 ②블록(반복문 내부의 코드)을 반복해서 실행하라는 의미이다.
# 이 말은 i가 9보다 커지기 전까지는 ②가 계속 반복된다는 의미이다.
# 조건문 설정에 따라 해당 블록을 영원히 반복할 수도 있는데, 이를 무한 루프(Infinite Loop)라고 한다.
# 물론 코딩 테스트에서 무한 루프를 구현할 일은 거의 없으니 실수로 무한 루프가 발생하지 않도록 주의하도록 하자.

i = 1
result = 0

# i가 9보다 작거나 같을 때 아래 코드를 반복적으로 실행
while i <= 9:
    result += i
    i += 1

print(result)

# 그렇다면 1부터 9까지의 수 중에서 홀수만 더하고자 할 때는 어떻게 할 수 있을까?
# 반복문 안에서 i가 홀수일 때만 result 변수에 값을 더하면 된다.

i = 1
result = 0

# i가 9보다 작거나 같을 때 아래 코드를 반복적으로 실행
while i <= 9:
    if i % 2 == 1:
        result += i
    i += 1
print(result)
print('-----------------------------------------------------------------------------------------------------------------------')

# for문
# 반복문으로 for문을 이용할 수도 있다.
# 리스트를 사용하는 대표적인 for문의 구조는 다음과 같은데, in 뒤에 오는 데이터에 포함되어 있는 모든 원소를 첫 번째 인덱스부터 차례대로 하나씩 방문한다.
# in 뒤에 오는 데이터로는 리스트, 튜플, 문자열 등이 사용될 수 있다.

# for 변수 in 리스트:
#     실행할 소스코드

# 다음은 앞서 while문으로 구현했던, 1부터 9까지의 정수의 합을 구하는 예제를 동일하게 for문으로 작성한 코드이다.
# for문에서 수를 차례대로 나열할 때는 range()를 주로 쓰는데 range(시작 값, 끝 값 +1)형태로 쓰인다.
# 예를 들어 1부터 9까지의 모든 수를 담고자 한다면 range(1, 10)이라고 작성한다.

result = 0

# i는 1부터 9까지의 모든 값을 순회
for i in range(1, 10):
    result += i
print(result)

# 또한 range()의 값으로 하나의 값만을 넣으면, 자동으로 시작 값은 0이 된다.
# 주로 리스트나 튜플 데이터의 모든 원소를 첫 번째 인덱스부터 방문해야 할 때 이 방법을 사용한다.
# 리스트의 인덱스는 0부터 출발하기 때문이다.
# 다음 코드를 보자.
# 학생의 번호를 1번부터 매긴다고 했을 때, 다음과 같이 학생마다 합격 여부를 출력할 수 있다.

scores = [90, 85, 77, 65, 97]

for i in range(5):
    if scores[i] >= 80:
        print(i + 1, "번 학생은 합격입니다.")

# 반복문 안에서 continue를 만나면 프로그램의 흐름은 반복문의 처음으로 돌아간다.
# 위의 예제에서 2번 학생과 4번 학생은 블랙리스트에 올라가 있어서 점수가 높아도 합격하지 못한다고 가정해보자.
# 이럴 때는 다음의 소스코드와 같이 블랙리스트에 해당 번호가 포함된 경우, 해당 학생은 무시하고 다시 다음 번호부터 처리하도록 돌아가게 할 수 있다.

scores = [90, 85, 77, 65, 97]
cheating_list = {2, 4}

for i in range(5):
    if i + 1 in cheating_list:
        continue
    if scores[i] >= 80:
        print(i+1, "번 학생은 합격입니다.")

# 더불어 반복문은 얼마든지 중접해서 사용할 수 있다.
# 예를 들어 2중 반복문이 사용되어야 하는 대표적인 예시는 구구단 예시이다.
# 실제로 중첩된 반복문은 코딩 테스트에서도 '플로이드 워셜 알고리즘', '다이나믹 프로그래밍'등의 알고리즘 문제에서 매우 많이 사용된다.
# 구구단 2단부터 9단까지의 모든 결과를 출력하는 소스코드 예시를 확인해보자.

for i in range(2, 10):
    for j in range(1, 10):
        print(i, "*", j, "=", i*j)
    print()
print('-----------------------------------------------------------------------------------------------------------------------')

# 함수
# 함수는 프로그래밍에 있어서 굉장히 중요하다. 프로그래밍을 하다 보면, 똑같은 코드가 반복적으로 사용되어야 할 때가 많다.
# 함수를 사용하지 않으면 소스코드를 매번 일일이 작성해야 하므로, 소스코드가 길어지며 이로인해 프로그램의 크기가 비효율적으로 커진다.
# 코딩 테스트에서 테스트 케이스(Test Case)가 입력된 뒤에 테스트 케이스만큼 특정한 알고리즘을 수행한 결과를 반복적으로 출력하도록 요구하는 문제가 출제되는 경우가 많다.
# 이럴 때는 문제를 푸는 코드를 함수화하면 매우 효과적으로 풀 수 있다.
# 이처럼 동일한 알고리즘을 반복적으로 수행해야 할 때 함수는 중요하게 사용된다.
# 파이썬에서 함수의 구조는 다음과 같다.
# 함수를 작성할 때는 함수 내부에서 사용되는 변수의 값을 전달 받기 위해 매개변수를 정의할 수 있다.
# 이후에 함수에서 어떠한 값을 반환하고자 할 때는 return을 이용한다.
# 이때 함수에서 매개변수나 return문은 존재하지 않을 수도 있다.

# def 함수명(매개변수):
#     실행할 소스코드
#     retrun 반환 값

# 대표적인 함수의 예시인 더하기 기능을 제공하는 함수를 작성해보자.
def add(a, b):
    return a + b

print(add(3, 7))

# 앞서 언급했듯이, 동일한 함수를 return문 없이 작성할 수도 있다.
# 다음 예시와 같이 함수 안에서 결과까지 출력하도록 하는 경우 return문 없이 함수를 작성한다.
def add(a, b):
    print('함수의 결과:', a + b)
add(3, 7)

# 또한 함수를 호출하는 과정에서 다음과 같이 인자(Argument)를 넘겨줄 때, 파라미터의 변수를 직접 지정해서 값을 넣을 수 있다.
# 예를 들어 함수 처리 과정에서 매개변수로 a, b가 사용될 때, 함수를 호출하는 라인에서 인자 a와 b를 지칭해서 각각 값을 넣을 수 있다.
# 이 경우 매개변수의 순서가 달라도 상관없다는 점이 특징이다.
def add(a, b):
    print('함수의 결과:', a + b)

add(b = 3, a = 7)

# 그리고 함수 안에서 함수 밖의 변수 데이터를 변경해야 하는 경우가 있다.
# 이때는 함수에서 global키워드를 이용하면 된다.
# global 키워드로 변수를 지정하면, 해당 함수에서는 지역 변수를 만들지 않고, 함수 바깥에 선언된 변수를 바로 참조하게 된다.
# 아래 예시에서는 a라는 변수를 함수안에서도 동일하게 접근하여 값을 변경하고 있다.
# 이를 위해 global 키워드가 사용된 것을 확인할 수 있다.
a = 0

def func():
    global a
    a += 1

for i in range(10):
    func()

print(a)

# 끝으로 파이썬에서는 람다 표현식(Lambda Express)을 사용할 수 있다.
# 람다 표현식을 이용하면 함수를 매우 간단하게 작성하여 적용할 수 있다.
# 특정한 기능을 수행하는 함수를 한 줄에 작성할 수 있다는 점이 특징이다.
# 예를 들어 앞서 정의했던 add() 함수와 같은 간단한 함수를 정의해야 할 때는 다음처럼 람다 표현식을 효괒거으로 사용할 수 있다.
# 이러한 람다식은 파이썬의 정렬 라이브러리를 사용할 때, 정렬 기준(Key)을 설정할 때에도 자주 사용된다.
# 자세한 내용은 '정렬'파트를 확인해 보도록 하자.

def add(a, b):
    return a + b

# 일반적인 add() 메서드 사용
print(add(3, 7))

# 람다 표현식으로 구현한 add() 메서드
print((lambda a, b: a + b)(3, 7))
print('-----------------------------------------------------------------------------------------------------------------------')

# 입출력
# 알고리즘 문제 풀이의 첫 번째 단계는 데이터를 입력받는 것이다.
# 알고리즘 문제의 경우 적절한 입력이 주어졌을 때, 그 입력을 받아서 적절한 알고리즘을 수행한 뒤의 결과를 출력하는 것을 요구하기 때문이다.
# 예를 들어 학생의 성적 데이터가 주어지고, 이를 내림차순으로 정렬한 결과를 출력하라는 문제를 만났다고 가정해보자.
# 일반적으로 입력 과정에서는 먼저 데이터의 개수가 첫 번째 줄에 주어지고, 처리할 데이터는 그다음 줄에 주어지는 경우가 많다.
# 즉 첫 번째 줄에 학생의 수가 주어지고, 두 번째 줄에 학생의 정보가 주어지며, 정보는 공백으로 구분한다.
# 대부분 문제에서의 입력 예시와 출력 예시는 다음과 같은 형태를 보일 것이다.

# 입력 예시
# 5
# 65 90 75 34 99

# 출력 예시
# 99 90 75 65 34

# 파이썬에서 데이터를 입력받을 때는 input()을 이용한다.
# input()의 경우 한 줄의 문자열을 입력 받도록 해준다.
# 만약 파이썬에서 입력받은 데이터를 정수형 데이터로 처리하기 위해서는 문자열을 정수로 바꾸는 int() 함수를 사용해야 한다.
# 그리고 여러 개의 데이터를 입력받을 때는 데이터가 공백으로 구분되는 경우가 많다.
# 그래서 입력받은 문자열을 띄어쓰기로 구분하여 각각 정수형 자료형의 데이터로 저장하는 코드의 사용 빈도가 매우 높다.
# 이떄는 list(map(int, input().split()))을 이용하면 된다.
# list(map(int, input().split()))의 동작 과정을 알아보자.
# 가장 먼저 input()으로 입력받은 문자열을 split()을 이용해 공백으로 나눈 리스트로 바꾼 뒤에, map을 이용하여 해당 리스트의 모든 원소에 int()함수를 적용한다.
# 최종적으로 그 결과를 list()로 다시 바꿈으로써 입력받은 문자열을 띄어쓰기로 구분하여 각각 숫자 자료형으로 저장하게 되는 것이다.
# 이 코드는 정말 많이 사용되므로, 반드시 외우고 있어야 한다.
# 많은 문제는 공백, 혹은 줄 바꿈을 기준으로 데이터를 구분한다.
# C/C++ 에서 입력을 받는 함수인 scanf()는 이 둘을 모두 동일하게 처리한다.
# 하지만 파이썬에서는 구분자가 줄 바꿈인지 공백인지에 따라서 다른 처리를 요구한다.
# 줄 바꿈이라면 int(input())을 여러 번 사용하면 되는데, 공백이라면 이렇게 사용해야 하므로 구분하서 알아두자.
# 결과적으로 코딩 테스트에서 입력을 위해 사용되는 전형적인 소스코드는 다음과 같다.

# 입력을 위한 전형적인 소스코드

# 데이터의 개수 입력
n = int(input('데이터의 개수 입력:'))
# 각 데이터를 공백으로 구분하여 입력
data = list(map(int, input("각 데이터를 공백으로 구분하여 입력:").split()))

data.sort(reverse=True) #내림차순
print(data)

# 공백으로 구분된 데이터의 개수가 많지 않다면, 단순히 map(int, input().split())을 이용하는 것도 가능하다.
# 예를 들어 문제에서 첫째 줄에 n, m, k가 공백으로 구분되어 입력된다는 내용이 명시되어 있다고 가정하자.
# 이 경우에는 다음과 같이 사용할 수 있다.

# 공백을 기준으로 구분하여 적은 수의 데이터 입력

# n, m, k를 공백으로 구분하여 입력
n, m, k = map(int, input("공백으로 구분하여 입력:").split())

print(n, m, k)

# 또한 문제를 풀다보면, 입력을 최대한 빠르게 받아야 하는 경우가 있다.
# 흔히 정렬, 이진 탐색, 최단경로 문제의 경우 매우 많은 수의 데이터가 연속적으로 입력이 되곤 한다.
# 예를 들어 1,000만 개가 넘는 라인이 입력되는 경우, 입력을 받는 것만으로도 시간초과를 받을 수 있다.
# 그래서 사용하는 언어별로 입력을 더 빠르게 받는 방법을 알고 있어야 한다.
# C++에서는 cin을 이용해 입력을 받기보다, scanf()를 사용하는 것이 권장된다.
# 자바의 경우에도 문법은 다르지만 비슷한 양상을 보인다.
# 파이썬도 마찬가지다.
# 입력의 개수가 많은 경우에는 단순히 input()함수를 그대로 사용하지는 않는다.
# 파이썬의 기본 input()함수는 동작 속도가 느려서 시간 초과로 오답 판정을 받을 수 있기 때문이다.
# 이 경우 파이썬의 sys 라이브러리에 정의되어 있는 sys.stdin.readline() 함수를 이용한다.
# sys 라이브러리는 다음과 같은 방식으로 사용하며 input() 함수와 같이 한 줄씩 입력받기 위해 사용한다.

import sys
sys.stdin.readline().rstrip()

# sys 라이브러리를 사용할 때는 한 줄 입력을 받고 나서 rstrip() 함수를 꼭 호출해야 한다.
# readline()으로 입력하면 입력 후 엔터(Enter)가 줄 바꿈 기호로 입력되는데, 이 공백 문자를 제거하려면 rstrip() 함수를 사용해야 한다.
# 이 또한 짧은 코드이니 관행적으로 외워서 사용하자.

# readline() 사용 소스코드 예시
import sys
data = sys.stdin.readline().rstrip()
print(data)

# 이상으로 간단히 파이썬에서의 입력 방법에 대해 알아보았다.
# 이제 출력 방법에 대해서 알아보자.
# 출력을 할 때는 print()를 이용하여 출력을 진행할 수 있다.
# print()는 변수나 상수를 매개변수로 입력받아 이를 표준 출력으로 출력한다.
# print()는 각 변수를 콤마(,)로 구분하여 매개변수로 넣을 수 있는데, 이 경우 각 변수가 띄어쓰기로 구분되어 출력된다.

# 변수 출력 예시

# 출력할 변수들
a = 1
b = 1

print(a, b)

# 또한 파이썬의 print()는 기본적으로 출력 이후에 줄 바꿈을 수행한다.
# 따라서 print()를 사용할 때마다 줄이 변경된다고 볼 수 있다.

# 출력 줄 바꿈 예시
a = 1
b = 2
print(a)
print(b)

# 일부 문제의 경우 출력할 때 문자열과 수를 함께 출력해야 되는 경우가 있다.
# 이 경우 단순히 더하기 연산자(+)를 이용하여 문자열과 수를 더하면 오류가 발생한다.

# 출력 시 오류가 발생하는 소스코드 예시

# 출력할 변수들
# answer = 7
# print("정답은" + answer + "입니다.")

# 위 코드를 실행하면, 문자열 자료형 끼리만 더하기 연산이 가능하다는 오류 메시지를 확인할 수 있다.
# 이 경우에는 2가지 방법으로 해결할 수 있다.
# str() 함수를 이용하여 출력하고자 하는 변수 데이터를 문자열로 바꾸어 주거나, 혹은 각 자료형을 콤마(,)를 기준으로 구분하여 출력하면 된다.

# 변수를 문자열로 바꾸어 출력하는 소스코드 예시

# 출력할 변수들
answer = 7
print("정답은 " + str(answer) + "입니다.")

# 각 변수를 콤마(,)로 구분하여 출력하는 소스코드 예시

# 출력할 변수들
answer = 7
print("정답은", str(answer), "입니다.")

# 각 변수를 콤마로 구분하여 출력하는 경우, 변수의 값 사이에 의도치 않은 공백이 삽입될 수 있다는 점을 신경 써주도록 하자.
# 또한 Python3.6 이상의 버전부터 f-string 문법을 사용할 수 있다.
# f-string은 문자열 앞에 접두사 'f'를 붙임으로써 사용할 수 있는데, f-string을 이용하면 단순히 중괄호({})안에 변수를 넣음으로써,
# 자료형의 변환 없이도 바꾸지 않고도 간단히 문자열과 정수를 함께 넣을 수 있다.
answer = 7
print(f"정답은 {answer}입니다.")
print('-----------------------------------------------------------------------------------------------------------------------')

# 주요 라이브러리 문법과 유의점