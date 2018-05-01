#몫과 나머지가 같은 숫자의 합
N = int(input())
sum = 0
#1부터 N*N - 1 사이 자연수 중에서 몫과 나머지가 같은 숫자를 생성
for i in range(1,N):
    sum += N*i + i
print(sum)

