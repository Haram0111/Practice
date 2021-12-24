# # #별 찍기
# N = int(input())

# for i in range(1,N+1):
#     print(' '*(i-1), end = '') 
#     for j in range(1,N+1):
#         if j >= i:            
#             print('*', end='')
            
#     print()  

# #직각삼각형

# for i in range(1,50):
#     a,b,c = map(int, input().split())
#     if a*a + b*b == c*c:
#         if a==0 and b==0 and c==0:
#             break
#         print("right")
#     else:
#         print("wrong")

# # #피보나치 수5 -공부해낼것-
# def pib(n):
#     global dp
#     dp[0] = 0 
#     dp[1] = 1
#     dp[2] = 1

#     for i in range(n+1)[3:]:
#         dp[i] = dp[i-1] + dp[i-2]
    
#     return dp[n]

# n = int(input('n번째 피보나치 수 : '))

# if n <= 0:
#     print("wrong input")

# else:
#     dp = [0]*(n+2)

#     print ( n, '번째 피보나치 수 결과 : ', pib(n) )


# #평균은 넘겠지
# n = int(input("개수 입력: "))
# numbers = []
# up_average = []

# for i in range(0, n):
#     number = int(input(f"{i+1}번째 숫자 입력: "))
    
#     if number == 0:
#         print("0이 입력되어 종료됩니다.")
#         exit()
    
#     numbers.append(number)

# result = sum(numbers)
# average =  result / n

# for k in range(0,n):
#     if numbers[k] > average:
#         up_average.append(numbers[k])
    
# countlist = len(up_average)

# topstudentprobability =  (countlist / n) * 100
# print("%.3f" %(topstudentprobability))

#1로 만들기
# a = int(input())
# count = 0
# while True:
#     if a == 10:
#         count = count + 4
#         break
#     elif a % 3 == 0:
#         a = a/3
#     elif a % 2 == 0:
#         a = a/2
#     elif a == 1:
#         count = count + 1
#         break
#     else:
#         a = a-1
#     count = count + 1
# print(count-1)

#안녕
# a = int(input())
# heart = 100
# smile = 0 
# for i in range(0,a):
#     damage = int(input(f"{i+1}번째 데미지 입력: "))
#     heart = heart - damage
#     happy = int(input(f"{i+1}번째 기쁨 입력: "))
#     smile = smile + happy
#     print(smile - happy)
#     if heart <= 0 or smile >= 100:
#         exit()

#알람 45분 일찍 맞추기
# a,b =map(int, input().split())
# b = b -45
# if a >24 or b >60:
#     print(" 다시 입력해주세요")
# elif b - 45 < 0:
#     b = b + 60
#     a = a-1
#     if a == -1:
#         a = a + 12
# print(a,b)

#1037약수 reverse 버전
# a = int(input())
# divisor = []
# for i in range(2,a):
#     if a % i == 0:
#         divisor.append(i)
#     else:
#         continue
# print(len(divisor))
# print(divisor)

#1037약수 sort버전
# a = int(input())
# if a == 1:
#     b = int(input())
#     print(b *b)
# else: 
#     for _ in range(a):
#     dk = list(map(int, input().split()))
#     dk.sort()
#     len(dk)
#     print(dk[0] * dk[len(dk) - 1])

#1037선배님 버전
n = int(input())
a = list(map(int,input().split()))
print(min(a)*max(a))
    

#1이 몇개냐에 따라 다름 111111 % 7 = 0 1 6개 이런식
#(3+7) % 3 덧셈 뺄셈 나머지 가능 = (3%3 + 7%3) % 3
# 11 % 7 = (10 + 1) % 7 = (10%7 + 1%7) % 7
# 111 = 11*10 +1
# 1111 = 111 * 10 + 1

# while True:
#     try:
#         n = int(input())
#     except:
#         break
#     num = 0
#     cnt = 1

#     while True:
#         num = num * 10 + 1
#         num = num % n

#         if num == 0:
#             print(cnt)
#             break
#         cnt += 1

# for i in range(1,10):
#     for j in range(1,10):
#         print(i*j)







