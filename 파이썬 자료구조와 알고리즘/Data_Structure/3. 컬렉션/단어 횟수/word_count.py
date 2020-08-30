from collections import Counter

x = 'hello hello hello world world'

def word_count(string):
    temp_arr = string.split(' ')
    counts = Counter(temp_arr)
    return counts

print(word_count(x))
