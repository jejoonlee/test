dust = int(input()) # int를 설정하여 정수로 만든다

if dust <= 30:
    print('좋음')
elif 30 < dust <= 80:
    print('보통')
elif 80 < dust <= 150:
    print('나쁨')
else:                   # else는 위의 모든 조건에 해당하지 않는 나머지
    print('매우나쁨')    # expression이 없어야 함/ 반드시 있을 필요는 없음

# else는 조건문에서 생략이 가능하다

# elif = else if = 복수 조건문을 사용할 때에 elif를 쓴다

# 굳이 위에 처럼, 작성을 안 해도 됨.
# 순차적으로 비교하는 것 
if dust <= 30:
    print('좋음')
elif dust <= 80:
    print('보통')
elif dust <= 150:
    print('나쁨')
else:
    print('매우나쁨')