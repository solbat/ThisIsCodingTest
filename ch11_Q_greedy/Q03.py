# ch11-Q03 문자열 뒤집기

s = input()

result = 0
count = 0

if len(s) <= 1:
    pass
else:
    for i in range(1, len(s)):
        if s[i-1] != s[i]:
            count += 1
    result = (count+1)//2

print(result)