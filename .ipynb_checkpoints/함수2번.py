def city():
    A='''
    1. 도시를 추가
    2. 추가 완료
    3. 종료
    '''
    x = []
    while True:
        print(A)
        a = input("값을 입력하세요:")
        if int(a) == 1 :
            b = input("도시를 영어로 입력하세요:")
            x.append(b[:3])
        elif int(a) == 2 or 3 :
            print(x)
            print("종료")
            break 
    

        
city()