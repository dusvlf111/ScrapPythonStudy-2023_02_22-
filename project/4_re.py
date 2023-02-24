import re


p = re.compile('ca.e') 
# . : 하나의 문자를 의미 
#  ^ : 문자열의 시작
# $ : 문자열의 끝 
# print(m.group()) # 매치되지 않으면 에러가 발생

    
def print_match(m):
    if m:
        print(m.group())
    else:
        print('매칭되지 않았습니다')
    
m = p.match('good care')
print_match(m)
