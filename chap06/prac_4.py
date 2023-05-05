# 2116313 손수경
M = 13					# 테이블의 크기
table = [None]*M			# 테이블 만들기: None으로 초기화


def hashFn(key):		# 해시 함수
    return key % M

# 1번을 해보세요!


def lp_insert(key):
    id = hashFn(key)
    count = M
    while count > 0 and (table[id] != None):
        id = (id + 1 + M) % M
        count -= 1
    if count > 0:
        table[id] = key
    return


# 2번을 해보세요!
n = int(input())
lp_insert(None)
for i in range(n):
    lp_insert.put(int(input()))

# 출력합니다!
print(table)
