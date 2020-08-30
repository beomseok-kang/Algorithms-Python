a = '고추장 닭날개 조림으로 하겠습니다. 근데 이제 바질을 곁들인'

def reverse_string_in_words(s):
    temp_arr = s.split()
    temp_arr.reverse()
    return ' '.join(temp_arr)

print(reverse_string_in_words(a))