# 모두 암기 해야함.
# 리스트 메서드

# 1
# len: 리스트의 길이를 반환하는 내장 함수
numbers = [1, 2, 3, 4, 5]
print(len(numbers))  # 5

# 2
# del: 리스트에서 특정 요소를 삭제하는 연산자
numbers = [1, 2, 3, 4, 5]
del numbers[2]
print(numbers)  # [1, 2, 4, 5]

# 3
# append: 리스트의 맨 뒤에 새로운 요소를 추가하는 메서드
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers)  # [1, 2, 3, 4, 5, 6]

# 4
# sort: 리스트를 오름차순으로 정렬하는 메서드
numbers = [3, 2, 4, 1, 5]
numbers.sort()
print(numbers)  # [1, 2, 3, 4, 5]

# 리스트를 내림차순으로 정렬
numbers.sort(reverse=True)
print(numbers)  # [5, 4, 3, 2, 1]

# 4_2
# sorted: 리스트를 원래 순서를 건드리지 않고
# 새로운 객체에 오름차순으로 정렬하여 반환하는 메서드
numbers = [3, 2, 4, 1, 5]
numbers_2 = sorted(numbers)
print(numbers)   # [3, 2, 4, 1, 5]
print(numbers_2)  # [1, 2, 3, 4, 5]

# 5
# reverse: 리스트의 요소 순서를 반대로 뒤집는 메서드
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)  # [5, 4, 3, 2, 1]

# 6
# index: 리스트에서 특정 요소의 인덱스를 반환하는 메서드
fruits = ['apple', 'banana', 'cherry']
print(fruits.index('banana'))  # 1

# 7
# insert: 리스트의 특정 위치에 요소를 삽입하는 메서드
numbers = [1, 2, 3, 4, 5]
numbers.insert(2, 10)
print(numbers)  # [1, 2, 10, 3, 4, 5]

# 8
# remove: 리스트에서 특정 요소를 제거하는 메서드
numbers = [1, 2, 3, 4, 5]
numbers.remove(3)
print(numbers)  # [1, 2, 3, 4, 5]

# 9
# pop: 리스트에서 마지막 요소를 빼낸 뒤, 그 요소를 삭제하는 메서드
numbers = [1, 2, 3, 4, 5]
numbers.pop(3)
print(numbers)  # [1, 2, 3, 5]

# 10
# count: 리스트에서 특정 요소의 개수를 세는 메서드
numbers = [1, 2, 3, 3, 4, 5]
print(numbers.count(3))  # 2

# 11
# extend: 리스트를 확장하여 새로운 요소들을 추가하는 메서드
numbers = [1, 2, 3]
numbers.extend([4, 5, 6])
print(numbers)  # [1, 2, 3, 4, 5, 6]

# 12
# += 연산자를 사용해서도 구현
numbers = [1, 2, 3]
numbers += [4, 5, 6]
print(numbers)  # [1, 2, 3, 4, 5, 6]
