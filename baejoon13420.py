NofP = eval(input())
for i in range(NofP):
    line = input()
    stringList = line.split()
    number1 = eval(stringList[0])
    number2 = eval(stringList[2])
    number3 = eval(stringList[4])
    operator = stringList[1]
    if operator == "+":
        answer = number1 + number2
    elif operator == "-":
        answer = number1 - number2
    elif operator == "*":
        answer = number1 * number2
    elif operator == "/":
        answer = number1 // number2
    if answer == number3:
        print("correct")
    else:
        print("wrong answer")