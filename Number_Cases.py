num1=int(input("첫번째 정수 입력 : "))
num2=int(input("두번째 정수 입력 : "))

if num1 <= 10 and num2 <= 10:
    for i in range(1,num1+1):
        for j in range(1,num2+1):
            print(i,j)