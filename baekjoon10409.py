def main():
    strList = input().split()
    n = eval(strList[0])
    T = eval(strList[1])
    strList = input().split()
    intList = [eval(i) for i in strList]
    sum = 0
    for i in range(n):
        sum += intList[i]
        if sum > T:
            return i

print(main())