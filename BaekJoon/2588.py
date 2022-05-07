# 방법 1 : B의 각 자리의 수를 추출해 A와 곱함
A = int(input())
B = int(input())

print(A * int(B%10))
print(A * int(B%100/10))
print(A * int(B/100))
print(A * B)

# 방법 2 : 문자열 인덱싱 이용해 B는 문자열로 받아서 처리
a = int(input())
b = input()

a1 = a * int(b[2])
a2 = a * int(b[1])
a3 = a * int(b[0])
a4 = a * int(b)

print (a1, a2, a3, a4, sep='\n')