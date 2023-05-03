# 2116313 손수경
# 이진트리를 위한 노드 클래스
class TNode:
    def __init__(self, data, left, right):  # 생성자
        self.data = data 			# 노드의 데이터
        self.left = left			# 왼쪽 자식을 위한 링크
        self.right = right			# 오른쪽 자식을 위한 링크


# 1번을 해보세요!
def postorder(n):
    return None


# 2번을 해보세요!
binary_tree = [None]


# 출력합니다!
root = binary_tree[0]
print('Post-Order : ', end='')
postorder(root)
print()
