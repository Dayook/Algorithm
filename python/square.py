#n x m 크기의 직사각형을 자르려고 합니다. 직사각형의 각 변은 x축, y축에 평행하며, 직사각형의 왼쪽 아래 꼭짓점의 좌표를 (0, 0), 오른쪽 위 꼭짓점의 좌표를 (n, m)으로 하겠습니다. 다음은 n = 3, m = 4인 직사각형이 놓여있는 모습을 나타낸 그림입니다.
# 위 그림과 같이 선분이 지나가는 모든 지점을 잘라낸 후 만들어지는 작은 직사각형 중 넓이가 가장 큰 직사각형은 색칠한 부분이며 넓이는 4가 됩니다.
# 직사각형의 오른쪽 위 꼭짓점을 나타내는 좌표 n과 m, 선분의 x축 좌표가 들어있는 배열 x_axis, y축 좌표가 들어있는 배열 y_axis가 매개변수로 주어질 때, 직사각형을 모두 잘라낸 후 만들어지는 작은 직사각형 중 넓이가 가장 큰 직사각형을 찾아 그 넓이를 return 하도록 solution 함수를 완성해주세요.
def solution(n, m, x_axis, y_axis):
    answer = 0
    # 0에서 inter_x까지,inter_x - inter_x ,interx에서 n까지
    # 중에 가장 큰 것을 구한다음 둘이 곱해준다
    max_x = 0
    max_y = 0
    x_axis.insert(0,0)
    x_axis.append(n)
    for i in range(len(x_axis)-1) :
        if x_axis[i+1] - x_axis[i] > max_x:
            max_x = x_axis[i+1] - x_axis[i]

    y_axis.insert(0,0)
    y_axis.append(m)
    for i in range(len(y_axis)-1):
        if y_axis[i+1] - y_axis[i] > max_y:
            max_y = y_axis[i+1] - y_axis[i]

    print(max_x * max_y)
    return answer


solution(4, 4, [1], [3])
