# 하나씩 더할때, 두개씩 더할때, n개씩 더할때 금액들 세트에 추가
# 하나씩 탐색하며 제일 작은 숫자 찾기
# 1
from itertools import combinations

n = int(input())
arr = list(map(int, input().split()))
sets = set()

for i in range(1, n+1, 1):
    cases = list(combinations(arr, i))
    for s in cases:
        sets.add(sum(s))

for index, e in enumerate(sets):
    if index+1 != e:
        print(index+1)
        break