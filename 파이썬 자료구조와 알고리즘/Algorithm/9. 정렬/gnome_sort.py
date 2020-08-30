def gnome_sort(seq):
    i = 0
    while i < len(seq):
        print(seq)
        if i == 0 or seq[i-1] <= seq[i]:
            i += 1
        else:
            seq[i], seq[i-1] = seq[i-1], seq[i]
            i -= 1
    return seq

list_test = [5, 3, 2, 4]
gnome_sort(list_test)
print(list_test)