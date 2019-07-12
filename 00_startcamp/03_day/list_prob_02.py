'''
문제 2.
자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
'''

numbers = int(input('Enter a number: '))

# 아래에 코드를 작성해 주세요.

# for j in range(1,n+1):
#     a=[]
#     for i in range(1,j+1):
#         print(i,sep=" ",end" ")
#     if(i<j):
#         print("+", sep=" ",end=" ")
#     a.append(i)
#     print("=",sum(a))
# print()


# int('100') => 100

for i in range(numbers):
    print(i+1)