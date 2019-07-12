# DOCstring
"""
다음과 같은 내용의 파일 quest.txt 가 있다.
0
1
2
3
이 파일의 내용을 다음과 같이 역순으로  reverse_quest.txt 라는 파일로 저장하시오.
"""
# 1. 읽기
# 2. 뒤집고
# 3. 작성하기



# with open('quest.txt','r') as f:
#     lines = f.readlines()
#     for line in reversed(lines):
#         print(line.strip())

# with open('reverse_quest.txt','w') as f:
#     for line in reversed(lines):
#         f.write(line) 
  
# # with open('quest.txt','w') as f:
# #     for i in reversed(range(4)):
# #         f.write(f'{i}\n')

# # with open('revers_quest.txt','w') as f:
# #     for line in lines:
# #         f.write(line)


# # lines. reverse()

# # with open('reverse_quest.txt'.'w') as f:
# #     f.writelines(lines)


# # 1. quest.txt 파일을 읽고
# with open('quest.txt', 'r') as f:
#     lines = f.readlines() 
        
# # 2. 읽은 것을 기반으로 뒤집고(확인용)
# for i in reversed(lines):
#     print(i.strip())
    
# # 3. reverse_quest.txt 파일 작성하기
# with open('reverse_quest.txt', 'w') as f:
#     for i in reversed(lines):
#         f.writelines(i)

with open('quest.txt','w') as f:
    for i in range(4):
        f.write(f'{i}\n')

with open('quest.txt','r') as f:
    lines = f.readlines()
    lines.reverse()

with open('reverse_quest.txt','w') as f:
    for line in lines:
        f.write(line)