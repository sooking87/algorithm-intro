# 2116313 손수경
# 이진트리를 위한 노드 클래스
class TNode:
    def __init__(self, data, left, right):  # 생성자
        self.data = data 			# 노드의 데이터
        self.left = left			# 왼쪽 자식을 위한 링크
        self.right = right			# 오른쪽 자식을 위한 링크


# 1번을 해보세요!
def calc_height(root):
    if root in None:
        return 0
    hLeft = calc_height(root.left)
    hRight = calc_height(root.right)
    return max(hLeft, hRight) + 1


# 2번을 해보세요!
n = int(input())
binary_tree = [TNode(0, 0, 0) for _ in range(n)]
for i in range(n):
    data, left, right = [int(m) for m in input().split()][:3]


# 출력합니다!
root = binary_tree[0]
print("트리의 높이 =", calc_height(root))
