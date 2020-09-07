def bisect_get_left_right(word, left_search):
    start = 0
    end = len(word)
    if left_search:
        while start <= end:
            mid = (start + end) // 2
            if word[mid] == '?':
                start = mid + 1
            else:
                end = mid - 1
        return end + 1
    else:
        while start <= end:
            mid = (start + end) // 2
            if word[mid] == '?':
                end = mid - 1
            else:
                start = mid + 1
        return len(word) - start

def solution(words, queries):
    answer = []
    for query in queries:
        length = len(query)
        # 물음표의 왼쪽 쿼리
        searcher = ''
        left_search = query[0] == '?'
        query_length = bisect_get_left_right(query, left_search)
        if left_search:
            searcher = query[query_length:]
        else:
            searcher = query[:-query_length]
        # print(searcher)
        count = 0
        for word in words:
            if len(word) != length:
                continue
            elif left_search and word[query_length:] == searcher:
                count += 1
            elif not left_search and word[:-query_length] == searcher:
                count += 1
        answer.append(count)
    return answer

# 효율성 통과하지 못함 시간 복잡도 대략 O(N^2 log N)