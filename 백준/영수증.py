X = int(input())
N = int(input())
sums =0
# 0부터 시작

for i in range(N):
    ## N = 5 -> i는 0,1,2,3,4
    a,b = map(int,input().split())   
    sums += a*b
if X == sums:
    print("Yes")
else :
    print("No")
    