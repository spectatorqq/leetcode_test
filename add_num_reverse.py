def add_num():
    """
    给两个数分别放在 reversed list 中，求两数合，也放在reversed list 中
    :return:
    """
    a = input()
    b = input()
    a = list(reversed(list(a)))
    b = list(reversed(list(b)))
    # print(a)
    # print(b)
    c = ''
    small_list = a if len(a) < len(b) else b
    bigger_list = a if len(a) >= len(b) else b
    for i in range(len(small_list)):
        temp_sum = int(small_list[i]) + int(bigger_list[i])
        if temp_sum >= 10:
            bigger_list[i + 1] = str(int(bigger_list[i + 1]) + 1)
        c += str(temp_sum)[-1]

    for i in range(len(small_list), len(bigger_list)):
        if int(bigger_list[i]) >= 10:
            bigger_list[i + 1] = str(int(bigger_list[i + 1]) + 1)
        bigger_list[i] = bigger_list[i][-1]

    c += ''.join(bigger_list[len(small_list):])
    print(c)
    print(''.join(reversed(list(c))))


if __name__ == '__main__':
    add_num()
