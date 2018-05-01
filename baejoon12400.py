rule = {
    'a':'y',
        'b':'h',
        'c':'e',
        'd':'s',
        'e':'o',
        'f':'c',
        'g':'v',
        'h':'x',
        'i':'d',
        'j':'u',
        'k':'i',
        'l':'g',
        'm':'l',
        'n':'b',
        'o':'k',
        'p':'r',
        'q':'z',
        'r':'t',
        's':'n',
        't':'w',
        'u':'j',
        'v':'p',
        'w':'f',
        'x':'m',
        'y':'a',
        'z':'q',
        ' ':' '}
n = eval(input())
strList = []
for i in range(n):
    line = input()
    strList.append(line)
for i in range(n):
    convertedStr = ""
    for c in strList[i]:
        convertedStr += rule[c]

    print("Case #{0}: {1}".format(i+1,convertedStr))
