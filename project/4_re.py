import re


p = re.compile('ca.e') 

# . : 하나의 문자를 의미    (ca.e)---ex) care, cafe, case
#  ^ : 문자열의 시작    (^de)---ex) desk, destination
# $ : 문자열의 끝   (se&) : case, base

# print(m.group()) # 매치되지 않으면 에러가 발생

    
def print_match(m):
    if m:
        print(m.group())
    else:
        print('매칭되지 않았습니다')
    
m = p.match('careless') # 주어진 문자열의 처음부터 일치하는지 확인
print_match(m)
