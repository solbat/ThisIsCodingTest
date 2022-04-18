# 9-1.py 간단한 다익스트라 알고리즘 소스코드

import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정. python에서는 1e9를 실수로 처리하므로 int() 함수 사용함.

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 시작 노드 번호를 입