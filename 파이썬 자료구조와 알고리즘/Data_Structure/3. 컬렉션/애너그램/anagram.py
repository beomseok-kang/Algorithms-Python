from collections import Counter

a = 'helloworld'
b = 'elwloorhld'
c = 'somerandomword'

def is_anagram(str_1, str_2):
    count1 = Counter(str_1)
    count2 = Counter(str_2)
    return count1 == count2

print(is_anagram(a,b))
print(is_anagram(a,c))