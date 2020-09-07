def question_length(query, left_search):
  if left_search:
    return len(query) - len(query.lstrip('?'))
  else:
    return len(query) - len(query.rstrip('?'))

def search_left(array, query, qm_length, start, end, left_search):
    if not array:
        return 0
    mid = (start + end) // 2
    if not left_search:
        while start <= end:
            mid = (start + end) // 2
            if max(array[mid], query) == query: # query_min = query, "fro??"
                start = mid + 1
            else:
                end = mid - 1
        return end
    else:
        query = ''.join(reversed(query))
        while start <= end:
            mid = (start + end) // 2
            if max(array[mid], query) == query:
                start = mid + 1
            else:
                end = mid - 1
        return end

def search_right(array, query, qm_length, start, end, left_search):
    if not array:
        return 1
    mid = (start + end) // 2
    if not left_search:
        query = query[:-qm_length] + '~' * qm_length
        while start <= end:
            mid = (start + end) // 2
            if min(array[mid], query) == query:
                end = mid - 1
            else:
                start = mid + 1
        return start
    else:
        query = ''.join(reversed(query))[:-qm_length] + '~' * qm_length
        while start <= end:
            mid = (start + end) // 2
            if min(array[mid], query) == query:
                end = mid - 1
            else:
                start = mid + 1
        return start

def solution(words, queries):
    arrays = [[[] for _ in range(2)] for _ in range(10001)]
    for word in words:
        arrays[len(word)][0].append(word)
    for array in arrays:
        array[1] = list(map(lambda x: ''.join(reversed(x)), array[0]))
        array[0].sort()
        array[1].sort()
    counts = []
    for query in queries:
        query_len = len(query)
        left_search = (query[0] == '?')
        array = arrays[query_len][int(left_search)]
        qm_length = question_length(query, left_search)

        start = 0
        end = len(array) - 1
        left = search_left(array, query, qm_length, start, end, left_search)
        right = search_right(array, query, qm_length, start, end, left_search)
        counts.append(right - left - 1)
    return counts

words = ['frodo', 'front', 'frost', 'frozen', 'frame', 'kakao']
queries = ['fro??', '????o', 'fr???', 'fro???', 'pro?', '?????']
print('solution: ', solution(words, queries))

# 통과.
# 시간 복잡도: 대략 O(N log N)