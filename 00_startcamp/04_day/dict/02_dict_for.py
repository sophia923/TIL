# 딕셔너리 반복문 활용하기

lunch = {
    '중국집' : '02-1234-1234',
    '분식집' : '031-1244-1234',
    '일식집' : '02-654-1231'
}

#기본 활용
for key in lunch:
    print(lunch[key])  # 이렇게하면 키 value를 가져올수 있음(즉 전화번호)


# .items() key and value를 동시에 뽑음
for key, value in lunch.items():
    print(key,value)


# value만 가져오기 .values
for value in lunch.values():
    print(value)


# key만 가져오기 .keys
for key in lunch.keys():
    print(key)