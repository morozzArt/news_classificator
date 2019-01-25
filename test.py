import math
from common_line import convert
themes = ('science', 'style', 'culture', 'life', 'economics', 'business', 'travel', 'forces', 'media', 'sport')


def key_of_max(d):
    v = list(d.values())
    k = list(d.keys())
    return k[v.index(max(v))]


def sum_theme(themes):
    sum = 0
    for key, value in themes.items():
        sum = sum + value
    return sum


def classification(artical, dict_word, dict_theme_count, dict_theme_word):
    servive_word = ['без', 'в', 'до', 'для', 'за', 'из', 'к', 'над', 'о', 'об', 'под', 'пред', 'с', 'у', 'пред', 'про',
                    'от', 'на', 'и', 'или', 'но', 'без', 'во', 'по', 'со']
    line = convert(artical)
    d = sum_theme(dict_theme_count)
    dc = 0
    v = len(dict_word)
    probability = {}
    word_list = line.split()
    for i in themes:
        dc = dict_theme_count[i]
        res = 0
        for word in word_list:
            if word in servive_word:
                continue
            if word in dict_word.keys():
                wic = dict_word[word][i]
            else:
                wic = 0
            res = res + math.log((wic + 1) / (v + dict_theme_word[i]))
        result = res + math.log(dc/d)
        probability.update({i: result})
    return key_of_max(probability)


def testing(tuple_from_train):
    dict_words = tuple_from_train[0]
    dict_theme_count = tuple_from_train[1]
    dict_theme_word = tuple_from_train[2]
    out = open('out.txt', 'w')
    with open('news_test.txt') as file_for_text:
        for line in file_for_text:
            them = classification(line, dict_words, dict_theme_count, dict_theme_word)
            out.write(them + '\n')
