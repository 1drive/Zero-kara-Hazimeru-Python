# 한 코끼리가 그의 친구를 방문하기로 결심했습니다.
# 코끼리의 집은 point 0에 위치해 있고, 그의 친구의 집은 동일 선상 point x에 위치해 있습니다.
# 코끼리는 한 번에 1, 2, 3, 4 또는 5 좌표를 움직일 수 있습니다.
# 코끼리가 그의 친구의 집까지 도달하는데 걸리는 최소한의 걸음수를 결정하세요.
import math

x = int(input())
print(math.ceil(x/5))