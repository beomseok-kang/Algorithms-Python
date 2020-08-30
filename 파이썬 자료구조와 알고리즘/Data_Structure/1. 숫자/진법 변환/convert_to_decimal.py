def convert_to_decimal (number, base) :
    num_list = list(str(number))
    num_temp = 0
    length = len(num_list)
    for i in range(length) :
        num_temp += int(num_list[i]) * (base ** (length - 1 - i))
    return num_temp

def test_convert_to_decimal() :
    number, base = 1001, 2
    assert(convert_to_decimal(number, base) == 9)
    print('테스트 통과!')

test_convert_to_decimal()