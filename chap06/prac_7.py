# 2116313 손수경
M = 13              # 테이블의 크기
table = [None]*M    # 테이블 만들기: None으로 초기화


# 1번을 해보세요!
def hashFn(key):
    return 0


# 선형 조사법의 삽입 알고리즘
def lp_insert(key):
    id = hashFn(key)
    count = M
    while count > 0 and (table[id] != None and table[id] != -1):
        # while count>0 and (table[id] != None) :
        id = (id + 1 + M) % M
        count -= 1
    if count > 0:
        table[id] = key
    return


# 2번을 해보세요!
lp_insert(None)


# 출력합니다!
print(table)
