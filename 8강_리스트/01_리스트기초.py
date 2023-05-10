# 리스트 생성하기
animals = ["사자", "호랑이", "고양이", "강아지"]

# 데이터 접근하기
name = animals[3] # 강아지 출력

# 데이터 추가하기
animals.append("하마")
animals.append(1) # 숫자 데이터도 들어감

# 데이터 삭제하기
del animals[-1] # 마지막 데이터 삭제하기

# 리스트 슬라이싱
slicing = animals[1:3] # [ '호랑이', '고양이']

# 리스트 길이
length = len(animals)  # 5

# 리스트 정렬
animals.sort() # 오름차순으로 바뀜
animals.sort(reverse=True) # 내림차순으로 출력

print(animals)


