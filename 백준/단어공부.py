a = input("입력:") .upper()  # 대문자로 변경
d = {}
result = 0

for s in a:
    if s not in d:
        d[s] = 1
    else:
        d[s] += 1

for i in d:
    result = max(d[i], result)

    print(d)
