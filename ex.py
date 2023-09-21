import random 

a = random.randint(1,50)

while True:
    ans = int(input("숫자를 맞춰봐!(1~50) : "))
    if a > ans:
        print("업!")
        
    elif a < ans:
        print("다운!")
        
    else:
        print("정답!")
        break
