# ch06-4 실전 문제 : 두 배열의 원소 교체

n, k = map(int, input().split())

a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))

a1.sort()
a2.sort(reverse=True)

for i in range(k):
    if a1[i] < a2[i]:
        a1[i], a2[i] = a2[i], a1[i]
    else:
        break

print(sum(a1))
