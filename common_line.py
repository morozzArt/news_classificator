def convert(line):
    trash = '?!/|:,.@#)""<<>>(*'
    article = line.lower()
    for char in article:
        if char in trash:
            article = article.replace(char, ' ')
    return article