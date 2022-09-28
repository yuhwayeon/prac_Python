
def average():
    x = []
    y = []
    while True:
        a = input("과목:")
        b = int(input("점수:"))
        c = input("추가하실 건가요? \n 예 or 아니오:")
        x.append(a)
        y.append(b)
        
        if c == "예":
            continue
        else:
            for i in range(len(x)):
                print(f"{x[i]}:{y[i]}")
        print("평균:",sum(y)/len(x))

        break
average()