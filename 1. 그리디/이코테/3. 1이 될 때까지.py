# N, K = map(int, input().split())
# answer = 0
# while 1 < N:
#     if N % K == 0:
#         N /= K
#     else:
#         N -= 1
#     answer += 1
# print(answer)

N, K = map(int, input().split())
count = 0
while(N > 1):
    if N % K:
        N -= 1
    else:
        N /= K
    count = count + 1
print(count)