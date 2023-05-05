# 2116313 손수경
M = 13					# 테이블의 크기


def hashFn(key):		# 해시 함수
    return key % M

# 1번을 해보세요!


def lp_delete(key):
    id = hashFn(int(key))
    count = M
    while count > 0:
        if table[id] == None:
            return
        if table[id] != -1 and table[id] == key:
            table[id] = -1
            return
        id = (id + 1 + M) % M
        count -= 1


# 2번을 해보세요!
table = [None if m == 'None' else int(m) for m in input().split()]
key = int(input())


# 출력합니다!
lp_delete(key)
print(table)
