numDic = {'ZERO':0, 'ONE':1, 'TWO':2, 'THREE':3, 'FOUR':4, 'FIVE':5, 'SIX':6, 'SEVEN':7, 'EIGHT':8, 'NINE':9}
stringDic = dict(zip(numDic.values(), numDic.keys()))

firstNumber = ''
secondNumber = ''
operator = ''
result = 0

inputExpression = input()

# 단어의 길이는 3~5
# 하나씩 검사
while(True) :
    for i in range(0, 9):
        if inputExpression[0:3] == stringDic[i]:
            firstNumber = f'{firstNumber}{numDic[stringDic[i]]}'
            break
        elif inputExpression[0:4] == stringDic[i]:
            firstNumber = f'{firstNumber}{numDic[stringDic[i]]}'
            break
        elif inputExpression[0:5] == stringDic[i]:
            firstNumber = f'{firstNumber}{numDic[stringDic[i]]}'
            break
        elif inputExpression[0] == ('+' or '-' or 'x' or '/' or '='):
            operator = inputExpression[0]
            break

    print(firstNumber)
    break