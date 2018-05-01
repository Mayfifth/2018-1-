def isPrimeNumber(N):
    siege = [eval (i) for i in range(2, N//2+1)]
    while len(siege) > 0:
        s = siege[0]
        if N % s == 0:
            return False
        for i in siege:
            if i % s == 0:
                siege.remove(i)
    return True

def Numbers(length,intList):
    #intList 수열에서 length 부분수열이 소수부분수열인지 검사
    for i in range(len(intList)-length+1):
        result = []
        for j in range(i,i+length):
            result.append(intList[j])
        if isPrimeNumber(sum(result)):
            return result
    return []

TestCase = eval(input())

for i in range(TestCase):
    strList = input().split()
    intList = [eval(i) for i in strList]
    intList.pop(0)
    flag = True
    for j in range(2, len(intList)+1): #소수부분수열 의 길이 2부터 length
        result = Numbers(j, intList)
        if len(result) > 0:
            print("Shortest primed subsequence is length {0}: ".format(j),end="")
            for k in result:
                print("{0}".format(k),end=" ")
            print()
            flag = False
            break
    if flag:
        print("This sequence is anti-primed.")


