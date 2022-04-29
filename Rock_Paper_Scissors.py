import random

while True:
    print("1. 가위 2. 바위 3. 보")
    user = int(input())
    com = random.randint(1, 3)
    print("유저 : ",user)
    print("컴퓨터 : ",com)
    if user==com:
        print("다시 시작")
        continue
    elif user==1 and com==3:
        print("유저 승리")
        break
    elif user==2 and com==1:
        print("유저 승리")
        break
    elif user==3 and com==2:
        print("유저 승리")
        break
    else:
        print("컴퓨터 승리")
        break
