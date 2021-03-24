# 우선 문자열을 입력받아서 그 문자열을 하나씩 쪼개서 리스트에 저장하는 방식을 채택한다.
a = input('Before reversing: ')
b = list(a)

count = len(b) # 리스트 b의 요소 개수 측정

print('')
print('After reversing: ',end='')
# 쪼갠 문자열을 리스트의 맨 끝부터 하나씩 출력하는 방식을 쓴다. 
def reversed(count):
    if count == 0:
        return

    print(b[count-1],end='')

    count -= 1
    reversed(count)

reversed(count)
