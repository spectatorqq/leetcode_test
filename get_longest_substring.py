def get_longest_substring(s):
    """
    获取最长子串
    :return:
    """
    # long_str = input()
    # max_len = len(list(set(long_str)))
    # if max_len == len(long_str):
    #     return max_len
    # print(max_len)
    # for i in range(max_len, 0, -1):
    #     for j in range(0, len(long_str) - i + 1,):
    #         if len(set(long_str[j: j + i])) == i:
    #             print(long_str[j: j + i])
    #             return i

    res = 0
    letter_dict = dict()
    index = -1
    max_len = len(set(s))
    for j in range(len(s)):
        if s[j] in letter_dict:
            index = max(letter_dict[s[j]], index)
        letter_dict[s[j]] = j
        res = max(j - index, res)
        if res == max_len:
            return res
    return res


if __name__ == '__main__':
    res = get_longest_substring('tmmzuxt')
    print(res)
