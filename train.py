from common_line import convert
def learning():
    themes_count = {'science': 0, 'style': 0, 'culture': 0, 'life': 0, 'economics': 0, 'business': 0, 'travel': 0,
                    'forces': 0,
                    'media': 0, 'sport': 0}
    themes_word = {'science': 0, 'style': 0, 'culture': 0, 'life': 0, 'economics': 0, 'business': 0, 'travel': 0,
                   'forces': 0,
                   'media': 0, 'sport': 0}
    servive_word = ['без', 'в', 'до', 'для', 'за', 'из', 'к', 'над', 'о', 'об', 'под', 'пред', 'с', 'у', 'пред', 'про',
                    'от', 'на', 'и', 'или', 'но', 'без', 'во', 'по', 'со']
    words = {}
    with open('news_train.txt') as file_for_train:
        for line in file_for_train:
            line = convert(line)
            article = line.split('\t')
            current_theme = line[:len(article[0])]
            themes_count.update({current_theme: themes_count.get(current_theme) + 1})
            word_list = line[len(article[0]) + 1: len(article[1] + article[2])].split()
            for word in word_list:
                if word in servive_word:
                    continue
                themes_word[current_theme] += 1
                if word in words.keys():
                    if words[word][current_theme] is None:
                        words[word][current_theme] = 1
                    else:
                        words[word][current_theme] = words[word][current_theme] + 1
                else:
                    words.update({word: {'science': 0, 'style': 0, 'culture': 0, 'life': 0,
                                         'economics': 0, 'business': 0, 'travel': 0, 'forces': 0,
                                         'media': 0, 'sport': 0}})
                    words[word][current_theme] = 1
        return  words, themes_count, themes_word

