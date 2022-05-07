from platform import java_ver
from re import I


def solution(s):

    num_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i, j in enumerate(num_list):
        s = str(i).join(s.split(j))
    return int(s)

print(solution("ninenineseven752eight"))


N, K = map(int, input().split())
lst = []
for i in range(1,N+1):
    if N%i == 0:
        lst.append(i)
if len(lst) < K:
    print(0)
else:
    print(lst[K-1])




    