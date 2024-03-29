# 에라토스테네스의 체 알고리즘을 이용한 소수 판별 함수

'''
에라토스테네스의 체 알고리즘 동작과정
1. 2부터 a까지의 모든 자연수를 나열한다.
2. 남은 수 중에서 아직 처리하지 않은 가장 작은 수 i를 찾는다.
3. 남은 수 중에서 i의 배수를 모두 제거한다.(i는 제거하지 않는다.)
4. 더이상 반복할 수 없을 떄까지 2번과 3번의 과정을 반복한다.
'''



# 에라토스테네스의 체 알고리즘(python)(1)
def find_prime_number(a):
    import math
    # 2부터 a까지의 모든 수에 대하여 소수 판별
    # 처음엔 모든 수가 소수(True)인 것으로 초기화(0과 1은 제외)
    array = [True for i in range(a + 1)]

    # 에라토스테네스의 체 알고리즘 수행
    # 2부터 n의 제곱근까지의 모든 수를 확인하여
    for i in range(2, int(math.sqrt(a)) + 1):
        if array[i] == True:  # i가 소수인 경우(남은 수인 경우)
            # i를 제외한 i의 모든 배수를 지우기
            j = 2
            while i * j <= a:
                array[i * j] = False
                j = j + 1
    # print(array)
    # 모든 소수 출력
    for i in range(2, a + 1):
        if array[i]:
            print(i, end=' ')

# a = 1000
# find_prime_number(a)




#--------------- 이건 에라토스테네스의 체 이용한 것은 아님(이 함수 사용시 시간초과 주의)----------------
# 소수 판별 함수(소수 갯수 반환)
def find_prime_number2(a):
    import math
    # case = int(input())
    num_list = list(map(int, input().split(' ')))
    natural_num = list(range(2, a))  # 자연수 범위를 정한다.(소수는 1이상인 정수이기때문에 1은 뺀상태)
    count = 0

    for i in range(2, math.ceil(math.sqrt(1000))):  # p²≥100인 p의 배수(p를 제외한)까지만 지우면 된다.
        for j in natural_num:
            if j / i == 1:  # 자기 자신으로 나뉘는것은 제외
                pass
            elif j % i == 0:  # 그 이외에 나뉘는 수가 존재하면
                natural_num.remove(j)  # 그 수는 정수 리스트에서 제거
    for k in num_list:
        if k in natural_num:  # num_list에 natural_num이랑 중복되는 수가 있다면 count +1
            print(k)
            count += 1

    print('총 {}개'.format(count))

find_prime_number2(1000) # 1000까지의 수 중에서 탐색
