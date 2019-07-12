import os

# 1. 해당 파일들이있는 위치로 ㅣ동
os.chdir(r'C:\Users\student\Desktop\TIL\00_startcamp\02_day\change_filenames')   
# 1. 전체 문자열로 해야되 백슬래쉬가 있어서 앞에 r을 붙어줘야함 (윈도위에서만)
# 2. 현재 폴더 안에 모든 파일 이름을 수집 
# filenames = os.listdir('디렉토리 주소')
filenames = os.listdir('.')
# print(filenames)
# 각각의 파일명을 돌면서 수정한다. 
for filename in filenames:
    os. rename(filename, f'SAMSUN_{filename}') 