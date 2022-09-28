a = int(input())
b = int(input())

def four(a,b):
    if a == 0 or b ==0: 
        pass
    elif a>0 and b>0:
        print("1")
    elif a<0 and b>0:
        print("2")
    elif a<0 and b<0:
        print("3")
    elif a>0 and b<0:
        print("4")

four(a,b)