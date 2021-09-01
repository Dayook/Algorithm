# 제곱근 사용을 위한 sqrt 함수
from math import sqrt

# 두 좌표의 직선 거리를 계산해주는 함수
def distance(store1, store2):
  return sqrt((store1[0] - store2[0]) ** 2 + (store1[1] - store2[1]) ** 2)


# 좌표 리스트를 파라미터로 받고, 리스트 안에서 가장 가까운 두 매장을 리턴하는 함수를 완성하시오
def closest_pair(coordinates):
  dis = 999
  for i in coordinates:
    for j in coordinates:
      if i != j and distance(i, j) < dis:
        dis = distance(i,j)
        pair = [i, j]
  return pair 
  


test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(closest_pair(test_coordinates))