# 모두 암기 해야함.
# 딕셔너리 메서드

# 1
# 딕셔너리 초기화
# 빈 딕셔너리 만드릭
empty_dict = {}

# 초기화할 딕셔너리 만들기
my_dict = {"apple": 1, "banana": 2, "orange": 3}

print(my_dict)

# 2
# 딕셔너리 쌍 추가
my_dict = {"apple": 1, "banana": 2, "orange": 3}

my_dict["grape"] = 4
print(my_dict)  # {"apple": 1, "banana": 2, "orange": 3, "grape": 4}

# 3
# del: 딕셔너리에서 특정 요소를 삭제
my_dict = {"apple": 1, "banana": 2, "orange": 3}
del my_dict["apple"]
print(my_dict)  # {"banana": 2, "orange": 3}

# 4
# 딕셔너리에서 특정 Key에 해당하는 Value를 얻는 방법
# 딕셔너리에 Key가 없는 경우, KeyError
my_dict = {"apple": 1, "banana": 2, "orange": 3}

print(my_dict["banana"])  # 2

# 5
# items: 딕셔너리의 모든 키와 값을 튜플 형태의 리스트로 반환
person = {'name': "john", 'age': 30, 'gender': 'mail'}

items = person.items()
print(items)  # dict_items([('name', 'John'), ('age', 30), ('gender', 'male')])

# 6
# clear: 딕셔너리의 모든 요소를 삭제
person = {'name': 'John', 'age': 30, 'gender': 'male'}

person.clear()
print(person)  # {}

# 7
# get: 딕셔너리에서 지정한 키에 대응하는 값을 반환
# 딕셔너리에 Key가 없는 경우, None 반환
# 직접 Key를 요청하는 것보다 get이 더 안전함.(None > KeyError)
person = {'name': 'John', 'age': 30, 'gender': 'male'}

name = person.get('name')
print(name)  # John

email = person.get('email')
print(email)  # None

# 기본값을 설정할 수 있음
email = person.get('email', 'unknown')
print(email)  # unknown

# 8
# in: 해당 Key가 딕셔너리 안에 있는지 확인
person = {'name': 'John', 'age': 30, 'gender': 'male'}

print('name' in person)  # True
print('email' in person)  # False

# 9
# keys: key들만 반환

# 10
# values: value들만 반환
