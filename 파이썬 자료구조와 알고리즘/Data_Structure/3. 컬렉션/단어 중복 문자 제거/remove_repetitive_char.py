from collections import Counter

x = 'aaabbbcdeefffghh'

def remove_repetitive_char(string):
    counts = Counter(string)
    result = []
    result.extend(string)
    to_remove = []
    for item in counts.items():
        if item[1] > 1: # value
            to_remove.append(item)
    for item in to_remove:
        for i in range(item[1]):
            result.remove(item[0])
    return ''.join(result)

print(remove_repetitive_char(x))