def get_su(n: int):
    """
    获取 n 以内的素数个数
    2 1,2
    3 1, 3
    4, 1, 2, 4
    5 1, 5
    6 1, 2, 3, 6
    :param n:
    :return:
    """
    su = []
    if n < 2:
        return 0
    else:
        for i in range(2, n+1):
            zhi = []
            for j in range(1, i+1):
                if i % j == 0:
                    zhi.append(j)
            if len(zhi) == 2:
                su.append(i)

    print(len(su), su)
    return len(su)


if __name__ == '__main__':
    for i in range(2, 100):
        get_su(i)


