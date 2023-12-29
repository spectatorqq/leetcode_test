import numpy as np
import jieba


def stop_list(file):
    stopwords = [lines.strip() for lines in open(file, 'r', encoding='utf8').readlines()]
    return stopwords


def cosine_similarity(s: str, s2: str, stopwords: list) -> float:
    seg1 = [word for word in jieba.cut(s) if word not in stopwords]
    seg2 = [word for word in jieba.cut(s2) if word not in stopwords]
    word_list = list(set(seg1 + seg2))
    word_count_vec_1 = []
    word_count_vec_2 = []
    for word in word_list:
        word_count_vec_1.append(seg1.count(word))
        word_count_vec_2.append(seg2.count(word))
    vec_1 = np.array(word_count_vec_1)
    vec_2 = np.array(word_count_vec_2)

    num = vec_1.dot(vec_2.T)
    denom = np.linalg.norm(vec_1) * np.linalg.norm(vec_2)
    cos = num / denom
    sim = 0.5 + 0.5 * cos
    return sim


def test_sort():
    a = [[1, 4], [2, 3], [3, 5], [4, 2]]
    b = list(sorted(a, key=lambda x: x[1], reverse=True))
    print(b)


def index_test():
    a = ['qwieo\njiofj']
    b = a.index('qwieo\njiofj')
    print(b)


if __name__ == '__main__':
    index_test()
    # test_sort()
    # str1 = "重庆是一个好地方"
    # str2 = "重庆好吃的在哪里"
    # str3 = "重庆是好地方"
    # stop_txt = r'E:\office_documents\济南农商行\开发\stopwords\stopwords\cn_stopwords.txt'
    # stop_words = stop_list(stop_txt)
    # sim1 = cosine_similarity(str1, str2, stop_words)
    # sim2 = cosine_similarity(str1, str3, stop_words)
    # print("sim1 ：", sim1)
    # print("sim2:", sim2)
    # sorted(stop_words)
