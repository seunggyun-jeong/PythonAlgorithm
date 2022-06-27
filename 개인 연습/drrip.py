# 경북대학교 2021 Goricon 출제 문제
# driip
'''드립이는 "driip"으로 끝나는 문자열은 모두 귀엽다고 생각한다.
다음 문자열들은 드립이가 귀엽다고 생각하는 문자열들의 예시이다. "dogdriip", "catdriip", "driip"
다음 문자열들은 드립이가 귀엽다고 생각하지 않는 문자열들의 예시이다. "dogdrip", "driipcat", "driiiiip"
문자열이 주어지면, 드립이가 주어진 문자열을 귀엽다고 생각하는지 판단하는 프로그램을 작성하자.'''

inputString = input()
stringRange = len(inputString)

if inputString[stringRange-5:stringRange] == 'driip' :
    print("cute")
else :
    print("not cute")