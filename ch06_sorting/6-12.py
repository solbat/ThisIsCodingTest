# 실전 문제 6-12 두 배열의 원소 교체

n, k = map(int, input().split())

A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

##

A_list.sort()
B_list.sort()

i = 0
j = n-1

for _ in range(k):
    if(A_list[i]<B_list[j]):
        A_list[i], B_list[j] = B_list[j], A_list[i]
        i += 1
        j -= 1
    else:
        break

##

# A_list.sort()
# B_list.sort(reverse=True)

# for i in range(k):
#     if A_list[i]<B_list[i]:
#         A_list[i], B_list[i] = B_list[i], A_list[i]
#     else:
#         break

print(sum(A_list))