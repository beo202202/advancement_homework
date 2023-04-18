# 모두 암기 해야함.
# 문자열 메서드

# 1
# count: 문자열 내에서 특정 문자가 몇 개 있는지 세는 메서드
# 내장 함수
text = "Hello, World!"
count = text.count("l")
print(count)    # 3

# 2
# find: 문자열 내에서 특정 문자열이 처음 나오는 위치를 찾아주는 메서드
# str 클래스 내장 함수
# string.find(찾을 문자열 및 문자, 시작위치, 끝위치)
# string.find(찾을 문자열 및 문자)
# 없을 경우 -1
text = "Hello, World!"
position = text.find("world")
print(position)  # 7

# 3
# index: 문자열 내에서 특정 문자열이 처음 나오는 위치를 찾아주는 메서드
# str 클래스 내장 함수
# 없을 경우 ValueError
# string.index(찾을 문자열 및 문자)
# string.index(찾을 문자열 및 문자, 시작위치, 끝위치
text = "Hello, World!"
try:
    position = text.index("World")
    print(position)  # 7
except ValueError:
    print("찾는 문자열이 없습니다.")

# 4
# join: 특정 문자열을 기준으로 다른 문자열들을 합쳐주는 메서드
# string.join()

fruits = ["apple", "banana", "cherry"]
joined_fruits = ", ".join(fruits)
print(joined_fruits)  # "apple, banana,m cherry"

# 5
# upper: 문자열 내의 모든 소문자를 대문자로 바꾸는 메서드
# lower: 문자열 내의 모든 대문자를 소문자로 바꾸는 메서드
# 대소문자를 구분하지 않고 검색할 때 유용하게 쓰임
text = "Hello, World!"
uppercase_text = text.upper()
print(uppercase_text)  # "HELLO, WORLD!"

lowercase_text = text.lower()
print(lowercase_text)  # "hello, world!"

# 6
# replace: 문자열 내에서 특정 문자열을 다른 문자열로 바꾸는 메서드
text = "Hello, World!"
replaced_text = text.replace("World", "Python")
print(replaced_text)  # "Hello, Python!"

# 7
# split: 문자열을 특정 문자를 기준으로 나누는 메서드(결과는 리스트 형태로 반환)
text = "apple,banana,cherry"
fruits = text.split(",")
print(fruits)  # ['apple', 'banana', 'cherry']
