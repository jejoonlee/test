dust = int(input())

if dust <= 30:
    if dust < 0:                            # 중첩 조건문
        print('음수 값입니다')               # 조건문 안에 조건문을 사용
    else:                               
        print('좋음')
elif dust <= 80:
    print('보통')
elif dust <= 150:
    print('나쁨')
else:
    if dust > 300:
        print('실외활동을 자제하세요.')
    print('매우나쁨')                       
# else가 없어서 300이 넘으면, '매우 나쁜'과 '실외활동을 자제하세요.' 두개가 다 출력이 된다