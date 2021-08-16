# type
print(type([7,5,2,3,6])) # => <class 'list'>
print(type(3.14))            # => <class 'float'>
print(type(True))            # => <class 'bool'>
print(type("True"))          # => <class 'str'>

# max, min
print(max(2, 5))             # => 5
print(min(2, 7, 5, 11, 6))   # => 2

# str : 숫자를 문자열로 바꿀 수 있음
my_str = str(257138)
print(my_str)                # => 257138
print(type(my_str))          # => <class 'str'>

# append, insert, del, index, reverse
my_list = [7, 5, 2, 3, 6]

my_list.append(9)            # 끝에 9 추가
print(my_list)               # => [7, 5, 2, 3, 6, 9]

my_list.insert(2, 11)        # 2번 인덱스에 11 추가
print(my_list)               # => [7, 5, 11, 2, 3, 6, 9]

del my_list[2]               # 2번 인덱스 값 삭제
print(my_list)               # => [7, 5, 2, 3, 6, 9]

my_index = my_list.index(9)  # 리스트에서 9의 인덱스
print(my_index)              # => 5

my_list.reverse()            # 리스트 뒤집기
print(my_list)               # => [9, 6, 3, 2, 5, 7]

# slicing
# 리스트의 일부를 받아올 수 있음. 시간 복잡도는 슬라이싱의 범위 길이에 비례
# my_list[a:b]를 하면 시간 복잡도는 O(b-a)
my_list = [7, 5, 2, 3, 6]

print(my_list[1:4])          # => [5, 2, 3]
print(my_list[:4])           # => [7, 5, 2, 3]
print(my_list[1:])           # => [5, 2, 3, 6]
print(my_list[:])            # => [7, 5, 2, 3, 6]
print(my_list[::2])          # => [7, 2, 6]

