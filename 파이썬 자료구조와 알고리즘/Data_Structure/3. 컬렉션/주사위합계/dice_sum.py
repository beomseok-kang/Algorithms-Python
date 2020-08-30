s = 6

def dice_combi_for_sum(sum):
    temp_arr = []
    num = 0
    for i in range(1,7):
        for j in range(1,7):
            if i + j == sum:
                temp_arr.append((i,j))
                num += 1
    return [num, temp_arr]

print(dice_combi_for_sum(6))

        